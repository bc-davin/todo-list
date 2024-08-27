from django.urls import path
from . import views

urlpatterns = [
    path("signup/", views.SignUpView.as_view(), name="accounts_signup"),  # Ensure this path is correct
]