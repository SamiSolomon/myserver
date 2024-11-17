# myapp/views.py
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render


def home_view(request):
    """
    View for the homepage with links to other routes.
    """
    return render(request, "myapp/home.html")

def name_view(request):
    """
    View to return the user's full name as a plain text response.
    """
    full_name = "Samuel Solomon"  # Replace with your actual name
    response_message = f"My full name is {full_name}."
    return HttpResponse(response_message)

def hobby_view(request):
    """
    View to return the user's favorite hobby or activity as a JSON response.
    """
    # You can add more details about the hobby here
    hobby_info = {
        "hobby": "Photography",  # Replace with your actual hobby
        " hobby1 ": "I love to learn new Technolgies",
        "hobby2": "I play and watch football .",
        "hobby3 ": "To worship God "  # Number of years you’ve been doing this hobby
    }
    return JsonResponse(hobby_info)

def dream_view(request):
    """
    View to return a motivational message about the user's dreams or goals.
    """
    # Define a motivational message that expresses your vision or goal
    motivational_message = (
        "I aspire to make a positive impact through technology by "
        "developing solutions that address real-world problems. "
        "My dream is to lead projects that improve accessibility "
        "and sustainability in underserved communities."
    )
    return HttpResponse(motivational_message)
