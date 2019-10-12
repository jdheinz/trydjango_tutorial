# Django is a Model View Template (MVT)
# DRY = Don't Repeat Yourself
from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import get_template
# Don't Repeat Yourself = DRY

from .forms import ContactForm
from blog.models import BlogPost

def home_page(request):
    my_title = 'Hello there...'
    qs = BlogPost.objects.all()[:5]
    context = {"title":"Welcome to Try Django", 'blog_list': qs}

    return render(request, "home.html", context)

def about_page(request):
    return render(request, "about.html", {"title":"About"})

def contact_page(request):

    form = ContactForm(request.POST or None)
    if form.is_valid():
        print(form.cleaned_data)
        form = ContactForm()
    context = {
        "title":"Contact Us", 
        "form": form
    }
    return render(request, "form.html", context)

def social_page(request):
    return render(request, "social.html", {})

def example_page(request):
    context = {"title": "Example"}
    template_name = "hello_world.html"
    template_obj = get_template(template_name)
    rendered_item = template_obj.render(context)
    return HttpResponse(rendered_item)#return render(requesst, "social.html", {})
