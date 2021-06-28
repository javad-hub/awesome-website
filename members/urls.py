from django.urls import path
from .views import RegistrationView

urlpatterns = [
	path('registeration/', RegistrationView.as_view(), name="register"),
]