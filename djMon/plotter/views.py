from django.shortcuts import render
from .models import points_collection
from django.http import HttpResponse


# Create your views here.

def index(request):
    return render(request=request, template_name= 'base.html')

def add_point(request):

    if(request.method == 'POST'):
        # print("Hi")
        data = request.POST
        print(data)

        records = {
        "X" : int(data['X']),
        "Y" : int(data['Y']),
        }
        points_collection.insert_one(records)
    # print("hello")

    return render(request=request, template_name= 'index.html')

def get_all_points(request):
    points = points_collection.find({},{'_id':0})

    # test_list = ['Hi', 'Hello']

    points_doc_list = []
    for document in points:
        points_doc_list.append(document)

    # print(points_doc_list) 

    # print(points_doc_list)
    return render(request=request, template_name='display.html', context= {'points_doc_list':points_doc_list})
