from django.shortcuts import render, redirect, get_object_or_404
from . models import Data_mahasiswa
from .forms import BiodataMhs

# Create your views here.
def index(request):
	hasil = Data_mahasiswa.objects.all()
	print(hasil)
	data = {
		'data':hasil,
	}
	return render(request, "index.html", data)

def tambah(request):
    form = BiodataMhs(request.POST or None, request.FILES or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect("/")
        pass
    return render(request,"tambah.html",{'form': form})

def edit_view(request):
	return render(request, "editdata.html")

def edit(request, nim):
	obj = get_object_or_404(Data_mahasiswa, nim=nim)

	form = BiodataMhs(request.POST or None, instance = obj)
	if form.is_valid():
		form.save()
		return redirect("/")
	data = {
		'mahasiswa': obj,
	}
	return render(request, 'editdata.html',data)

def hapus(request, nim):
    dt = Data_mahasiswa.objects.get(nim=nim)
    dt.delete()
    return redirect("/")