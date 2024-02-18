from django import forms

class FibonacciForm(forms.Form):
    number_of_terms = forms.IntegerField(label='Number of Fibonacci terms', min_value=1)