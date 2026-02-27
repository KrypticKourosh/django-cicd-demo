from django.http import JsonResponse

def home(request):
    return JsonResponse(
        {'message': 'This change has to be made on the host!'}
    )