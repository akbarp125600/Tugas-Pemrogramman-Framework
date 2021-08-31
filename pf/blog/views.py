from django.shortcuts import render, redirect, get_object_or_404
from .models import Data_mahasiswa
from .models import Kategori_service
from .models import Barang
from .models import Kategori_Barang
from .forms import FormBarang
from .forms import FormKategoriBarang
from .forms import BiodataMhs
from .forms import Kategori
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.db import connection
# from .models import 

#functions user
def index(request):
	return render(request,'index.html')

def about(request):
	return render(request,'user/view_about.html')

def service(request):
	return render(request,'user/view_service.html')

def service_list(request):
	hasil = Data_mahasiswa.objects.all()
	print(hasil)
	data = {
	'data': hasil,
	}
	return render(request,'user/view_service_list.html',data)

def service_detail(request, nim):
	obj = get_object_or_404(Data_mahasiswa, nim = nim)

	form = BiodataMhs(request.POST or None,request.FILES or None, instance = obj)
	# if form.is_valid():
	# 	form.save()
	# 	return redirect('/tambah_view')
	data = {
	'mhs' : obj,
	}
	return render(request,'user/view_service_detail.html', data)

def blog(request):
	return render(request,'user/view_blog.html')

def blog_detail(request):
	return render(request,'user/view_blog_detail.html')

def career(request):
	return render(request,'user/view_career.html')

def faq(request):
	return render(request,'user/view_faq.html')

def privacy_policy(request):
	return render(request,'user/view_privacy_policy.html')

def catalog(request):
	hasil = Barang.objects.all()
	data = {
	'data': hasil,
	}
	return render(request,'user/view_catalog.html', data)

def catalog_detail(request, id_barang):
	obj = get_object_or_404(Barang, id_barang = id_barang)

	form = FormBarang(request.POST or None,request.FILES or None, instance = obj)
	# if form.is_valid():
	# 	form.save()
	# 	return redirect('/tambah_view')
	data = {
	'mhs' : obj,
	}
	return render(request,'user/view_catalogdetail.html', data)

def contact(request):
	return render(request,'user/view_contact.html')

#functions login
def login(request):
	if request.method == 'POST':

		username_login = request.POST['username']
		password_login = request.POST['password']

		user = authenticate(request, username=username_login, password=password_login)

		if user is None:
			login(request, user)
		return render(request, 'admin/index_admin.html')

	return render(request,"login/login.html")

#---Functions Admin---#
def index_admin(request):
	return render(request,"admin/index_admin.html")

#functions tambah data service
# d
def tambah_view(request):
	cursor 	=connection.cursor()
	cursor.execute("select dt_mahasiswa.nim, dt_mahasiswa.nama, kategori.nama_kategori, dt_mahasiswa.keterangan, dt_mahasiswa.images from dt_mahasiswa INNER JOIN kategori ON dt_mahasiswa.id_kategori = kategori.id_kategori order by dt_mahasiswa.nim asc ")
	results = cursor.fetchall()
	return render(request,'pages/data service/data.html',{'Data_mahasiswa':results})

def tambahdata(request):
    form 	= BiodataMhs(request.POST or None, request.FILES or None)
    kat 	= Kategori_service.objects.all()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('/tambah_view')

    return render(request,"pages/data service/tambahdata.html",{'form': form,'kategori': kat})

def edit(request, nim):
	kat 	= Kategori_service.objects.all()
	obj 	= get_object_or_404(Data_mahasiswa, nim = nim)
	form 	= BiodataMhs(request.POST or None,request.FILES or None, instance = obj)
	if form.is_valid():
		form.save()
		return redirect('/tambah_view')
	data = {
	'mhs' : obj,
	'kategori' : kat,
	}
	return render(request,"pages/data service/editdata.html", data)

def hapusdata(request, nim):
    dt = Data_mahasiswa.objects.get(nim = nim)
    dt.delete()
    return redirect('/tambah_view')

#functions data kategori Service
def kategori_view(request):
	hasil = Kategori_service.objects.all()
	data = {
	'data' : hasil,
	}
	return render(request,"pages/kategori service/kategori_view.html",data)

