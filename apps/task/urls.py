from django.urls import path 

from .views import *

urlpatterns = [
    path('', TaskAPIView.as_view(), name='api_task '),
    path('create/', TaskAPICreate.as_view(), name='api_task_create '),
    path('<int:pk>/', TaskAPIRetrieve.as_view(), name='api_task_retrieve '),
    path('update/<int:pk>/', TaskAPIUpdate.as_view(), name='api_task_update '),
    path('delete/<int:pk>/', TaskAPIDestroy.as_view(), name='api_task_delete '),



]