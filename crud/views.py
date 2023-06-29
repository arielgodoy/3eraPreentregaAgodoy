from django.shortcuts import render, redirect
from .models import Documento
from .forms import DocForm

# Create your views here.
def inicio(request):   
    return render(request,"base.html")  

def buscarDocs(request, name):
    docs = Documento.objects.filter(titulo = name)
    return render(request,"listadocs.html",{'docs':docs}) 


def listarDocs(request):  
    docs = Documento.objects.all()  
    return render(request,"listadocs.html",{'docs':docs})  

def creaDocs(request):  
    if request.method == "POST":  
        form = DocForm(request.POST)  
        if form.is_valid():  
            try:  
                if form.save():
                    print("todo ok 2")
                model = form.instance        

                return redirect('listarDocs')  
            except:  
                pass  
    else:  
        form = DocForm()  
    return render(request,'creadoc.html',{'form':form})  

def updateDocs(request, id):  
    doc = Documento.objects.get(id=id)
    form = DocForm(initial={'titulo': doc.titulo, 'descripcion': doc.descripcion, 'autor': doc.autor, 'anio': doc.anio})
    if request.method == "POST":  
        form = DocForm(request.POST, instance=doc)  
        if form.is_valid():  
            try:  
                form.save() 
                model = form.instance
                return redirect('listarDocs')  
            except Exception as e: 
                pass    
    return render(request,'docupdate.html',{'form':form})  

def deleteDocs(request, id):
    doc = Documento.objects.get(id=id)
    try:
        doc.delete()
    except:
        pass
    return redirect('listarDocs')