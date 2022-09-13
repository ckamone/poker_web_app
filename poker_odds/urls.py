from django.urls import path
from . import views

from pywebio.platform.django import webio_view
from pywebio.input import input, FLOAT
from pywebio.output import *
from .pot_odds import odds
from .poker_outs import outs

# `task_func` is PyWebIO task function
webio_view_func1 = webio_view(odds, cdn=True)
webio_view_func2 = webio_view(outs, cdn=True)

urlpatterns = [
    path(r"tool1", webio_view_func1),
    path(r"tool2", webio_view_func2),
]
