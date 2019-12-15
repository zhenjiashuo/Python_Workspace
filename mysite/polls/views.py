from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, word. You're at the polls index.")

# Create your views here.
