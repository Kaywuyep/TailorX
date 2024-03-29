#from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from django.views.generic import DetailView
from django.views import View
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login
from .models import Post, Picture, Message, Tailor
from .forms import UserImage
from django.contrib.auth.views import LoginView
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import ClientRegistrationForm, TailorRegistrationForm
from django.contrib.auth.views import LogoutView
from django.contrib.auth.views import (
    PasswordResetView as DjangoPasswordResetView,
    PasswordResetConfirmView as DjangoPasswordResetConfirmView,
)
from rest_framework import generics
from rest_framework import filters
from .serializers import TailorSerializer, PictureSerializer, MessageSerializer
# Create your views here.


class HomePageView(TemplateView):
    template_name = 'homepage.html'


class AboutPageView(TemplateView):
    template_name = 'aboutpage.html'


class PostPageView(ListView):
    model = Post
    template_name = 'post.html'

class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'


class MyLoginView(LoginView):
    template_name = 'registration/login.html'

    # redirect_authenticated_user = True

    def login(request):
        if request.method == 'POST':
            form = AuthenticationForm(request, request.POST)
            if form.is_valid():
                # Log the user in
                user = form.get_user()
                auth_login(request, user)
                # Redirect to the tailor portal page
                return redirect('tailor_portal')  # Assuming 'tailor_portal' is the name of the URL pattern for the tailor portal page
        else:
            form = AuthenticationForm()
        return render(request, 'login.html', {'form': form})


class MyLogoutView(LogoutView):
    template_name = 'registration/logout.html'

    def dispatch(self, request, *args, **kwargs):
         response = super().dispatch(request, *args, **kwargs)
         return redirect('home')


class PasswordResetView(DjangoPasswordResetView):
    template_name = 'password_reset.html'


class PasswordResetConfirmView(DjangoPasswordResetConfirmView):
    template_name = 'password_reset_confirm.html'


class ImageRequestView(View):
    def get(self, request):
        form = UserImage()
        return render(request, 'picture-form.html', {'form': form})

    def post(self, request):
        form = UserImage(request.POST, request.FILES)
        if form.is_valid():
            form.save()

            # Getting the current instance object to display in the template
            img_object = form.instance

            return render(request, 'picture-form.html', {'form': form, 'img_obj': img_object})
        return render(request, 'picture-form.html', {'form': form})


class PictureView(generics.ListAPIView):
    serializer_class = PictureSerializer

    def get_queryset(self):
        tailor_id = self.kwargs['tailor_id']
        return Tailor.objects.get(pk=tailor_id).tailor_pictures.all()


class MessageListView(generics.ListCreateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer


class ClientRegistrationView(View):
    def get(self, request):
        form = ClientRegistrationForm()
        return render(request, 'client_registration.html', {'form': form})

    def post(self, request):
        form = ClientRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username') # Get the username that is submitted
            messages.success(request, f'Account created for {username}!') # Show sucess message when account is created
            return redirect('home')  # Redirect to a success page
        return render(request, 'client_registration.html', {'form': form})


class TailorRegistrationView(View):
    def get(self, request):
        form = TailorRegistrationForm()
        return render(request, 'tailor_registration.html', {'form': form})

    def post(self, request):
        form = TailorRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username') # Get the username that is submitted
            messages.success(request, f'Account created for {username}!') # Show sucess message when account is created
            return redirect('home')  # Redirect to a success page
        return render(request, 'tailor_registration.html', {'form': form})


class TailorSearchView(generics.ListAPIView):
    queryset = Tailor.objects.all()
    serializer_class = TailorSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['location']
