from django.contrib import admin
from .models import Profile, Stat, Skill, Testimonial, Resume, Education, Experience, Service, ContactMessage, PortfolioItem, PortfolioImage, SocialProfile
from django.utils.html import format_html

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ("title", "email", "phone", "city", "freelance_status")
    search_fields = ("title", "email", "city")

@admin.register(Stat)
class StatAdmin(admin.ModelAdmin):
    list_display = ("label", "value")
    search_fields = ("label",)

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ("name", "level")
    list_filter = ("level",)
    search_fields = ("name",)

@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ("name", "position")
    search_fields = ("name", "position")


class EducationInline(admin.TabularInline):
    model = Education
    extra = 1  # Number of empty forms displayed

class ExperienceInline(admin.TabularInline):
    model = Experience
    extra = 1

@admin.register(Resume)
class ResumeAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'address')
    search_fields = ('name', 'email')
    inlines = [EducationInline, ExperienceInline]

@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ('degree', 'institution', 'year', 'resume')
    search_fields = ('degree', 'institution')

@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('title', 'company', 'start_year', 'end_year', 'resume')
    search_fields = ('title', 'company')


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'icon')  # Columns displayed in admin panel
    search_fields = ('title', 'description')  # Enable search
    list_filter = ('title',)  


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "subject", "is_resolved", "created_at")
    list_filter = ("is_resolved", "created_at")
    search_fields = ("name", "email", "subject", "message")

class PortfolioImageInline(admin.TabularInline):
    model = PortfolioItem.images.through  # Manages the ManyToMany relationship
    extra = 1

@admin.register(PortfolioItem)
class PortfolioItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'client', 'project_date')
    list_filter = ('category', 'project_date')
    search_fields = ('title', 'client', 'category')
    inlines = [PortfolioImageInline]
    exclude = ('images',)  # Hide default M2M field (managed via inlines)

@admin.register(PortfolioImage)
class PortfolioImageAdmin(admin.ModelAdmin):
    list_display = ('image_preview',)

    def image_preview(self, obj):
        return format_html('<img src="{}" style="max-height: 100px;" />', obj.image.url)
    image_preview.short_description = 'Preview'


@admin.register(SocialProfile)
class SocialProfileAdmin(admin.ModelAdmin):
    list_display = ('name', 'url', 'icon_class')