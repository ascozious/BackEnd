# Generated by Django 2.1.1 on 2018-11-28 06:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20181128_1331'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='master_barang',
            name='merk',
        ),
        migrations.AddField(
            model_name='master_barang',
            name='merk',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.master_merk'),
        ),
    ]
