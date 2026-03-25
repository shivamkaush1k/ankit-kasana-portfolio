from django.shortcuts import render
from .models import Profile, Skill, Experience, Education, Language, Hobby


def home(request):
    profile = Profile.objects.first()
    skills = Skill.objects.all()
    experiences = Experience.objects.all()
    educations = Education.objects.all()
    languages = Language.objects.all()
    hobbies = Hobby.objects.all()

    context = {
        'profile': profile,
        'skills': skills,
        'experiences': experiences,
        'educations': educations,
        'languages': languages,
        'hobbies': hobbies,
    }
    return render(request, 'portfolio/index.html', context)