from rest_framework.permissions import BasePermission


def is_user_admin(user):
    """
    Check if the user is an admin. This would mean that the user either has the role of 'admin' or is a superuser.
    """
    return user.role == 'admin' or user.is_superuser

class IsAdmin(BasePermission):
    """Allows access only to Admin users."""

    def has_permission(self, request, view):
        return request.user.is_authenticated and is_user_admin(request.user)


class IsWarehouseManager(BasePermission):
    """Allows access only to Warehouse Managers."""

    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'warehouse_manager'


class IsCalibrationSpecialist(BasePermission):
    """Allows access only to Calibration Specialists."""

    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'calibration_specialist'


class IsInventoryClerk(BasePermission):
    """Allows access only to Inventory Clerks."""

    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'inventory_clerk'


class IsPurchasingAgent(BasePermission):
    """Allows access only to Purchasing Agents."""

    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'purchasing_agent'


class IsFinanceOfficer(BasePermission):
    """Allows access only to Finance Officers."""

    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'finance_officer'


class IsMechanic(BasePermission):
    """Allows access only to Mechanics."""

    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'mechanic'

class IsSelf(BasePermission):
    """Allows access only to the user itself."""

    def has_object_permission(self, request, view, obj):
        return request.user.is_authenticated and request.user == obj