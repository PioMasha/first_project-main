from django.urls import path
from .views import LoginView, LougoutView, CreateAccountView

app_name = 'login'

urlpatterns = [
    path('', LoginView.as_view(), name='login'),
    path('logout/', LougoutView.as_view(), name='logout'),
    path('create/', CreateAccountView.as_view(), name='create'),
]