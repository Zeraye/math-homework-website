from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import QuadraticForm
from fractions import Fraction


def quadratic_solver(a, b, c):
    if a != 0:
        delta = b**2-4*a*c
        p = -b/(2*a)
        q = -delta/(4*a)
        if delta >= 0:
            root_of_delta = delta**(1/2)
            x1 = (-b+root_of_delta)/(2*a)
            x2 = (-b-root_of_delta)/(2*a)
        else:
            root_of_delta = x1 = x2 = "brak"
    elif b != 0:
        delta = root_of_delta = p = q = "brak"
        x1 = x2 = -c/b
    else: delta = root_of_delta = p = q = x1 = x2 = "brak"

    equat_arr = []

    if a != 0:
        if a == 1: equat_arr.append("x&sup2;")
        elif a == -1: equat_arr.append("-x&sup2;")
        else: equat_arr.append(str(a) + "x&sup2;" )

    if b != 0:
        if b > 0 and a != 0: equat_arr.append("+")
        if b == 1: equat_arr.append("x")
        elif b == -1: equat_arr.append("x")
        elif b > 0: equat_arr.append(str(b) + "x")
        else: equat_arr.append(str(b) + "x" )

    if c < 0: equat_arr.append(str(c))
    elif c > 0 and (a != 0 or b != 0): equat_arr.append("+" + str(c))

    equat = ""
    for i in range(len(equat_arr)):
        equat += equat_arr[i]

    return equat, x1, x2, p, q, delta


def quadratic(request):
    if request.method == 'POST':
        form = QuadraticForm(request.POST)
        a = form['a'].value()
        b = form['b'].value()
        c = form['c'].value()
        if a == "": a = "0"
        if b == "": b = "0"
        if c == "": c = "0"
        try:
            list = quadratic_solver(int(a), int(b), int(c))
        except:
            return render(request, 'quadratic.html')
        context = {
            'equat': list[0],
            'x1': list[1],
            'x2': list[2],
            'p': list[3],
            'q': list[4],
            'delta': list[5]
        }

        return render(request, 'quadratic.html', context=context)

    else:
        form = QuadraticForm()

    return render(request, 'quadratic.html')
