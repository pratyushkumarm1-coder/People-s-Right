from .models import Notification

def notifications(request):
    return {
        'recent_notifications': Notification.objects.filter(is_read=False).order_by('-created_at')[:5],
        'unread_notifications_count': Notification.objects.filter(is_read=False).count()
    }
