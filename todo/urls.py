from django.urls import path

from todo.views import (
    TaskCreate,
    TaskDelete,
    TaskDetail,
    TaskList,
    TaskUpdate,
)


urlpatterns = [
    path("list/", TaskList.as_view(), name="task-list"),
    path("task/<int:pk>/", TaskDetail.as_view(), name="task-detail"),
    path("create/", TaskCreate.as_view(), name="task-create"),
    path("update/<int:pk>/", TaskUpdate.as_view(), name="task-update"),
    path("delete/<int:pk>/", TaskDelete.as_view(), name="task-delete"),
]
