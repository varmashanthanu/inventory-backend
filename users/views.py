from django.contrib.auth import get_user_model
from rest_framework import generics, status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.parsers import JSONParser
from rest_framework_simplejwt.token_blacklist.models import BlacklistedToken
from drf_spectacular.utils import extend_schema, OpenApiParameter
from .serializers import UserSerializer, RegisterSerializer, LogoutSerializer
from .permissions import IsAdmin, IsSelf
from .models import RevokedToken

User = get_user_model()



# ✅ REGISTER USER (Admin Only)
@extend_schema(
    request=RegisterSerializer,
    responses={201: UserSerializer},
    description="Register a new user (Admin only). Requires Authorization: Bearer <your-token>",
    parameters=[
        OpenApiParameter(
            name="Authorization",
            type=str,
            location=OpenApiParameter.HEADER,
            description="Bearer <your-auth-token>",
            required=True,
        ),
    ]
)
class UserRegisterView(generics.GenericAPIView):
    """
    Allows Admin users to create new users.
    """
    serializer_class = RegisterSerializer
    permission_classes = [IsAdmin]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({"user": UserSerializer(user).data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# ✅ LOGIN (JWT Token Generation)
@extend_schema(
    responses={200: {"access": "string", "refresh": "string"}},
    description="Login with username and password to receive JWT tokens (access & refresh)."
)
class CustomTokenObtainPairView(TokenObtainPairView):
    """
    Custom JWT Login View - Returns Access and Refresh tokens.
    """
    pass


# ✅ LOGOUT (Blacklist Refresh Token)
@extend_schema(
    description="Logout user by blacklisting their refresh token.",
    # request={"application/json": "string"},
    responses={200: {"message": "Successfully logged out"}}
)
class LogoutView(APIView):
    """
    Logout user by blacklisting their refresh token.
    """
    permission_classes = [permissions.IsAuthenticated]
    parser_classes = [JSONParser]  # Ensure JSON requests are parsed.
    serializer_class = LogoutSerializer

    def post(self, request):
        try:
            refresh_token = request.data.get("refresh")  # Extract refresh token from JSON body
            if not refresh_token:
                return Response({"error": "Refresh token is required."}, status=status.HTTP_400_BAD_REQUEST)

            # Blacklist the refresh token
            token = RefreshToken(refresh_token)
            token.blacklist()  # Blacklist the refresh token

            # Blacklist the access token
            access_token = request.headers.get("Authorization", "").split(" ")[1]  # Extract token from header
            RevokedToken.objects.create(token=access_token)  # Store it in DB

            return Response({"message": "Successfully logged out"}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)


# ✅ LIST ALL USERS (Admin Only)
@extend_schema(
    responses={200: UserSerializer(many=True)},
    description="Retrieve a list of all registered users. Requires Authorization: Bearer <your-token>",
    parameters=[
        OpenApiParameter(
            name="Authorization",
            type=str,
            location=OpenApiParameter.HEADER,
            description="Bearer <your-auth-token>",
            required=True,
        ),
    ]
)
class UserListView(generics.ListAPIView):
    """
    Lists all users.
    Only Admins can access this.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdmin]

# ✅ USER DETAIL / UPDATE / DELETE (Admin Only)
@extend_schema(
    responses={200: UserSerializer},
    description="Retrieve, update, or delete a specific user by ID. Requires Authorization: Bearer <your-token>",
    parameters=[
        OpenApiParameter(
            name="Authorization",
            type=str,
            location=OpenApiParameter.HEADER,
            description="Bearer <your-auth-token>",
            required=True,
        ),
    ]
)
class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    Allows Admins to retrieve, update, or delete user details.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdmin | IsSelf]
