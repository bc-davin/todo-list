from django.urls import path
from . import views

urlpatterns = [
    path("homePage/", views.homePage, name="tasks_home"),  # Ensure this path is correct
    path("list_tasks/", views.TaskListCreateView.as_view(), name="tasks_list_tasks"),  # Ensure this path is correct
    path("get_task/<int:pk>/", views.TaskRetrieveUpdateDestroyView.as_view(), name="tasks_get_task"),  # Ensure this path is correct
    path("update_task/<int:pk>/", views.TaskRetrieveUpdateDestroyView.as_view(), name="tasks_update_task"),  # Ensure this path is correct
    path("delete_task/<int:pk>/", views.TaskRetrieveUpdateDestroyView.as_view(), name="tasks_delete_task"),  # Ensure this path is correct
]
