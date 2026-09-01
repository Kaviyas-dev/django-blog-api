from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from .models import Profile

@login_required
def profile_view(request):
    profile,created = Profile.objects.get_or_create(user=request.user)
    return render(request,"profile.html",{"profile":profile})

def edit_profile(request):
    profile,created = Profile.objects.get_or_create(user=request.user)
    if request.method=="POST":
        request.user.username = request.POST.get("username")
        request.user.email = request.POST.get("email")
        request.user.save()
        profile.phone = request.POST.get("phone")
        profile.address = request.POST.get("address")
        profile.bio = request.POST.get("bio")

        if request.FILES.get("profile_image"):
            profile.profile_image = request.FILES.get("profile_image")
        profile.save()
        return redirect("profile")
    return render(request,"edit_profile.html",{"profile":profile})

