# Generated by Django 3.1.3 on 2021-01-06 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_kategori_barang'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='barang',
            name='kategori',
        ),
        migrations.AddField(
            model_name='barang',
            name='id_kategoribarang',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]