from django.shortcuts import render, redirect
from .models import MiniUrl
from .forms import MiniUrlForm

def home(request):
    mini_urls = MiniUrl.objects.all()
    return render(request, 'm/home.html.twig', locals())

def add_url(request):
    form = MiniUrlForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('home')
    return render(request, 'm/url_add_form.html.twig', locals())

# Create your views here.
