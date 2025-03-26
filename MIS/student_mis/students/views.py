from django.shortcuts import redirect, render, get_object_or_404
from django.http import JsonResponse
from .models import Student

# Render the frontend (HTML page)
def index(request):
    # Fetch all students from the database
    # students = Student.objects.all()

    # # Pass the student data to the template
    # return render(request, 'index.html', {'students': students})
    # Fetch all student records from the database
    students = Student.objects.all()
    return render(request, 'index.html', {'students': students})


# API: Get all students
def student_list(request):
    students = Student.objects.all()
    data = [
        {
            "ReqNo": s.ReqNo,
            "Name": s.Name,
            "Branch": s.Branch,
            "Year": s.Year,
            "Address": s.Address,
            "City": s.City,
            "State": s.State,
            "Country": s.Country,
        } for s in students
    ]
    return JsonResponse(data, safe=False)

# API: Get a single student by ReqNo
def student_detail(request, req_no):
    student = get_object_or_404(Student, ReqNo=req_no)
    data = {
        "ReqNo": student.ReqNo,
        "Name": student.Name,
        "Branch": student.Branch,
        "Year": student.Year,
        "Address": student.Address,
        "City": student.City,
        "State": student.State,
        "Country": student.Country,
    }
    return JsonResponse(data)



def add_student(request):
    if request.method == 'POST':
        req_no = request.POST.get('req_no')
        name = request.POST.get('name')
        branch = request.POST.get('branch')
        year = request.POST.get('year')

        student = Student(
            ReqNo=req_no,
            Name=name,
            Branch=branch,
            Year=year,
        )
        student.save()
        return redirect('index')
    
    return redirect('index')


# from django.shortcuts import render
# from .models import Student


