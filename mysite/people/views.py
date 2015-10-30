from django.shortcuts import render, render_to_response
from django.template import RequestContext, loader
from people.forms import EmployeeForm
from people.models import Employee
# Create your views here.
from django.http import HttpResponse

def index(request):
    #import pdb;pdb.set_trace()
    context = {}
    if request.method == 'POST':
        search_query = request.POST.get('search','')
        emp_objs = Employee.objects.filter(first_name__icontains = search_query)
        context["emp_obj"] = emp_objs 
    return render_to_response('people/index.html',
                                context,
                                context_instance=RequestContext(request))

def newProfile(request):
    #import pdb;pdb.set_trace()
    form = EmployeeForm(request)
    error = False
    if request.method == 'POST':
        form = EmployeeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            
            return render_to_response('people/index.html',
                                        context = {"saved": True},
                                        context_instance=RequestContext(request))
        else:
            error = True
    context = {
        'form': form,
        'error' : error
    }

    return render_to_response('people/newProfile.html',
                                context,
                                context_instance=RequestContext(request))

