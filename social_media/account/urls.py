from django.urls import path,include
from . import views

app_name='account'
urlpatterns = [

      path('login/',views.user_login, name="user_login"),
      path('logout/',views.user_logout, name="user_logout"),
      path('register/',views.user_registration, name="user_register"),
      path('dashboard/<int:user_id>/' , views.user_dashboard, name='dashboard'),
      path('edit_profile/<int:user_id>',views.edit_profile, name='edit_profile'),
      path('phone_login', views.phone_login,name="phone_login"),
      path('verify/<str:phone>/<int:rand_num>/', views.verify, name='verify'),
      path('follow', views.follow, name='follow'),
      path('unfollow', views.unfollow, name='unfollow'),
]
