from django.urls import path

from .views import *
from django.contrib.auth.urls import *

urlpatterns = [
    path('', index, name="home"),
    path('login/', user_login, name='login'),
    path('logout/', logout_view, name='logoutm'),
    path('addECP/', addECP, name='addECP'),
    path('superimpose/', superimpose, name='superimpose'),
]
