# Generated by Django 4.0.2 on 2022-03-05 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mypostgresapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vt_owner',
            name='regn_dt',
            field=models.DateField(),
        ),
    ]
