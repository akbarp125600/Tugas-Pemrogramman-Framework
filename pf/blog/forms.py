from django import forms
from .models import Data_mahasiswa
from .models import Kategori_service
from .models import Barang
from .models import Kategori_Barang

class BiodataMhs(forms.ModelForm):
    class Meta:
        model = Data_mahasiswa
        fields = "__all__"
        error_messages = {
            'no': {
                'required': 'Anda harus mengisi form NPM'
            },
            'nama' : {
                'required': "Anda harus mengisi form Nama"
            },
            'keterangan' : {
                'required': "Anda harus menset form Tanggal lahir"
            },
            'alamat':{
                'required': "Anda harus mengisi form Alamat"
            }
        }

class Kategori(forms.ModelForm):
    class Meta:
        model = Kategori_service
        fields = "__all__"
        error_messages = {
            'no': {
                'required': 'Anda harus mengisi form NPM'
            },
            'nama' : {
                'required': "Anda harus mengisi form Nama"
            },
        }

class FormBarang(forms.ModelForm):
    class Meta:
        model = Barang
        fields = "__all__"
        error_messages = {
            'no': {
                'required': 'Anda harus mengisi form NPM'
            },
            'nama' : {
                'required': "Anda harus mengisi form Nama"
            },
            'keterangan' : {
                'required': "Anda harus menset form Tanggal lahir"
            },
            'alamat':{
                'required': "Anda harus mengisi form Alamat"
            }
        }

class FormKategoriBarang(forms.ModelForm):
    class Meta:
        model = Kategori_Barang
        fields = "__all__"
        error_messages = {
            'no': {
                'required': 'Anda harus mengisi form NPM'
            },
            'nama' : {
                'required': "Anda harus mengisi form Nama"
            },
            'keterangan' : {
                'required': "Anda harus menset form Tanggal lahir"
            },
            'alamat':{
                'required': "Anda harus mengisi form Alamat"
            }
        }