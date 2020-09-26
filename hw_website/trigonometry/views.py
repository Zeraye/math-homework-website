from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import TrigonometryForm
import math


def trigonometry_solver(angle, sin, cos, tan, cot):
    approx = 3
    try:
        if angle != "":
            angle = math.radians(float(angle))
            sin = math.sin(angle)
            cos = math.cos(angle)
            tan = math.tan(angle)
            if tan != 0: cot = 1/tan
            else: cot = "brak"
        elif sin != "":
            sin = float(sin)
            angle = math.asin(sin)
            cos = math.cos(angle)
            tan = math.tan(angle)
            if tan != 0: cot = 1/tan
            else: cot = "brak"
        elif cos != "":
            cos = float(cos)
            angle = math.acos(sin)
            sin = math.sin(angle)
            tan = math.tan(angle)
            if tan != 0: cot = 1/tan
            else: cot = "brak"
        elif tan != "":
            tan = float(tan)
            angle = math.atan(tan)
            sin = math.sin(angle)
            cos = math.cos(angle)
            if tan != 0: cot = 1/tan
            else: cot = "brak"
        elif cot != "":
            cot = float(cot)
            if cot != 0:
                tan = 1/cot
                angle = math.atan(tan)
                sin = math.sin(angle)
                cos = math.cos(angle)
            else:
                tan = "brak"
                cos = 0
                sin = 1
                angle = math.asin(sin)
        else: return "brak", "brak", "brak", "brak", "brak"
        if sin != "brak" and sin > 1000: sin = "&infin;"
        if cos != "brak" and cos > 1000: cos = "&infin;"
        if tan != "brak" and tan > 1000: tan = "&infin;"
        if cot != "brak" and cot > 1000: cot = "&infin;"
        if sin != "brak" and sin < -1000: sin = "-&infin;"
        if cos != "brak" and cos < -1000: cos = "-&infin;"
        if tan != "brak" and tan < -1000: tan = "-&infin;"
        if cot != "brak" and cot < -1000: cot = "-&infin;"
        angle = math.degrees(angle)
        if angle != "brak": angle = round(angle, approx)
        if sin != "brak": sin = round(sin, approx)
        if cos != "brak": cos = round(sin, approx)
        if tan != "brak": tan = round(sin, approx)
        if cot != "brak": cot = round(sin, approx)
        return str(angle), str(sin), str(cos), str(tan), str(cot)
    except: return "brak", "brak", "brak", "brak", "brak"


def trigonometry(request):
    if request.method == 'POST':
        form = TrigonometryForm(request.POST)
        angle = form['angle'].value()
        sin = form['sin'].value()
        cos = form['cos'].value()
        tan = form['tan'].value()
        cot = form['cot'].value()
        list = trigonometry_solver(angle, sin, cos, tan, cot)
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
