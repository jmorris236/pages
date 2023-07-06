from django.urls import path
from .views import HomePageView, MathPageView, SciencePageView, CodingPageView

urlpatterns = [
    path('coding/', CodingPageView.as_view(), name='coding'),
    path('science/', SciencePageView.as_view(), name='science'),
    path('math/', MathPageView.as_view(), name='math'),
    path('', HomePageView.as_view(), name='home'),
]