from django.urls import path
from .views import HomePageView, AboutPageView
from .views import PostPageView, PostDetailView, MyLoginView
from django.contrib.auth.views import LogoutView


urlpatterns = [
        path('accounts/logout/', MyLogoutView.as_view(next_page='login'), name='logout'),
        path('accounts/login/', MyLoginView.as_view(), name='login'),
        path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
        path('post/', PostPageView.as_view(), name='post'),
        path('about/', AboutPageView.as_view(), name='about'), # new
        path('', HomePageView.as_view(), name='home'),
]
