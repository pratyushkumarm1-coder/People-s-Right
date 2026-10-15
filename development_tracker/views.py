from django.shortcuts import render, get_object_or_404, redirect
from .models import Complaint, Category
from .forms import ComplaintForm
import json

def home(request):
    complaints = Complaint.objects.all().order_by('-created_at')
    categories = Category.objects.all()
    
    # Prepare map data
    map_data = []
    for c in complaints:
        if c.latitude and c.longitude:
            map_data.append({
                'id': c.id,
                'title': c.title,
                'lat': c.latitude,
                'lng': c.longitude,
                'status': c.get_status_display(),
                'urgency': c.get_urgency_display()
            })
    
    # Stats for Status Panel
    stats = {
        'total': complaints.count(),
        'open': complaints.filter(status='open').count(),
        'investigating': complaints.filter(status='investigating').count(),
        'in_progress': complaints.filter(status='in_progress').count(),
        'resolved': complaints.filter(status='resolved').count(),
    }
    
    return render(request, 'home.html', {
        'complaints': complaints, 
        'categories': categories,
        'map_data_json': json.dumps(map_data),
        'stats': stats
    })

def complaint_detail(request, pk):
    complaint = get_object_or_404(Complaint, pk=pk)
    return render(request, 'complaint_detail.html', {'complaint': complaint})

def add_complaint(request):
    if request.method == "POST":
        form = ComplaintForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ComplaintForm()
    return render(request, 'add_complaint.html', {'form': form})
