from django.shortcuts import render
from django.http import JsonResponse
from  django.views.decorators.csrf import csrf_exempt
import json
from .utils import add, subtract, multiply, divide


def index(request):
    return render(request, 'index.html')


@csrf_exempt
def calculate(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        x = data.get('x')
        y = data.get('y')
        operation = data.get('operation')

        if operation == 'add':
            result = add(x, y)
        elif operation == 'subtract':
            result = subtract(x, y)
        elif operation == 'multiply':
            result = multiply(x, y)
        elif operation == 'divide':
            result = divide(x, y)
        else:
            result = 'Error: Invalid operation'

        return JsonResponse({'result': result})
    return JsonResponse({'error': 'Invalid request'}, status=400)
