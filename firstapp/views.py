from django.http import HttpResponse
from datetime import date

# Define view functions

def index(request):
    """
    View function for the index page.
    
    Returns:
        HttpResponse: HTML response containing a simple message.
    """
    # Create a simple HTML template
    template = "<html>" \
                "This is your first view" \
               "</html>"
    # Return the template as the content of the HTTP response
    return HttpResponse(content=template)

def get_date(request):
    """
    View function to display the current date.
    
    Returns:
        HttpResponse: HTML response containing today's date.
    """
    # Get today's date
    today = date.today()
    # Create HTML template with today's date
    template = "<html>" \
                f"Today's date is {today}" \
               "</html>"
    # Return the template as the content of the HTTP response
    return HttpResponse(content=template)