from django.urls import path
from product import views
from .views import*

urlpatterns=[

# post method
        path('add-productMain/', addproductMain.as_view()),
        path('add-productImage/', addproductImage.as_view()),

# get method
    path('Get-productMain/', views.GetproductMain.as_view()),
    path('Get-productImage/', views.GetproductImage.as_view()),


# updated method
    path('Put-productMain/<int:pk>', views.PutproductMain.as_view()),
    path('Put-productImage/<int:pk>', views.PutproductImage.as_view()),

    # delete method
    path('Delete-productMain/', DeleteproductMain.as_view()),
    path('Delete-productImage/', DeleteproductImage.as_view()),
]