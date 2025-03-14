from drf_spectacular.extensions import OpenApiAuthenticationExtension
from users.authentication import CustomJWTAuthentication

class CustomJWTAuthenticationScheme(OpenApiAuthenticationExtension):
    """
    Register CustomJWTAuthentication for drf-spectacular (Swagger UI)
    """
    target_class = "users.authentication.CustomJWTAuthentication"
    name = "JWTAuth"

    def get_security_definition(self, auto_schema):
        return {
            "type": "http",
            "scheme": "bearer",
            "bearerFormat": "JWT"
        }
