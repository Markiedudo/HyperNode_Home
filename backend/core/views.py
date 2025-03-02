from django.shortcuts import render
from .models import ContactMessage  # Import the model
from django.http import JsonResponse,HttpResponse
from django.utils.translation import gettext_lazy as _, activate

def home(request):
    context = {
        "title": _("Home - HyperNode"),
        "description": _("Innovating the Future, One Node at a Time."),
    }
    return render(request, "home.html", context)

def test_translation(request):
    activate('zh-hans')  # Force Django to use Chinese
    translated_text = _("Welcome to HyperNode")
    return HttpResponse(f"Translated: {translated_text}")

def about(request):
    return render(request, "about.html")

def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")

        if not name or not email or not message:
            return JsonResponse({"success": False, "error": "All fields are required."})

        # Save message to the database
        ContactMessage.objects.create(name=name, email=email, message=message)

        # Return JSON response for AJAX
        return JsonResponse({"success": True})

    return render(request, "contact.html")