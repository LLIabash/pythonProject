from django.urls import path
from .views import UserListCreateView, UserDetailView

urlpatterns = [
    path('users/', UserListCreateView.as_view(), name='user-list-create'),
    path('users/<uuid:id>/', UserDetailView.as_view(), name='user-detail'),
]