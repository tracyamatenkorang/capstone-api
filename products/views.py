from rest_framework import generics, permissions, filters
from .models import Product, Category, Review, Wishlist
from .serializers import ProductSerializer, CategorySerializer, ReviewSerializer, WishlistSerializer
from rest_framework import filters
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend

# List and Create Products
# class ProductCreate(generics.CreateAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
#     #permission_classes = [IsAuthenticatedOrReadOnly]

# class ProductList(generics.ListAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
#     permission_classes = [IsAuthenticatedOrReadOnly]
#     filter_backends = [DjangoFilterBackend, filters.SearchFilter]
#     filterset_fields = {
#         'price': ['gte', 'lte'],
#         'category': ['exact'],
#         'stock_quantity': ['exact'],
#     }
#     search_fields = ['name', 'category__name']

# class ProductDetail(generics.RetrieveAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
#     permission_classes = [IsAuthenticatedOrReadOnly]

# class ProductUpdate(generics.UpdateAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
#     permission_classes = [IsAuthenticatedOrReadOnly]

# class ProductDelete(generics.DestroyAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
#     permission_classes = [IsAuthenticatedOrReadOnly]



class ProductListCreate(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    search_fields = ['name', 'category__name']
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = {
        'price': ['gte', 'lte'],
        'category': ['exact'],  # Filter products by price range (greater than or less than)
        'stock_quantity': ['exact'],  # Filter by products in stock
    }



# # Retrieve, Update, and Delete a Product
class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

# List and Create Categories
class CategoryListCreate(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

# Retrieve, Update, and Delete a Category
class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ReviewListCreate(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        # Set the user automatically to the logged-in user
        serializer.save(user=self.request.user)

class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        # Restrict users to only update/delete their own reviews
        return self.queryset.filter(user=self.request.user)
    


class WishlistListCreate(generics.ListCreateAPIView):
    queryset = Wishlist.objects.all()
    serializer_class = WishlistSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        # Set the user automatically to the logged-in user
        serializer.save(user=self.request.user)

class WishlistDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Wishlist.objects.all()
    serializer_class = WishlistSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Restrict users to only update/delete their own wishlists
        return self.queryset.filter(user=self.request.user)
