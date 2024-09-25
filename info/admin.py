from django.contrib import admin

from .models import About, SocialLink

#a65
#melarang data lebih dari satu
class AboutAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        count = About.objects.all().count()
        if count == 0:
            return True
        return False
    
admin.site.register(About, AboutAdmin)
admin.site.register(SocialLink)
