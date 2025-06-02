from .models import SocialLinks

def social_links(request):
    return {'social': SocialLinks.objects.first()}