from django.urls import path
from .views import ManageHome, ClassLogin, AddKey, ViewAPIKey

app_name = 'homepage'
urlpatterns = [
    path('', ManageHome.as_view(), name='managehome'),
    path('login/', ClassLogin.as_view(), name='login'),
    path('addkey/', AddKey.as_view(), name='addkey'),
    path('api-key/', ViewAPIKey.as_view())
]