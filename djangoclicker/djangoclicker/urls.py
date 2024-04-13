from django.contrib import admin
from django.urls import path, include
# from . import views

# urlpatterns = [
#     # path('admin/', admin.site.urls),
#     path('','views.index, name='index')',
#     path('login/', views.user_login, name='login'),
#     path('logout/', views.user_logout()),
#     path('registartion/', views.user_registration(), name='registartion'),
#     path('user/<int:pk>/', views.UserDetail.as_view())
#
# ]

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', include('auth_clicker.views.index')),
    path('login/', include('auth_clicker.views.user_login')),
    path('logout/', include('auth_clicker.views.user_logout()')),
    path('registartion/', include('auth_clicker.views.user_registration()')),
    path('user/<int:pk>/', include('auth_clicker.views.UserDetail.as_view()')),


]
