from django.urls import path

from .views import HomePageView, AboutPageView, GamePageView, RpsGameView, TimerView, ColorsView, ColorsHexView, TestYRView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('games/', GamePageView.as_view(), name='games'),
    path('games/rps', RpsGameView.as_view(), name='rps'),
    path('games/timer', TimerView.as_view(), name='timer'),
    path('games/colors', ColorsView.as_view(), name='colors'),
    path('games/colorshex', ColorsHexView.as_view(), name='colorshex'),
    path('games/test_your_reaction', TestYRView.as_view(), name='test_your_reaction'),
]
