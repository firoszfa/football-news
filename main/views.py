from django.shortcuts import render

# Create your views here.

def show_main(request):
    context = {
        'npm' : '2406412972',
        'name': 'Firos Aqiela Zufa',
        'class': 'PBP F'
    }

    return render(request, "main.html", context)
