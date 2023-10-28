from django.shortcuts import render

# Create your views here.
def calculate(request):
    if request.method == 'POST':
        operation = request.POST.get('operation')
        num1 = float(request.POST.get('num1'))
        num2 = float(request.POST.get('num2'))
        
        result = None

        if operation == 'add':
            result = num1 + num2
        elif operation == 'subtract':
            result = num1 - num2
        elif operation == 'multiply':
            result = num1 * num2

        return render(request, 'calculator.html', {'result': result})

    return render(request, 'calculator.html')

