from django.shortcuts import render
from django.http import HttpResponse

def jobroles(request):
    job1 = "reporting executive"
    job2 = "business analyst"
    job3 = "data analyst"
    job4 = "statiscian"
    job5 = "data scientist"
    job6 = "data engineer/data architect"
    job7 = "machine learning engineer"
    job8 = "big data engineer"


    return HttpResponse("1");

