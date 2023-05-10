from django.shortcuts import render
from .models import *
from django.db.models import Q
from django.views.generic import *
from django.urls import reverse_lazy
# Create your views here.
def home(request):
    category = Category.objects.all().order_by('-id')
    if 'q' in request.GET:
        q = request.GET['q']
        malumot = Malumot.objects.filter(Q(name__icontains=q)) 
    else:
        malumot = Malumot.objects.all().order_by('-id')
    return render(request,'list.html',{'malumot':malumot,'category':category})
class detail(DetailView):
    model = Malumot
    template_name = 'detail.html'
def nomi(request):
    category = Category.objects.all().order_by('-id')
    if 'q' in request.GET:
        q = request.GET['q']
        malumot = Malumot.objects.filter(Q(name__icontains=q)) 
    else:
        malumot = Malumot.objects.all().order_by('-name')
    return render(request,'list.html',{'malumot':malumot,'category':category})
def matn(request):
    category = Category.objects.all().order_by('-id')
    if 'q' in request.GET:
        q = request.GET['q']
        malumot = Malumot.objects.filter(Q(name__icontains=q)) 
    else:
        malumot = Malumot.objects.all().order_by('-text')
    return render(request,'list.html',{'malumot':malumot,'category':category})
def audio(request):
    category = Category.objects.all().order_by('-id')
    if 'q' in request.GET:
        q = request.GET['q']
        malumot = Malumot.objects.filter(Q(name__icontains=q)) 
    else:
        malumot = Malumot.objects.all().order_by('-audio')
    return render(request,'list.html',{'malumot':malumot,'category':category})
def categores(request):
    qi = request.GET.get('category')
    category = Category.objects.all()
    if category == None:
             malumot = Malumot.objects.all()
    else:
            malumot = Malumot.objects.filter(category__name=qi)
    return render(request,'cate.html',{'malumot':malumot,'category':category,'qi':qi})
def dashboard(request):
    category = Category.objects.all().order_by('-id')
    if 'q' in request.GET:
        q = request.GET['q']
        malumot = Malumot.objects.filter(Q(name__icontains=q)) 
    else:
        malumot = Malumot.objects.all().order_by('-id')
    return render(request,'dashboard/index.html',{'malumot':malumot,'category':category})
class MalumotCreate(CreateView):
    model = Malumot
    template_name = 'dashboard/new.html'
    fields = ['name','category','audio','text','img']
class MalumotUpdate(UpdateView):
    model = Malumot
    template_name = 'dashboard/update.html'
    fields = ['name','category','audio','text','img']
class MalumotDelete(DeleteView):
    model = Malumot
    template_name = 'dashboard/update.html'
    success_url = reverse_lazy('dash')
class detailAdmin(DetailView):
    model = Malumot
    template_name = 'dashboard/detaila.html'
