from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from django.http import HttpResponse
from .forms import ContactForm

def home(request):
    print("Using email:", settings.EMAIL_HOST_USER)

    if request.method == 'POST':
        print("🚀 POST request received on home!")
        

        name = request.POST.get('name')
        message = request.POST.get('message')
        contact_info = request.POST.get('contact_info')
        
        if not name or not message:
            return render(request, 'main/home.html', {'error': 'Please fill out all fields.'})

        subject = f"New message from {name}"
        body = f"{message}\n\nFrom: {name}\nContact Info: {contact_info}"

        try:
            send_mail(
                subject,
                body,
                settings.EMAIL_HOST_USER,
                [settings.CONTACT_EMAIL],
                fail_silently=False
            )
            print("✅ Email sent!")
            return render(request, 'main/home.html', {'success': True})
        except Exception as e:
            print("❌ Email failed:", str(e))
            return render(request, 'main/home.html', {'error': 'There was an error sending your message.'})

    return render(request, 'main/home.html')


def about(request):
    return render(request, 'main/about.html')

def services(request):
    return render(request, 'main/services.html')

def gallery(request):
    return render(request, 'main/gallery.html')
