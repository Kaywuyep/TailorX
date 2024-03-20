#from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from .models import Post
# Create your views here.

class HomePageView(TemplateView):
    template_name = 'homepage.html'


class AboutPageView(TemplateView):
    template_name = 'aboutpage.html'


class PostPageView(ListView):
    model = Post
    template_name = 'post.html'
