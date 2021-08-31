from django.db import models
# Create your models here.
class Data_mahasiswa(models.Model):
    nim 		= models.IntegerField(primary_key=True)
    nama 		= models.CharField(max_length=100, blank=True, null=True)
    keterangan 	= models.TextField(blank=True, null=True)
    id_kategori = models.IntegerField(blank=True, null=True)
    images 		= models.ImageField(max_length=200,null=True, blank=True,upload_to='images/')

    class Meta:
        db_table = 'dt_mahasiswa'

class Kategori_service(models.Model):
    id_kategori     = models.IntegerField(primary_key=True)
    nama_kategori   = models.CharField(max_length=50)

    class Meta:
        db_table = 'kategori'

class Barang(models.Model):
    id_barang         = models.IntegerField(primary_key=True)
    nama              = models.CharField(max_length=50, blank=True, null=True)
    harga             = models.BigIntegerField(blank=True, null=True)
    id_kategoribarang = models.IntegerField(blank=True, null=True)
    keterangan        = models.TextField(blank=True, null=True)
    images            = models.ImageField(max_length=200,null=True, blank=True,upload_to='images/')

    class Meta:
        db_table = 'barang'

class Kategori_Barang(models.Model):
    id_kategoribarang   = models.IntegerField(primary_key=True)
    nama                = models.CharField(max_length=50,null=True, blank=True)

    class Meta:
        db_table = 'kategori_barang'