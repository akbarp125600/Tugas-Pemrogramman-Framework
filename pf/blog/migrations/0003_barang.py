# Generated by Django 3.1.3 on 2021-01-05 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20201217_1523'),
    ]

    operations = [
        migrations.CreateModel(
            name='Barang',
            fields=[
                ('id_barang', models.IntegerField(primary_key=True, serialize=False)),
                ('nama', models.CharField(blank=True, max_length=50, null=True)),
                ('harga', models.BigIntegerField(blank=True, null=True)),
                ('kategori', models.CharField(blank=True, max_length=20, null=True)),
                ('images', models.ImageField(blank=True, max_length=200, null=True, upload_to='images/')),
            ],
            options={
                'db_table': 'barang',
            },
        ),
    ]