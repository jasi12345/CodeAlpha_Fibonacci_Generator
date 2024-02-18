from django.shortcuts import render
from django.http import JsonResponse
from .forms import FibonacciForm



def Fibonnacciview(request):
    form = FibonacciForm()
    return render(request,'myfirst.html',{'form':form})


def fibonaccigenerator(n):
   fibsequence = []

   if n >= 1:
        fibsequence.append(0)
   if n >= 2:
        fibsequence.append(1)

   for i in range(2,n):
        fibsequence.append(fibsequence[-1] +fibsequence[-2])
   return fibsequence

def generatefibonnacci(request):
    if request.method == 'POST':
        form =FibonacciForm(request.POST)
        if form.is_valid():
            number_of_terms = form.cleaned_data['number_of_terms']
            fibonacci_sequence  = fibonaccigenerator(number_of_terms)
            return JsonResponse({'fibonnacci_sequence':fibonacci_sequence })
    return JsonResponse({'error':'Invalid request'})
