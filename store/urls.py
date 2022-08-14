from . import views
from django.urls import path
from .views import RegisterForm

urlpatterns= [

    path('register/',RegisterForm.as_view(),name='register'),
    path('login_user/',views.login_user,name='login_user'),
    path('logout_user/',views.logout_user,name='logout_user'),
    path('category/<int:id>/<slug:slug>',views.category_products,name='category_products'),
    path('categories/',views.categories,name='categories'),
    path('', views.store,name='store'),
    path('details/<int:id>', views.details,name='details'),
    path('order_product/', views.order_product,name='order_product'),
    path('cart/', views.cart,name='cart'),
    path('addtocart/<int:id>', views.cart,name='cart'),
    path('profile/<int:id>', views.profile,name='profile'),

    

]