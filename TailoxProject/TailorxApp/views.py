#from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from django.views.generic import DetailView
from django.views import View
from django.shortcuts import render, redirect
from .models import Post
from django.contrib.auth.views import LoginView
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import ClientRegistrationForm, TailorRegistrationForm
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
    # template_name = 'login.html'


    def form_invalid(self, form):
        messages.error(self.request,'Invalid username or password')
        return self.render_to_response(self.get_context_data(form=form))





class ClientRegistrationView(View):
    def get(self, request):
        form = ClientRegistrationForm()
        return render(request, 'client_registration.html', {'form': form})

    def post(self, request):
        form = ClientRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('registration_success')  # Redirect to a success page
        return render(request, 'client_registration.html', {'form': form})


class TailorRegistrationView(View):
    def get(self, request):
        form = TailorRegistrationForm()
        return render(request, 'tailor_registration.html', {'form': form})

    def post(self, request):
        form = TailorRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('registration_success')  # Redirect to a success page
        return render(request, 'tailor_registration.html', {'form': form})
