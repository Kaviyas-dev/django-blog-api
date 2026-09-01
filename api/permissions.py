from rest_framework.permissions import BasePermission


class IsPostOwnerOrReadOnly(BasePermission):
    def has_object_permission(self,request,view,obj):
        # Anyone can view
        if request.method in ["GET","HEAD","OPTIONS"]:
            return True
        # Only author can modify/delete
        return obj.author == request.user