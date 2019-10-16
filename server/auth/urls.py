from django.contrib.auth import views as auth_views
from django.urls import path
from django.views.generic import TemplateView

from .views import SignUp

urlpatterns = [
    path('', auth_views.LoginView.as_view(
        template_name='auth/signin.html'), name='signin' 
    ),
    path('registro', SignUp.as_view(
        template_name='auth/signup.html'), name='signup' 
    ),
    path('salir', auth_views.LogoutView.as_view(), name='signout' ),

    path('password_change', auth_views.PasswordChangeView.as_view(
        template_name='auth/password_change.html'), name='password_change'
    ),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(
        template_name='auth/password_change_done.html'), name='password_change_done'
    ),
    path('password_reset/', auth_views.PasswordResetView.as_view(
        template_name='auth/password_reset_form.html'), name='password_reset' 
    ),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(
        template_name='auth/password_reset_done.html'), name='password_reset_done'
    ),
    path('password_reset/confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name='auth/password_reset_confirm.html'), name='password_reset_confirm'
    ),
    path('password_reset/complete/', auth_views.PasswordResetCompleteView.as_view(
        template_name='auth/password_reset_complete.html'), name='password_reset_complete'
    ),
]