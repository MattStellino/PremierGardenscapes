"""
Views for the Premier Gardenscapes website.
Handles the main landing page and contact form processing.
"""

from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from django.http import HttpResponse


def home(request):
    """
    Main landing page view that handles both GET and POST requests.
    
    GET: Renders the home page with all sections
    POST: Processes contact form submissions and sends emails
    """
    # Email configuration loaded from settings

    if request.method == 'POST':
        # Extract form data
        name = request.POST.get('name')
        message = request.POST.get('message')
        contact_info = request.POST.get('contact_info')

        # Validate required fields
        if not name or not message:
            return render(request, 'main/home.html', {
                'error': 'Please fill out all required fields.'
            })

        # Prepare email content
        subject = f"New message from {name}"
        body = f"{message}\n\nFrom: {name}\nContact Info: {contact_info}"

        try:
            # Send email using Django's email backend
            send_mail(
                subject=subject,
                message=body,
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[settings.CONTACT_EMAIL],
                fail_silently=False
            )
            return render(request, 'main/home.html', {'success': True})
            
        except Exception as e:
            return render(request, 'main/home.html', {
                'error': 'There was an error sending your message. Please try again.'
            })

    # GET request - render the home page
    return render(request, 'main/home.html')


# Legacy view functions (kept for potential future use)
def about(request):
    """Legacy about page view - currently unused in single-page layout."""
    return render(request, 'main/about.html')


def services(request):
    """Legacy services page view - currently unused in single-page layout."""
    return render(request, 'main/services.html')


def gallery(request):
    """Legacy gallery page view - currently unused in single-page layout."""
    return render(request, 'main/gallery.html')
