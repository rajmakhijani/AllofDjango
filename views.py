from django.shortcuts import render
from .forms import inputForm
from django.http import HttpResponseRedirect,HttpResponse


# Create your views here.
def add(request):      
    form = inputForm(request.POST)     
    if form.is_valid():  
        form.save()             
        cd = form.cleaned_data    
        input1 = cd['inputa']
        input2 = cd['inputb']
        output = input1 + input2
        return HttpResponseRedirect('/math/{output}'.format(output=output))
    else:
        form = inputForm()   
    return render(request, 'math/base.html', {'form': form }) 

def thanks(request,id):
    return HttpResponse(f"sum of two numbers will be : {id}")