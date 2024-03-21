from django.urls import path
from .views import HomePageView, AboutPageView
from .views import PostPageView, PostDetailView, MyLoginView
from .views import MyLogoutView, ImageRequestView
from .views import ClientRegistrationView, TailorRegistrationView


urlpatterns = [
        path('client', ClientRegistrationView.as_view(), name='client'),
        path('tailor', TailorRegistrationView.as_view(), name='tailor'),
        path('image_request/', ImageRequestView.as_view(), name='image_request'),
        path('accounts/logout/', MyLogoutView.as_view(), name='logout'),
        path('accounts/login/', MyLoginView.as_view(), name='login'),
        path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
        path('post/', PostPageView.as_view(), name='post'),
        path('about/', AboutPageView.as_view(), name='about'), # new
        path('', HomePageView.as_view(), name='home'),
]
