from django import forms


class TrigonometryForm(forms.Form):
    angle = forms.CharField()
    sin = forms.CharField()
    cos = forms.CharField()
    tan = forms.CharField()
    cot = forms.CharField()
