# Generated by Django 4.0.2 on 2022-03-08 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mypostgresapp', '0016_vm_vh_class_transport_catg'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vm_vh_class',
            name='transport_catg',
            field=models.CharField(blank=True, max_length=2, null=True),
        ),
    ]
