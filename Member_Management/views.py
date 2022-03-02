from django.shortcuts import render, HttpResponse
from .models import member, Department, Wing

# Create your views here.
def memberHome(request):
    return render(request, 'memberHome.html')

def view_all_member(request):
    members = member.objects.all()
    context = {
        'members' : members,
    }
    return render(request, 'view_all_member.html', context)

def add_member(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        dept = request.POST['dept']
        program = request.POST['program']
        new_dept = Department(dept,program)
        new_dept.save()
        student_id = (request.POST['student_id'])
        new_member = member(first_name=first_name, last_name = last_name, department = dept, student_id =student_id)
        new_member.save()
        return HttpResponse('Member added Successfully!')
    elif request.method =='GET':
        return render(request, 'add_member.html')
    else:
        HttpResponse('An exception occured! Member has not been added')

def remove_member(request):
    return render(request, 'remove_member.html')

def filter_member(request):
    return render(request, 'filter_member.html')