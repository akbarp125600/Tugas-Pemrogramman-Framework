from django.contrib import admin
from django.urls import include, path
from django.conf.urls import url, include
from blog import views
from django.conf import settings
from django.conf.urls.static import static

#method view index
urlpatterns = [
#Fuctions Users
    path('admin/', admin.site.urls),
    path('',views.index),
    path('index_admin',views.index_admin),
    path('about',views.about),
    path('service',views.service),
    path('service_list',views.service_list),
    path('service_detail/<int:nim>',views.service_detail),
    path('blog',views.blog),
    path('blog_detail',views.blog_detail),
    path('career',views.career),
    path('faq',views.faq),
    path('privacy_policy',views.privacy_policy),
    path('catalog',views.catalog),
    path('catalog_detail/<int:id_barang>',views.catalog_detail),
    path('contact',views.contact),

    #function Login
    path('login',views.login),

    #Function Admin
    path('index_admin',views.index_admin),
    path('tambah_view',views.tambah_view),
    path('tambahdata',views.tambahdata),
    path('editdata/<int:nim>',views.edit),
    path('hapusdata/<int:nim>',views.hapusdata),
    path('kategori_view',views.kategori_view),
    path('tambah_kategori',views.tambah_kategori),
    path('edit_kategori/<int:id_kategori>',views.edit_kategori),
    path('hapus_kategori/<int:id_kategori>',views.hapus_kategori),
    path('detail_kategori/<int:id_kategori>',views.detail_kategori),
    path('barang_view',views.barang_view),
    path('tambah_barang',views.tambah_barang),
    path('edit_barang/<int:id_barang>',views.edit_barang),
    path('hapus_barang/<int:id_barang>',views.hapus_barang),
    path('view_kategoribarang',views.view_kategoribarang),
    path('tambah_kategoribarang',views.tambah_kategoribarang),
    path('edit_kategoribarang/<int:id_kategoribarang>',views.edit_kategoribarang),
    path('hapus_kategoribarang/<int:id_kategoribarang>',views.hapus_kategoribarang),

] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
