from django.contrib import admin
from blogapp.models import Profile,Post,Comments
# Register your models here.
admin.site.register(Profile)
admin.site.register(Post)
admin.site.register(Comments)