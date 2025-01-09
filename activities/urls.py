# activities/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ActivityViewSet
from django.urls import path
from . import views
from activities.views import ActivityDetailView

router = DefaultRouter()
router.register(r'activities', ActivityViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('activities/', views.ActivityListCreateView.as_view(), name='activity-list'),
    path('activities/<int:pk>/', views.ActivityDetailView.as_view(), name='activity-detail'),
    path('activities/<int:pk>/', ActivityDetailView.as_view(), name='activity-detail'),
]