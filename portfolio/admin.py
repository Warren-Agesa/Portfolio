from django.contrib import admin
from .models import Project, About, HeroSection, Skill, Education, Interest, WorkExperience, ContactMessage, PersonalInfo, SocialLinks

class SingletonModelAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        model = self.model
        return not model.objects.exists()

admin.site.register(Project)
admin.site.register(About, SingletonModelAdmin)
admin.site.register(HeroSection, SingletonModelAdmin)
admin.site.register(Skill)
admin.site.register(Education)
admin.site.register(Interest)
admin.site.register(WorkExperience)
admin.site.register(PersonalInfo, SingletonModelAdmin)

class ContactMessageAdmin(admin.ModelAdmin):
    readonly_fields = [f.name for f in ContactMessage._meta.fields]

    def has_change_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request):
        return False

admin.site.register(ContactMessage, ContactMessageAdmin)
admin.site.register(SocialLinks, SingletonModelAdmin)