from django.urls import path

from account.views import *

urlpatterns = [
    path('register/', RegisterApiView.as_view()),
    path('active/<uuid:activation_code>/', ActivationView.as_view()),
    path('login/', loginApiView.as_view()),
    path('change_password/', ChangePasswordView.as_view()),
    ]