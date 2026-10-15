from django.contrib import admin
from .models import Category, Complaint, Notification

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'icon')

@admin.register(Complaint)
class ComplaintAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'status', 'urgency', 'reporter_name', 'created_at')
    list_filter = ('status', 'urgency', 'category')
    search_fields = ('title', 'description', 'location_address', 'reporter_name')
    readonly_fields = ('created_at', 'updated_at')

@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ('message', 'is_read', 'created_at')
    list_filter = ('is_read',)
