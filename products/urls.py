from django.urls import path
from . import views

urlpatterns = [
    #path('products/create/', views.ProductCreate.as_view(), name='product-create'),
    path('products/', views.ProductListCreate.as_view(), name='product-list-create'),
    path('products/<int:pk>/', views.ProductDetail.as_view(), name='product-detail'),
    #path('products/<int:pk>/update/', views.ProductUpdate.as_view(), name='product-update'),
    #path('products/<int:pk>/delete/', views.ProductDelete.as_view(), name='product-delete'),

    path('categories/', views.CategoryListCreate.as_view(), name='category-list-create'),
    path('categories/<int:pk>/', views.CategoryDetail.as_view(), name='category-detail'),

    path('reviews/', views.ReviewListCreate.as_view(), name='review-list-create'),
    path('reviews/<int:pk>/', views.ReviewDetail.as_view(), name='review-detail'),
    path('wishlists/', views.WishlistListCreate.as_view(), name='wishlist-list-create'),
    path('wishlists/<int:pk>/', views.WishlistDetail.as_view(), name='wishlist-detail'),
]