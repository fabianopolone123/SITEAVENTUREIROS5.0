"""Views básicas para diagnóstico."""
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def client_events(request):
    if request.method != 'POST':
        return JsonResponse({'detail': 'Method not allowed'}, status=405)

    return JsonResponse({
        'status': 'ok',
        'received': request.body.decode('utf-8')[:100]
    })


def stream_events(request):
    return JsonResponse({'status': 'stream not implemented'})
