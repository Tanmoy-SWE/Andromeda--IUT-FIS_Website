from django.shortcuts import render, HttpResponse
from .models import member, members
from django.db.models import Q

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
        student_id = (request.POST['student_id'])
        new_member = member(first_name=first_name, last_name = last_name, dept = dept, program = program, student_id =student_id)
        new_member.save()
        return HttpResponse('Member added Successfully!')
    elif request.method =='GET':
        return render(request, 'add_member.html')
    else:
        HttpResponse('An exception occured! Member has not been added')

def remove_member(request, id = 0):
    if id:
        try:
            member_to_be_remved = member.objects.get(id=id)
            member_to_be_remved.delete()
            return HttpResponse('Member Removed Successfully.')
        except:
            return HttpResponse('Please Enter A Valid Student ID.')
    members = member.objects.all()
    context = {
        'members' : members
    }
    return render(request, 'remove_member.html', context)

def filter_member(request):
    if request.method == 'POST':
        name = request.POST['name']
        dept = request.POST['dept']
        program = request.POST['program']
        member = members.objects.all()
        if name :
            member = member.filter(Q(first_name__icontains = name) | Q(last_name__icontains = name))
        if dept :
            member = member.filter(dept__icontains = dept)
        if program :
            member = member.filter(program__icontains = program)
        context = {
            'member' : member
        }
        return render(request, 'view_all_member.html', context)
    elif request.method == 'GET':
        return render(request, 'filter_member.html')
    else:
        return HttpResponse('An Error Occurred!')