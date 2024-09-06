from django.http import JsonResponse
from .message import SUCCESS_MESSAGE, ERROR_MESSAGE


def success_response(data=None, message=SUCCESS_MESSAGE, status=200):
    response = {
        "status": status,
        "message": message,
        "data": data
    }
    return JsonResponse(response, status=status)

def error_response(message=ERROR_MESSAGE,status=400):
    response = {
        "status": status,
        "message": message
    }
    return JsonResponse(response, status=status)
