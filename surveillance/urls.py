from django.urls import path

from .components.UI_CORE.ui_core_test import current_datetime as view
urlpatterns = [
    path('', view, name='index'),
]
