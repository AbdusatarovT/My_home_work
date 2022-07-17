from django.urls import path

from product.views import *

urlpatterns = [
    path('category/', CategoryListCreateView.as_view()),
    path('category/<int:pk>/', CategoryRetrieveUpdateDestroyView.as_view()),
    path('product/', ProductListCreateView.as_view()),
    path('product/<int:pk>/', CategoryRetrieveUpdateDestroyView.as_view()),

]