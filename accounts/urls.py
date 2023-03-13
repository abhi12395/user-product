from django.urls import path
from accounts import views
from .views import*

urlpatterns = [

    #post method

    path('adduser/', addUser.as_view()),
    path('addUserProfile/', addUserProfile.as_view()),
    path('addlogin_top/', addlogin_top.as_view()),
    path('addUserCartProduct/', addUserCartProduct.as_view()),
    path('addUserCart/', addUserCart.as_view()),

# get method
    path('get-GetUser/', views.GetUser.as_view()),
    path('get-GetUserProfile/', views.GetUserProfile.as_view()),
    path('get-Getlogintop/', views.Getlogintop.as_view()),
    path('get-GetUserCartProduct/', views.GetUserCartProduct.as_view()),
    path('get-GetUserCart/', views.GetUserCart.as_view()),

# updated method
    path('Put-User/<int:pk>', views.PutUser.as_view()),
    path('Put-PutUserProfile/<int:pk>', views.PutUserProfile.as_view()),
    path('Put-logintop/<int:pk>', views.Putlogintop.as_view()),
    path('Put-UserCartProduct/<int:pk>', views.PutUserCartProduct.as_view()),
    path('Put-UserCart/<int:pk>', views.PutUserCart.as_view()),


    # delete method
    path('Delete-User/', DeleteUser.as_view()),
    path('Delete-UserProfile/', DeleteUserProfile.as_view()),
    path('Delete-logintop/', Deletelogintop.as_view()),
    path('Delete-UserCartProduct/', DeleteUserCartProduct.as_view()),
    path('Delete-UserCart/', DeleteUserCart.as_view()),



]