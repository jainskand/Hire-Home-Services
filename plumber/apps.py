from django.apps import AppConfig


class PlumberConfig(AppConfig):
    name = 'plumber'

    def ready(self):
    	import plumber.signals
