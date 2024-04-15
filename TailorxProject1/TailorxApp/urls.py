from django.urls import path
from .views import HomePageView, AboutPageView
from .views import PostPageView, PostDetailView, MyLoginView
from .views import portfolio  #MyLogoutView,
from .views import ClientRegistrationView, TailorRegistrationView
from .views import PasswordResetView, TailorSearchView
from .views import PasswordResetConfirmView,  PictureView
from .views import MessageListView, post_login_view, register_tailor, register_client
from .views import TailorPortalView, logout_user, profile, picture
from django.views.generic import TemplateView


urlpatterns = [
        path('picture', picture, name='picture_tailor'),
        path('tailor-portal/', TailorPortalView.as_view(), name='tailor-portal'),
        path('tailors/search/', TailorSearchView.as_view(), name='tailor-search'),
        path('tailors/<int:tailor_id>/portfolio/', PictureView.as_view(), name='picture'),
        path('messages/', MessageListView.as_view(), name='messages'),
        path('password-reset-confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
        path('password-reset/', PasswordResetView.as_view(), name='password-reset'),
        path('client/', ClientRegistrationView.as_view(), name='client'),
        path('tailor/', TailorRegistrationView.as_view(), name='tailor'),
        path('register_tailor/', register_tailor, name='register_tailor'),
        path('register_client/', register_client, name='register_client'),
        path('profile', profile, name='profile'),
        #path('image_request/', ImageRequestView.as_view(), name='image_request'),
        path('portfolio', portfolio, name='portfolio'),
        path('logout/', logout_user, name='logout'),
        path('login/', MyLoginView.as_view(), name='login'),
        path('post-login/', post_login_view, name='post-login'),
        path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
        path('post/', PostPageView.as_view(), name='post'),
        path('about/', AboutPageView.as_view(), name='about'), # new
        path('home/', HomePageView.as_view(), name='home'),
        path('', TemplateView.as_view(template_name='landingpage.html'), name='landingpage'),
]
