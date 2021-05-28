from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = 'pages/home.html'


class AboutPageView(TemplateView):
    template_name = 'pages/about.html'


class GamePageView(TemplateView):
    template_name = 'pages/games.html'


class RpsGameView(TemplateView):
    template_name = 'pages/rps.html'


class TimerView(TemplateView):
    template_name = 'pages/timer.html'


class ColorsView(TemplateView):
    template_name = 'pages/colorsflipper.html'


class ColorsHexView(TemplateView):
    template_name = 'pages/colorsflipper_hex.html'


class TestYRView(TemplateView):
    template_name = 'pages/testyourreaction.html'