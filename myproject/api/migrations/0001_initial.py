# Generated by Django 2.1.1 on 2018-10-25 08:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='master_barang',
            fields=[
                ('barang_id', models.AutoField(primary_key=True, serialize=False)),
                ('kode', models.CharField(max_length=100)),
                ('barcode', models.CharField(max_length=100)),
                ('nama', models.CharField(max_length=200)),
                ('alias', models.CharField(max_length=200)),
                ('harga1', models.CharField(max_length=200)),
                ('harga2', models.CharField(max_length=200)),
                ('harga3', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='master_kategori',
            fields=[
                ('kategori_id', models.AutoField(primary_key=True, serialize=False)),
                ('kode', models.CharField(max_length=200)),
                ('nama', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='master_location',
            fields=[
                ('location_id', models.AutoField(primary_key=True, serialize=False)),
                ('type', models.CharField(max_length=150)),
                ('code', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='master_merk',
            fields=[
                ('merk_id', models.AutoField(primary_key=True, serialize=False)),
                ('merk', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='master_pelanggan',
            fields=[
                ('pelanggan_id', models.AutoField(primary_key=True, serialize=False)),
                ('tipe', models.CharField(max_length=200)),
                ('nama', models.CharField(max_length=200)),
                ('alamat', models.CharField(max_length=1000)),
                ('kode_pos', models.IntegerField()),
                ('telepon', models.CharField(max_length=100)),
                ('fax', models.CharField(max_length=100)),
                ('hp', models.CharField(max_length=100)),
                ('nama_pj', models.CharField(max_length=200)),
                ('hp_pj', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='master_unit',
            fields=[
                ('unit_id', models.AutoField(primary_key=True, serialize=False)),
                ('satuan', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='master_vendor',
            fields=[
                ('vendor_id', models.AutoField(primary_key=True, serialize=False)),
                ('nama', models.CharField(max_length=200)),
                ('alamat', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='receiving_detail',
            fields=[
                ('id_rd', models.AutoField(primary_key=True, serialize=False)),
                ('note', models.CharField(max_length=1000)),
                ('qty', models.IntegerField()),
                ('barang', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.master_kategori')),
            ],
        ),
        migrations.CreateModel(
            name='receiving_header',
            fields=[
                ('id_rh', models.AutoField(primary_key=True, serialize=False)),
                ('approval', models.IntegerField()),
                ('approval_date', models.DateField()),
                ('counter', models.IntegerField()),
                ('date', models.DateField()),
                ('note', models.CharField(max_length=1000)),
                ('doc_number', models.CharField(max_length=100)),
                ('status', models.CharField(max_length=100)),
                ('lokasi', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.master_location')),
                ('vendor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.master_vendor')),
            ],
        ),
        migrations.AddField(
            model_name='master_barang',
            name='isi_kategori',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.master_kategori'),
        ),
        migrations.AddField(
            model_name='master_barang',
            name='merk',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.master_merk'),
        ),
        migrations.AddField(
            model_name='master_barang',
            name='satuan',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.master_unit'),
        ),
    ]