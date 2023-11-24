from django.shortcuts import render
from apps.settings import models
# Create your views here.
def index(request):
    settings = models.Settings.objects.latest("id")
    slide = models.Slide.objects.all()
    about = models.About.objects.latest("id")
    history = models.History.objects.latest("id")
    offer = models.Offer.objects.all()
    return render(request, "index.html", locals())

def blog(request):
    return render(request, "blog.html", locals())

def single_post(request):
    return render(request, "single_post.html", locals())
    