from django.shortcuts import render, Http404
from .models import students_data,students_marks

def home(request):
  return render(request,'index.html')

def students_list(request):
  students_list = students_data.objects.all()
  return render(request, 'students_list.html',{"students_list":students_list})
def Check(request):
    return render(request, 'results.html')

def Student_Marks(request):
    student_id = request.POST['student_id']
    std_marks = students_marks.objects.filter(id=student_id,).values()
    student_detail = students_data.objects.filter(id=student_id)

    def assign_grade(mark):
        if mark >= 91:
            return "S"
        elif mark >= 81:
            return "A"
        elif mark >= 71:
            return "B"
        elif mark >= 61:
            return "C"
        elif mark >= 51:
            return "D"
        elif mark >= 50:
            return "E"
        else:
            return "F"


    for i in std_marks:
        marks = list(i.values())
        marks = marks[2:]

    total=sum(marks)
    total = (total/400)*100
    grade_list = []

    for subject in marks:
        b = assign_grade(subject)
        grade_list.append(b)

    total_grade=assign_grade(total)


    return render(request, 'marklist.html', {"results": std_marks,"grade_list":grade_list,"student_detail":student_detail,"total":total,"total_grade":total_grade})
