from django.urls import path
from . import views

urlpatterns = [
    path('', views.PhotoListView.as_view(), name='photo_list'),
    path('upload/', views.PhotoCreateView.as_view(), name='photo_upload'),
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('photo/<int:pk>/', views.PhotoDetailView.as_view(), name='photo_detail'),
]