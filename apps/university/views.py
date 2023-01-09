from django.shortcuts import render

from apps.blog.models import Blog
from apps.course.models import Course
from apps.profiles.models import Profile


def home_view(request):
    courses = Course.objects.all().order_by('-id')
    teachers = Profile.objects.filter(role=1).order_by('-id')[:3]
    posts = Blog.objects.order_by('-id')[:5]
    context = {
        'teachers': teachers,
        'courses': courses,
        'posts': posts,
    }

    return render(request, 'index.html', context)