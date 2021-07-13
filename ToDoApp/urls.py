from django.urls import path
from .views import (TaskList,
                    TaskDetail,
                    TaskCreate,
                    TaskUpdate,
                    TaskDelete,
                    CustomLoginView,
                    CustomLogoutView,
                    RegisterPage,
                    HomeView,
                    AboutView)

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='CustomLoginView'),
    path('logout/', CustomLogoutView.as_view(), name='CustomLogoutView'),
    path('register/', RegisterPage.as_view(), name='RegisterPage'),
    path('', HomeView.as_view(), name='HomeView'),
    path('about/', AboutView.as_view(), name='AboutView'),
    path('list/', TaskList.as_view(), name='TaskList'),
    path('task/<int:pk>/', TaskDetail.as_view(), name='TaskDetail'),
    path('create/', TaskCreate.as_view(), name='TaskCreate'),
    path('update/<int:pk>/', TaskUpdate.as_view(), name='TaskUpdate'),
    path('delete/<int:pk>/', TaskDelete.as_view(), name='TaskDelete'),
]