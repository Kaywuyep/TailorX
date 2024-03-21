from django.urls import path
from .views import HomePageView, AboutPageView
from .views import PostPageView, PostDetailView, MyLoginView
from .views import MyLogoutView, ImageRequestView
from .views import ClientRegistrationView, TailorRegistrationView
from .views import PasswordResetView
from .views import PasswordResetConfirmView


urlpatterns = [
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
        path('', HomePageView.as_view(), name='home'),
]
