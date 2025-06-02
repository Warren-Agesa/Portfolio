from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='images/')
    url = models.URLField(blank=True)

    def __str__(self):
        return self.title

from django.db import models

class About(models.Model):
    content = models.TextField()
    location = models.CharField(max_length=100, blank=True)
    profession = models.CharField(max_length=100, blank=True)
    mission = models.CharField(max_length=255, blank=True)
    cv = models.FileField(upload_to='cv/', blank=True, null=True)

    def __str__(self):
        return "About Section"

    def save(self, *args, **kwargs):
        self.pk = 1  
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "About Section"
        verbose_name_plural = "About Section"

class Skill(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Education(models.Model):
    title = models.CharField(max_length=200)
    institution = models.CharField(max_length=200)
    year = models.CharField(max_length=50, blank=True)
    description = models.TextField(blank=True)  

    def __str__(self):
        return self.title

class Interest(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class HeroSection(models.Model):
    name = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=200)
    intro = models.TextField()
    image = models.ImageField(upload_to='images/', blank=True, null=True)

    def __str__(self):
        return "Hero Section"

    def save(self, *args, **kwargs):
        self.pk = 1  
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Hero Section"
        verbose_name_plural = "Hero Section"

        
class WorkExperience(models.Model):
    job_title = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    location = models.CharField(max_length=100, blank=True)
    start_date = models.CharField(max_length=50)  
    end_date = models.CharField(max_length=50, blank=True)  
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.job_title} at {self.company}"

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name} - {self.subject}"
    
class PersonalInfo(models.Model):
    birthday = models.CharField(max_length=50)
    website = models.URLField()
    phone = models.CharField(max_length=50)
    city = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    degree = models.CharField(max_length=50)
    email = models.EmailField()
    freelance = models.CharField(max_length=50)

    def __str__(self):
        return f"Personal Info for {self.email}"
    
class SocialLinks(models.Model):
    facebook = models.URLField(blank=True)
    whatsapp = models.URLField(blank=True)
    instagram = models.URLField(blank=True)
    twitter = models.URLField(blank=True)

    def __str__(self):
        return "Social Links"