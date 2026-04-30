from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def departments_view(request):
    return render(request, 'departments.html')

@login_required
def platform_engineering(request):
    return render(request, 'platform_engineering.html')

@login_required
def product_dev(request):
    return render(request, 'product_dev.html')

@login_required
def mobile_app(request):
    return render(request, 'mobile_app.html')

@login_required
def human_resources(request):
    return render(request, 'human_resources.html')

@login_required
def management(request):
    return render(request, 'management.html')

@login_required
def broadcasting(request):
    return render(request, 'broadcasting.html')