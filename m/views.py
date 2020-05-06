from django.shortcuts import render, redirect, get_object_or_404
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

def redirect_by_code(request, code):
    mini_url = get_object_or_404(MiniUrl, code=code)
    mini_url.nb_access += 1
    mini_url.save()
    return redirect(mini_url.url)


# Create your views here.
