from django.urls import path
from .views import groups_page, users_page

urlpatterns = [
    path('', groups_page, name='groups_page'),
    path('users_page/', users_page, name='users_page')   
]