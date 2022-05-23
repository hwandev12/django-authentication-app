from django.shortcuts import render


# create home page view
def home(request):
    return render(request, 'pages/home.html')