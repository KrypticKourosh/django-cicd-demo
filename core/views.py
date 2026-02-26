from django.http import JsonResponse

def home(request):
    return JsonResponse(
        {'message': 'CI/CD is wokring!'}
    )