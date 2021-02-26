from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsAdminOrAttendant(BasePermission):
    """
    The request is authenticated as an Admin, or is an Attendant.
    """

    def has_permission(self, request, view):
        admin = request.user.role == 'admin'
        supervisor = request.user.role == 'supervisor'
        return bool(admin or attendant)
