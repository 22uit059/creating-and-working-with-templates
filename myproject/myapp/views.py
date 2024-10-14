# Create your views here.
from django.shortcuts import render

def home(request):
    number_result = None
    name_result = None

    if request.method == 'GET':
        number = request.GET.get('number')
        if number:
            number = int(number)
            if number % 2 == 0:
                number_result = f"{number} is an even number"
            else:
                number_result = f"{number} is an odd number"
        
        char = request.GET.get('character')
        if char:
            names = ['Hello', 'Hi', 'Harry', 'Arthy', 'Henry']
            name_result = [name for name in names if name.startswith(char)]

    context = {
        'number_result': number_result,
        'name_result': name_result,
    }
    return render(request, 'home.html', {'name_result':name_result})
