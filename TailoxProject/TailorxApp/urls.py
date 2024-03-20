from django.urls import path
from .views import HomePageView, AboutPageView
from .views import PostPageView, PostDetailView, LoginView


urlpatterns = [
        path('accounts/login/', LoginView.as_view(), name='login'),
        path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
        path('post/', PostPageView.as_view(), name='post'),
        path('about/', AboutPageView.as_view(), name='about'), # new
        path('', HomePageView.as_view(), name='home'),
]
