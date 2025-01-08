# activities/admin.py
from django.contrib import admin
from .models import Activity

@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    list_display = ('activity_type', 'duration', 'distance', 'calories_burned', 'date', 'user')  # Display these fields in the list
    list_filter = ('activity_type', 'date')  # Add filters by activity type and date
    search_fields = ('activity_type', 'user__username')  # Enable search by activity type and username
    ordering = ('-date',)  # Default ordering by date (most recent first)
