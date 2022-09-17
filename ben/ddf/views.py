from lib2to3.pygram import pattern_symbols
from multiprocessing import context
from django.shortcuts import render,HttpResponse
from ddf.models import post,pot,pat,con

def index (request):
    allpost=post.objects.all()
    context={'allpost':allpost}
    return  render (request,'index.html',context)
def artical(request):
     dot=pot.objects.all()
     context={'dot':dot}
     return   render(request,'artical.html',context)
def service(request):
    gat=pat.objects.all()
    context={'gat':gat}
    return render(request,'service.html',context)
    
def fo(request):
    if request.method=="POST":
        email=request.POST['email']
        password=request.POST['password']
        Ca=con(email=email,password=password)
        Ca.save()

    return render(request,'form.html')
# Create your views here.
