
from django.urls import path, include
from . import views

urlpatterns =[
    path('', views.home_view, name='home'),
    path('<str:shortened_part>', views.redirect_url_view, name='redirect')
]