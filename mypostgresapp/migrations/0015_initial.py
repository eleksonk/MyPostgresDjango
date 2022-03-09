# Generated by Django 4.0.2 on 2022-03-08 13:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('mypostgresapp', '0014_remove_vt_owner_vh_class_delete_vm_vh_class_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='vm_vh_class',
            fields=[
                ('code', models.IntegerField(default=0, primary_key=True, serialize=False)),
                ('descr', models.CharField(default='NA', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='vt_owner',
            fields=[
                ('regn_no', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('owner_name', models.CharField(max_length=35)),
                ('regn_dt', models.DateField()),
                ('no_cyl', models.IntegerField()),
                ('vh_class', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='mypostgresapp.vm_vh_class')),
            ],
        ),
    ]
