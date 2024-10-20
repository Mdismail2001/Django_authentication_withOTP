from django.urls import path
from . import views 
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/',views.register, name='register'),
    path('login/',views.login_view, name='login'),
    path('home/', views.home_view, name='home'),
    path('logout/',views.logout_view, name='logout'),
    path('otp_view/', views.otp_view, name='otp_view'),
    path('profile_update/', views.profile_update, name='profile_update'),
    path('table_list/', views.tabile_list, name='table_list'),
    path('typography/', views.typography_views, name='typography'),
    path('icon', views.icon_views, name='icon'),
    path('map/', views.maps_views,name='map'),
    path('notifications', views.notifications_views, name='notifications'),
    path('rtl_support/', views.rtl_support_views, name='rtl_support'),
    
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name= 'registration/password_reset_form.html'), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name= 'registration/password_reset_done.html'), name='password_reset_done'),
    path('password_reset_confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='registration/password_reset_confirm.html') , name='password_reset_confirm'),
    path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(template_name= 'registration/password_reset_complete.html'), name='password_reset_complete'),


]
