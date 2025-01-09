# activities/views.py
from rest_framework import viewsets, permissions
from .models import Activity
from .serializers import ActivitySerializer

class ActivityViewSet(viewsets.ModelViewSet):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        # Set the user to the logged-in user
        serializer.save(user=self.request.user)

    def get_queryset(self):
        # Filter activities by the logged-in user
        return Activity.objects.filter(user=self.request.user)

from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to the Fitness Tracker API!")


from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from .models import Activity
from .serializers import ActivitySerializer

class ActivityListCreateView(ListCreateAPIView):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)

class ActivityDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)

