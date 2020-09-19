from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import QuadraticForm
from fractions import Fraction


def quadratic_solver(a, b, c):
    approx = 3
    if a != 0:
        delta = b**2-4*a*c
        if delta % 1 == 0: delta = int(delta)
        p = -b/(2*a)
        if p % 1 == 0: p = int(p)
        else: p = round(p, approx)
        q = -delta/(4*a)
        if q % 1 == 0: q = int(q)
        else: q = round(q, approx)
        if delta >= 0:
            root_of_delta = delta**(1/2)
            x1 = (-b+root_of_delta)/(2*a)
            if x1 % 1 == 0: x1 = int(x1)
            else: x1 = round(x1, approx)
            x2 = (-b-root_of_delta)/(2*a)
            if x2 % 1 == 0: x2 = int(x2)
            else: x2 = round(x2, approx)
        else:
            x1 = x2 = "brak"
    elif b != 0:
        x1 = -c/b
        if x1 % 1 == 0: x1 = int(x1)
        else: x1 = round(x1, approx)
    else: return str(c)

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

    if a == 0 and b != 0: return equat, str(x1)
    else: return equat, str(x1), str(x2), str(p), str(q), str(delta)


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

        try:
            context = {
                'equat': list[0],
                'x1': '<p>x&#8321; = ' + list[1] + '</p>',
                'x2': '<p>x&#8322; = ' + list[2] + '</p>',
                'p': '<p>p = ' + list[3] + '</p>',
                'q': '<p>q = ' + list[4] + '</p>',
                'delta': '<p>&#8710; = ' + list[5] + '</p>'
                # 'equat': list[0],
                # 'x1': list[1],
                # 'x2': list[2],
                # 'p': list[3],
                # 'q': list[4],
                # 'delta': list[5],
            }
        except:
            try:
                context = {
                    'equat': list[0],
                    'x1': '<p>x = ' + list[1] + '</p>'
                }
            except:
                context = {
                    'equat': list,
                }

        return render(request, 'quadratic.html', context=context)

    else:
        form = QuadraticForm()

    return render(request, 'quadratic.html')
