from django.urls import path
from . import views
from . import views

urlpatterns = [
    path('', views.home),
    path('signup', views.sign_up, name='sign_up'),
    path('signin', views.sign_in, name='sign_in'),
    path('codevalidation', views.code_validation, name='code_validation'),
    path('forgotpassword', views.forgot_password_form, name='forgot_password_form'),
    path('updatepassowrd', views.update_password, name='update_password'),
    path('signout', views.sign_out, name="sign_out")
]