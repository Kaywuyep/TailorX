from django.urls import path
from .views import HomePageView, AboutPageView
from .views import PostPageView


urlpatterns = [
        path('post/', PostPageView.as_view(), name='post'),
        path('about/', AboutPageView.as_view(), name='about'), # new
        path('', HomePageView.as_view(), name='home'),
]
