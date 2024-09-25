#a44
from info.models import SocialLink
from .models import Category


def get_categories(request):
    categories = Category.objects.all()
    return dict(categories=categories)




#a66
def get_social_links(request):
    social_links = SocialLink.objects.all()
    return dict(social_links=social_links)