from users.models import Profile

# def profile(request):
#     print(request.user)
#     return dict(
#         profile=Profile.objects.get(user=request.user)
#     )

def profile(request):
    if request.user.is_authenticated:
        try:
            profile = Profile.objects.get(user=request.user)
        except Profile.DoesNotExist:
            profile = None
    else:
        profile = None

    return {'profile': profile}