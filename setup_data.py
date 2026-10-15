from development_tracker.models import Category, Complaint
from django.contrib.auth.models import User

# Create superuser
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'admin@example.com', 'admin123')

# Create categories
categories = [
    {'name': 'Infrastructure', 'icon': 'bi-cone-striped'},
    {'name': 'Public Safety', 'icon': 'bi-shield-shaded'},
    {'name': 'Sanitation', 'icon': 'bi-trash3'},
    {'name': 'Environment', 'icon': 'bi-tree'},
    {'name': 'Utilities', 'icon': 'bi-lightning-charge'},
]

for cat_data in categories:
    cat, created = Category.objects.get_or_create(name=cat_data['name'], defaults={'icon': cat_data['icon']})

# Sample Complaints in Odisha
sample_complaints = [
    {
        'title': 'Potholes on Janpath Road',
        'description': 'Several deep potholes have formed on Janpath near Master Canteen, causing traffic hazards.',
        'category_name': 'Infrastructure',
        'location': 'Master Canteen, Bhubaneswar',
        'lat': 20.2721,
        'lng': 85.8438,
        'urgency': 'high'
    },
    {
        'title': 'Garbage Piles near Puri Ghat',
        'description': 'Unauthorized waste dumping is occurring near the riverside area, creating foul smell.',
        'category_name': 'Sanitation',
        'location': 'Puri Ghat Area, Cuttack',
        'lat': 20.4503,
        'lng': 85.8812,
        'urgency': 'high'
    },
    {
        'title': 'Streetlight Outage',
        'description': 'Streetlights in Saheed Nagar sector 4 have been non-functional for a week.',
        'category_name': 'Utilities',
        'location': 'Saheed Nagar, Bhubaneswar',
        'lat': 20.2847,
        'lng': 85.8500,
        'urgency': 'medium'
    }
]

for comp in sample_complaints:
    cat = Category.objects.get(name=comp['category_name'])
    Complaint.objects.get_or_create(
        title=comp['title'],
        defaults={
            'description': comp['description'],
            'category': cat,
            'location_address': comp['location'],
            'latitude': comp['lat'],
            'longitude': comp['lng'],
            'urgency': comp['urgency']
        }
    )

print("Complaint data setup complete.")
