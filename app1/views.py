
from django.shortcuts import render

def data_render(request):
    data='this backend data'
    d={'backend':data}
    return render(request,'backenddatadisplay.html',context=d)
# Create your views here.
