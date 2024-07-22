from django.urls import path

from .views import (
    SignInPage,
    SignOutPage,
    SignUpPage,
)

urlpatterns = [
    path("sign-in/", SignInPage.as_view(), name="sign-in"),
    path("sign-out/", SignOutPage.as_view(), name="sign-out"),
    path("sign-up/", SignUpPage.as_view(), name="sign-up"),
]
