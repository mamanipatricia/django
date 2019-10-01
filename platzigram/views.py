# platzgram views

# django
from django.http import HttpResponse

# utilities
from datetime import datetime
import json

def hello_world(request):
    """ return a greeting """
    # now = datetime.now()
    # using la funcion string format time
    # now = datetime.now().strftime('%b %dth, %Y  - %H:%M hrs')
    # return HttpResponse('Oh, hi! Current server time is {now}'.format(now=str(now)))

    return HttpResponse('Oh, hi! Current server time is {now}'.format(
        now=datetime.now().strftime('%b %dth, %Y  - %H:%M hrs')
    ))


def sorted_integers(request):
    """ return  a JSON response with sorted integers"""
    # print(request)
    # pdb debugger
    # import pdb; pdb.set_trace()
    # print(request.GET['numbers'])
    ## numbers = request.GET['numbers']
    ## return HttpResponse(str(numbers))
    # return HttpResponse("Hii...!")

    numbers = [int(i) for i in request.GET['numbers'].split(',')]
    sorted_ints = sorted(numbers)

    # como regresar un JSON
    data = {
        'status': 'ok',
        'numbers': sorted_ints,
        'message': 'Integers sorted succesfully.'
    }
    # return HttpResponse(str(numbers), content_type='application/json')
    return HttpResponse(
        json.dumps(data, indent=4),
        content_type='application/json'
    )
# otras maneras de pasar argumentos
def say_hi(request, name, age):
    """ Return a greeting."""
    if age < 12:
        message = 'Sorry {}, you are not allowed here'.format(name)

    else:
        message = 'Hello, {}! Welcome to Platzigram'.format(name)

    return HttpResponse(message)











