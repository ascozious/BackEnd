# Generated by Django 2.1.1 on 2018-12-01 07:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_auto_20181201_1424'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='inven_detail',
            name='barcode',
        ),
        migrations.RemoveField(
            model_name='inven_detail',
            name='kategori',
        ),
        migrations.RemoveField(
            model_name='inven_detail',
            name='satuan',
        ),
    ]