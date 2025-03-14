from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.tokens import AccessToken
from rest_framework.exceptions import AuthenticationFailed
from .models import RevokedToken

class CustomJWTAuthentication(JWTAuthentication):
    """
    Custom JWT Authentication that checks for revoked access tokens.
    """
    def authenticate(self, request):
        response = super().authenticate(request)  # Get user and token

        if response is not None:
            user, token = response
            # Check if the token is in the revoked list
            if RevokedToken.objects.filter(token=str(token)).exists():
                raise AuthenticationFailed("Token has been revoked. Please log in again.")

        return response
