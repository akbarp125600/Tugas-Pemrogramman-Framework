from django.contrib import admin
from django.urls import include, path
from django.conf.urls import url, include
from mahasiswa import views
#from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index),
   	path('tambah_view',views.tambah),
   	path('editdata/<int:nim>',views.edit),
   	path('hapusdata/<int:nim>',views.hapus),
    #url(r'^mahasiswa/', include('mahasiswa.urls')),
]