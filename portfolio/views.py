from django.shortcuts import render, redirect
from django.contrib import messages
from .models import HeroSection, Skill, About, Education, Interest, WorkExperience, Project, PersonalInfo, SocialLinks
from .forms import ContactForm


def home(request):
    hero = HeroSection.objects.first()
    return render(request, 'portfolio/home.html', {'hero': hero})

def about(request):
    about = About.objects.first()
    skills = Skill.objects.all()
    education = Education.objects.all()
    interests = Interest.objects.all()
    hero = HeroSection.objects.first()
    work_experience = WorkExperience.objects.all()
    personal_info = PersonalInfo.objects.first()
    return render(request, 'portfolio/about.html', {
        'about': about,
        'skills': skills,
        'education': education,
        'interests': interests,
        'hero': hero,
        'work_experience': work_experience,
        'personal_info': personal_info,
    })

def projects(request):
    projects = Project.objects.all()
    return render(request, 'portfolio/projects.html', {'projects': projects})

def services(request):
    services = [
        {
            "icon": "laptop",
            "title": "Custom Web Applications",
            "description": "I build secure, scalable, and user-friendly web apps tailored to your business needs using Django and modern frontend frameworks."
        },
        {
            "icon": "phone",
            "title": "Responsive Website Design",
            "description": "Your website will look and work great on any device, ensuring the best experience for all your users."
        },
        {
            "icon": "cloud-upload",
            "title": "Deployment & Hosting",
            "description": "I handle deployment, hosting, and maintenance so your site is always fast, secure, and online."
        },
        {
            "icon": "tools",
            "title": "API Integration",
            "description": "Connect your site to third-party services or build custom APIs for mobile and web applications."
        },
        {
            "icon": "bar-chart",
            "title": "Analytics & SEO",
            "description": "Get found and grow your audience with integrated analytics and search engine optimization best practices."
        },
        {
            "icon": "chat-dots",
            "title": "Consulting & Support",
            "description": "From project planning to troubleshooting, I offer expert advice and ongoing support for your digital projects."
        },
    ]
    return render(request, 'portfolio/services.html', {"services": services})


def contact(request):
    return render(request, 'portfolio/contact.html')


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Thank you for your message! I will get back to you soon.")
            return redirect('home')  
    else:
        form = ContactForm()
    return render(request, 'portfolio/contact.html', {'form': form})

