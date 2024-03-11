from rest_framework import permissions
from .models import Roomate,Team

class IsAuthenticatedAndTokenValid(permissions.BasePermission):
    def has_permission(self, request, view):
        token = request.headers.get('token')
        if not token:
            return False  # No token provided
        try:
            user = Roomate.objects.get(token=token)
            # Optionally, you can store the user in the request for later use
            request.user = user
            return True
        except Roomate.DoesNotExist:
            return False  # Token is not valid

class IsAuthenticatedAndTeamValid(permissions.BasePermission):
    def has_permission(self, request, view):
        token = request.headers.get('token')

        if not token:
            
            return False  # No token provided
        try:
            user = Roomate.objects.get(token=token)
            print(request.query_params.get('team_id'))
            # Optionally, you can store the user in the request for later use
            team=Team.objects.get(user_id=user.id,id=request.query_params.get('team_id'))
            request.user = user
            return True
        except:
            return False  # Token is not valid