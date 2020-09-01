# Generated by Django 3.0.8 on 2020-09-01 05:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servicios', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='producto',
            old_name='cantidadstock',
            new_name='stock',
        ),
        migrations.RemoveField(
            model_name='color',
            name='nomcolor',
        ),
        migrations.RemoveField(
            model_name='color',
            name='numcolor',
        ),
        migrations.RemoveField(
            model_name='color',
            name='value',
        ),
        migrations.RemoveField(
            model_name='producto',
            name='fotosproducts1',
        ),
        migrations.RemoveField(
            model_name='producto',
            name='fotosproducts2',
        ),
        migrations.RemoveField(
            model_name='producto',
            name='fotosproducts3',
        ),
        migrations.RemoveField(
            model_name='producto',
            name='fotosproducts4',
        ),
        migrations.RemoveField(
            model_name='producto',
            name='fotosproducts5',
        ),
        migrations.RemoveField(
            model_name='producto',
            name='fotosproducts6',
        ),
        migrations.RemoveField(
            model_name='producto',
            name='fotosproducts7',
        ),
        migrations.RemoveField(
            model_name='producto',
            name='imagenidcolor',
        ),
        migrations.RemoveField(
            model_name='producto',
            name='photoprincipal',
        ),
        migrations.AddField(
            model_name='color',
            name='imagencolor1',
            field=models.ImageField(blank=True, null=True, upload_to='productos'),
        ),
        migrations.AddField(
            model_name='color',
            name='imagencolor2',
            field=models.ImageField(blank=True, null=True, upload_to='productos'),
        ),
        migrations.AddField(
            model_name='color',
            name='imagencolor3',
            field=models.ImageField(blank=True, null=True, upload_to='productos'),
        ),
        migrations.AddField(
            model_name='color',
            name='imagencolor4',
            field=models.ImageField(blank=True, null=True, upload_to='productos'),
        ),
        migrations.AddField(
            model_name='color',
            name='imagencolor5',
            field=models.ImageField(blank=True, null=True, upload_to='productos'),
        ),
        migrations.AddField(
            model_name='color',
            name='nombrecolor',
            field=models.CharField(blank=True, db_column='nomcolor', max_length=60, null=True),
        ),
        migrations.AddField(
            model_name='color',
            name='numbercolor',
            field=models.CharField(blank=True, db_column='imgnumberColor', max_length=60, null=True),
        ),
        migrations.AddField(
            model_name='color',
            name='valuecolor',
            field=models.CharField(blank=True, db_column='numvaluecolor', max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name='producto',
            name='brevedescripcion',
            field=models.TextField(blank=True, db_column='breveDescripcion', null=True),
        ),
        migrations.AlterField(
            model_name='producto',
            name='descripcion',
            field=models.TextField(blank=True, db_column='Descripcion', null=True),
        ),
        migrations.AlterModelTable(
            name='color',
            table='nombrecolor',
        ),
        migrations.DeleteModel(
            name='Imagenescolor',
        ),
    ]
