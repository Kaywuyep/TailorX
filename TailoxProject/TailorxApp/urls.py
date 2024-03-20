from django.urls import path
from .views import HomePageView, AboutPageView
from .views import PostPageView, PostDetailView


urlpatterns = [
        path ('post/<ink:pk>/', PostDetailView.as_view(), name='post_detail'),
        path('post/', PostPageView.as_view(), name='post'),
        path('about/', AboutPageView.as_view(), name='about'), # new
        path('', HomePageView.as_view(), name='home'),
]
