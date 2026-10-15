from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)
    icon = models.CharField(max_length=50, help_text="Bootstrap icon class (e.g., bi-exclamation-triangle)")

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Categories"

class Notification(models.Model):
    message = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)
    
    def __str__(self):
        return self.message
    
    class Meta:
        ordering = ['-created_at']

class Complaint(models.Model):
    STATUS_CHOICES = [
        ('open', 'Open'),
        ('investigating', 'Investigating'),
        ('in_progress', 'Work Going On'),
        ('resolved', 'Resolved'),
        ('closed', 'Closed'),
    ]
    
    URGENCY_CHOICES = [
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='complaints')
    location_address = models.CharField(max_length=255)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='open')
    urgency = models.CharField(max_length=10, choices=URGENCY_CHOICES, default='medium')
    image = models.ImageField(upload_to='complaints/', null=True, blank=True)
    reporter_name = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if self.pk:
            old_complaint = Complaint.objects.get(pk=self.pk)
            # If status changed to resolved, create a notification
            if old_complaint.status != 'resolved' and self.status == 'resolved':
                Notification.objects.create(
                    message=f"Work completed! The complaint '{self.title}' has been resolved."
                )
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

