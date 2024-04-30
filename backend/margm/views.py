from django.shortcuts import render

def index(request):
    
    context = {}

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'home.html', context=context)