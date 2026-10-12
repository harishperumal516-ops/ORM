from django.shortcuts import render

# Create your views here.
def foodapp(request):
    return render(request, 'foodapp.html')