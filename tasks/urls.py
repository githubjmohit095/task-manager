from django.urls import path
from .views import (TaskListCreateView, TaskRetrieveUpdateDestroyView, 
                    RateLimitedTaskView, UserCreateView, UserListView,
                    CustomLoginView, CustomLogoutView)

urlpatterns = [
    path('tasks/', TaskListCreateView.as_view(), name='task-list-create'),
    path('tasks/<int:pk>/', TaskRetrieveUpdateDestroyView.as_view(), name='task-detail'),
    path('tasks/rate-limited/', RateLimitedTaskView.as_view(), name='rate-limited-task'),
    path('users/register/', UserCreateView.as_view(), name='user-register'),
    path('users/', UserListView.as_view(), name='user-list'),
    path("users/login/", CustomLoginView.as_view(), name="custom-login"),
    path("users/logout/", CustomLogoutView.as_view(), name="custom-logout"),
]
