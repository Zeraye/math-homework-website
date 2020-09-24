from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import TrigonometryForm
import math


def trigonometry_solver(arr):
    # code goes here
    [angle, sin, cos, tan, cot] = arr
    angle = arr[0]
    print(type(angle))
    if angle != "":
        sin = math.sin(math.radians(angle))
        cos = math.cos(math.radians(angle))
        tan = math.tan(math.radians(angle))
        if tan != 0: cot = 1/t
        else: cot = "nie istnieje"
    else:
        return "1", "1", "1", "1", "1"
    return str(angle), str(sin), str(cos),  str(tan),  str(cot)


def trigonometry(request):
    if request.method == 'POST':
        form = TrigonometryForm(request.POST)
        # code goes here
        angle = form['angle'].value()
        sin = form['sin'].value()
        cos = form['cos'].value()
        tan = form['tan'].value()
        cot = form['cot'].value()
        arr = [angle, sin, cos, tan, cot]
        for element in arr:
            if element != "":
                element = float(element)
                print(type(element))
                print(element)
        list = trigonometry_solver(arr)
        context = {
            'angle': '<p>&alpha; = ' + list[0] + '</p>',
            'sin': '<p>sin&alpha; = ' + list[1] + '</p>',
            'cos': '<p>cos&alpha; = ' + list[2] + '</p>',
            'tan': '<p>tan&alpha; = ' + list[3] + '</p>',
            'cot': '<p>cot&alpha; = ' + list[4] + '</p>'
        }

        return render(request, 'trigonometry.html', context=context)

    else:
        form = TrigonometryForm()

    return render(request, 'trigonometry.html')
