from django.shortcuts import render, redirect, get_object_or_404
from .models import Profile, Stat, Skill, Testimonial, Resume, Service, ContactMessage, PortfolioItem
from .forms import ContactForm
from django.contrib import messages

def home(request):
    return render(request, 'index.html')

def about(request):
    profile = Profile.objects.first()  # Assuming one profile exists
    stats = Stat.objects.all()
    skills = Skill.objects.all()
    testimonials = Testimonial.objects.all()

    # Splitting skills into two columns
    skills_half = len(skills) // 2
    skills_data = {
        "first_half": skills[:skills_half],
        "second_half": skills[skills_half:]
    }

    context = {
        "about_description": "A brief description about Warren Karanja.",
        "profile": profile,
        "stats": stats,
        "skills": skills_data,
        "testimonials": testimonials,
    }

    return render(request, "about.html", context)

def resume(request):
    resume = Resume.objects.prefetch_related('education', 'experience').first()
    return render(request, 'resume.html', {'resume': resume})

def services(request):
    services = Service.objects.all()
    return render(request, 'service.html', {'services': services})


def portfolio(request):
    items = PortfolioItem.objects.all()
    return render(request, 'portfolio.html', {'items': items})

def portfolio_details(request, pk):
    item = get_object_or_404(PortfolioItem, pk=pk)
    return render(request, 'portfolio-details.html', {'item': item})

def contact(request):
    form = ContactForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        ContactMessage.objects.create(
            name=form.cleaned_data["name"],
            email=form.cleaned_data["email"],
            subject=form.cleaned_data["subject"],
            message=form.cleaned_data["message"]
        )
        messages.success(request, "Your message has been sent successfully!")
        return redirect("home")  
    
    return render(request, "contact.html", {"form": form})