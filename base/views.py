from django.http import HttpResponse

def baseView(request):
    return HttpResponse("hey this is base file")