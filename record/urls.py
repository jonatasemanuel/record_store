from django.urls import path
from . import views


urlpatterns = [
    path('', views.albums, name='album'),
    path('find/', views.find, name='find'),
    path('<int:credits_id>', views.credits, name='credits')
]