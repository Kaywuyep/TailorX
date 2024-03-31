from django.urls import path
from .views import HomePageView, AboutPageView
from .views import PostPageView, PostDetailView, MyLoginView
from .views import MyLogoutView, ImageRequestView
from .views import ClientRegistrationView, TailorRegistrationView
from .views import PasswordResetView, TailorSearchView
from .views import PasswordResetConfirmView,  PictureView
from .views import MessageListView
from django.views.generic import TemplateView


urlpatterns = [
        path('tailor-portal/', TemplateView.as_view(template_name='tailor-portal.html'), name='tailor_portal'),
        path('tailors/search/', TailorSearchView.as_view(), name='tailor-search'),
        path('tailors/<int:tailor_id>/portfolio/', PictureView.as_view(), name='picture'),
        path('messages/', MessageListView.as_view(), name='messages'),
        path('password-reset-confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
        path('password-reset/', PasswordResetView.as_view(), name='password-reset'),
        path('client/', ClientRegistrationView.as_view(), name='client'),
        path('tailor/', TailorRegistrationView.as_view(), name='tailor'),
        path('image_request/', ImageRequestView.as_view(), name='image_request'),
        path('logout/', MyLogoutView.as_view(), name='logout'),
        path('login/', MyLoginView.as_view(), name='login'),
        path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
        path('post/', PostPageView.as_view(), name='post'),
        path('about/', AboutPageView.as_view(), name='about'), # new
        path('home', HomePageView.as_view(), name='home'),
        path('', TemplateView.as_view(template_name='landingpage.html'), name='landingpage'),
]
