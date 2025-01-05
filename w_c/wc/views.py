from django.shortcuts import render

# Create your views here.
def home(request):

	context=("name":"HOME")
	return request(render,"home.html",context)

