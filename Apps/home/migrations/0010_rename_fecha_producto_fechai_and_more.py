# Generated by Django 4.1.1 on 2022-09-29 05:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_rename_fechai_producto_fecha_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='producto',
            old_name='fecha',
            new_name='fechaI',
        ),
        migrations.RenameField(
            model_name='producto',
            old_name='nombre',
            new_name='nombreP',
        ),
    ]
