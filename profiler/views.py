from django.shortcuts import render
from django.http import HttpResponse

from profiler.models import Student

def index(request):
	return HttpResponse("Hello world, Now we had started with our application....!")

def studentid(request, student_id):
	return HttpResponse("Id of student is : %s" % student_id)
	
def studentdata(request):
	sd = Student.objects.all()
	return render(request, "profiler/index.html", {"students_data":sd})
	