def detail_kategori(request, id_kategori):
	cursor 	=connection.cursor()
	cursor.execute("select dt_mahasiswa.nim, dt_mahasiswa.nama, kategori.id_kategori, kategori.nama_kategori, dt_mahasiswa.keterangan, dt_mahasiswa.images from dt_mahasiswa INNER JOIN kategori ON dt_mahasiswa.id_kategori = kategori.id_kategori order by dt_mahasiswa.nim asc ")
	results = cursor.fetchall()
	return render(request,"pages/kategori service/detail_kategori.html",{'Data_mahasiswa':results})

def tambah_kategori(request):
	form = Kategori(request.POST or None, request.FILES or None)
	if request.method == 'POST':
		if form.is_valid():
			form.save()
			return redirect('/kategori_view')
	return render(request,"pages/kategori service/tambah_kategori.html")

def edit_kategori(request, id_kategori):
	obj  = get_object_or_404(Kategori_service, id_kategori = id_kategori)
	form = Kategori(request.POST or None, instance = obj)
	if form.is_valid():
		form.save()
		return redirect('/kategori_view')
	data = {
	'mhs' : obj,
	}
	return render(request,"pages/kategori service/edit_kategori.html",data)

def hapus_kategori(request, id_kategori):
    dt = Kategori_service.objects.get(id_kategori=id_kategori)
    dt.delete()
    return redirect('/kategori_view')

def barang_view(request):
	cursor 	=connection.cursor()
	cursor.execute("select barang.id_barang, barang.nama, barang.harga, barang.id_kategoribarang,barang.images, kategori_barang.id_kategoribarang, kategori_barang.nama, barang.keterangan from  barang INNER JOIN kategori_barang ON barang.id_kategoribarang = kategori_barang.id_kategoribarang order by barang.id_barang asc")
	results = cursor.fetchall()
	return render(request,'pages/barang/barang_view.html',{'Barang':results})

def tambah_barang(request):
	kat  = Kategori_Barang.objects.all()
	form = FormBarang(request.POST or None, request.FILES or None)
	if request.method == 'POST':
		if form.is_valid():
			form.save()
			return redirect('/barang_view')
	return render(request,'pages/barang/tambah_barang.html',{'form': form,'kategori_barang': kat})

def edit_barang(request, id_barang):
	kat  = Kategori_Barang.objects.all()
	obj  = get_object_or_404(Barang, id_barang = id_barang)
	form = FormBarang(request.POST or None, instance = obj)
	if form.is_valid():
		form.save()
		return redirect('/barang_view')
	data = {
	'mhs' : obj,
	'kategori_barang' : kat, 
	}
	return render(request,'pages/barang/edit_barang.html', data)

def hapus_barang(request, id_barang):
	dt = Barang.objects.get(id_barang = id_barang)
	dt.delete()
	return redirect('/barang_view')

def view_kategoribarang(request):
	hasil = Kategori_Barang.objects.all()
	data = {
	'data' : hasil,
	}
	return render(request,'pages/kategori barang/view_kategoribarang.html', data)

def tambah_kategoribarang(request):
	form = FormKategoriBarang(request.POST or None, request.FILES or None)
	if request.method == 'POST':
		if form.is_valid():
			form.save()
			return redirect('/view_kategoribarang')
	return render(request,'pages/kategori barang/tambah_kategoribarang.html')

def edit_kategoribarang(request, id_kategoribarang):
	obj  = get_object_or_404(Kategori_Barang, id_kategoribarang = id_kategoribarang)
	form = FormKategoriBarang(request.POST or None, instance = obj)
	if form.is_valid():
		form.save()
		return redirect('/view_kategoribarang')
	data = {
	'mhs' : obj,
	}
	return render(request,'pages/kategori barang/edit_kategoribarang.html', data)

def hapus_kategoribarang(request, id_kategoribarang):
	dt = Kategori_Barang.objects.get(id_kategoribarang = id_kategoribarang)
	dt.delete()
	return redirect('/view_kategoribarang')