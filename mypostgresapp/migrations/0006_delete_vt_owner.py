# Generated by Django 4.0.2 on 2022-03-08 13:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mypostgresapp', '0005_vt_owner_fk_vh_class_alter_vm_vh_class_code_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='vt_owner',
        ),
    ]
