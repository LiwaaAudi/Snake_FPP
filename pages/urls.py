from django.urls import path

from .views import HomePageView, AboutPageView, GamePageView, RpsGameView, TimerView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('games/', GamePageView.as_view(), name='games'),
    path('games/rps', RpsGameView.as_view(), name='rps'),
    path('games/timer', TimerView.as_view(), name='timer'),
]
