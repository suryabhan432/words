from django.http import HttpResponse
from django.shortcuts import render
import operator

def home(request):
	return render(request,'home.html')

def index(request):
	x = request.GET['area']
	y = x.split()
	z = len(y)

	worddictionary = {}
	for word in y:
		if word in worddictionary:
			worddictionary[word] += 1
		else:
			worddictionary[word] = 1
	
	sorted_list = sorted(worddictionary.items(),key = operator.itemgetter(1))
			
	a = {'surya':x,'list':y,'satish':z,'repeat_word':sorted_list}
	return render(request,'show.html',a)


