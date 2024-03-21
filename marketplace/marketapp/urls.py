from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView
urlpatterns = [
    path("",views.IndexView,name="index"),
    path("base/",views.BaseView.as_view(),name="base"),
    path('logout/',LogoutView.as_view(next_page='index'),name='logout'),
    path("register/",views.UserRegisterView.as_view(),name="register"),
    path("login/", views.LoginView.as_view(), name="login"),
    path("logout_confirm/",views.UserLogoutConfirm,name="logout_confirm"),
]
