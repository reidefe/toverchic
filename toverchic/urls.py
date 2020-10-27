

from django.urls import path
from django.contrib.auth import views as auth_views
from .views import Productdetail,Products,signup, createProduct, userDetails

urlpatterns = [
    path('', Products.as_view(), name='home'),
    path('product/<int:pk>', Productdetail.as_view(), name='product-detail'),
    path('user/<int:pk>', userDetails.as_view(), name='user-detail'),
    path('create-product/', createProduct.as_view(), name='create-product'),
    path('login/',auth_views.LoginView.as_view(template_name='login.html'),name='login'),
    path('logout/', auth_views.LogoutView.as_view(),name='logout'),
    path('signup/', signup,name='signup')
]
