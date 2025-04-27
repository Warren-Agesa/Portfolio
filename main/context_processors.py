from .models import SocialProfile

def social_profiles(request):
    profiles = SocialProfile.objects.all()
    return {'social_profiles': profiles}
