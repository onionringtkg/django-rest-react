from django.urls import path
from django.conf.urls import include
from rest_framework import routers
from api.views import TaskViewsSet, UserViewsSet, ManageUserView

router = routers.DefaultRouter()
router.register('tasks', TaskViewsSet)
router.register('users', UserViewsSet)

urlpatterns = [
    path('myself/', ManageUserView.as_view(), name='myself'),
    path('', include(router.urls))    
]

