from django.db import models
from django.utils import timezone

class Profile(models.Model):
    title = models.CharField(max_length=255)
    short_description = models.TextField()
    birthday = models.DateField()
    website = models.URLField(blank=True, null=True)
    phone = models.CharField(max_length=20)
    city = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    degree = models.CharField(max_length=100)
    email = models.EmailField()
    freelance_status = models.CharField(max_length=50)
    bio = models.TextField()
    profile_image = models.ImageField(upload_to='img/', default='default.jpg')

class Stat(models.Model):
    icon = models.CharField(max_length=100)  # CSS class for icon
    label = models.CharField(max_length=100)
    value = models.PositiveIntegerField()

class Skill(models.Model):
    name = models.CharField(max_length=100)
    level = models.PositiveIntegerField(help_text="Percentage value")

class Testimonial(models.Model):
    name = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    image = models.ImageField(upload_to="testimonials/")
    text = models.TextField()


class Resume(models.Model):
    name = models.CharField(max_length=255)
    professional_summary = models.TextField()
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    email = models.EmailField()

class Education(models.Model):
    resume = models.ForeignKey(Resume, related_name='education', on_delete=models.CASCADE)
    degree = models.CharField(max_length=255)
    institution = models.CharField(max_length=255)
    year = models.CharField(max_length=10)
    description = models.TextField()

class Experience(models.Model):
    resume = models.ForeignKey(Resume, related_name='experience', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    company = models.CharField(max_length=255)
    start_year = models.CharField(max_length=10)
    end_year = models.CharField(max_length=10, blank=True, null=True)
    responsibilities = models.TextField()  
    
class Service(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    icon = models.CharField(max_length=50, default="bi bi-activity")

    def __str__(self):
        return self.title
    

class ContactMessage(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()
    is_resolved = models.BooleanField(default=False)  
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.subject}"
    
class PortfolioItem(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    category = models.CharField(max_length=100)
    client = models.CharField(max_length=100, default="Default Client")
    project_date = models.DateField(default=timezone.now)
    project_url = models.URLField()
    images = models.ManyToManyField('PortfolioImage')

    def __str__(self):
        return self.title

class PortfolioImage(models.Model):
    image = models.ImageField(upload_to='portfolio/')