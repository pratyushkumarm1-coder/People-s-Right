from django import forms
from .models import Complaint

class ComplaintForm(forms.ModelForm):
    class Meta:
        model = Complaint
        fields = ['title', 'description', 'category', 'location_address', 'latitude', 'longitude', 'status', 'urgency', 'image', 'reporter_name']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Complaint title (e.g. Broken streetlight)'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Provide details...', 'rows': 4}),
            'category': forms.Select(attrs={'class': 'form-select'}),
            'location_address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nearby address or landmark'}),
            'latitude': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Latitude (optional)', 'step': 'any'}),
            'longitude': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Longitude (optional)', 'step': 'any'}),
            'status': forms.Select(attrs={'class': 'form-select'}),
            'urgency': forms.Select(attrs={'class': 'form-select'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
            'reporter_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Name (Optional)'}),
        }
