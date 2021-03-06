# Generated by Django 3.0.8 on 2021-01-05 22:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servicios', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='color',
            old_name='state',
            new_name='estado',
        ),
        migrations.RenameField(
            model_name='talla',
            old_name='state',
            new_name='EstadoTalla',
        ),
        migrations.AlterField(
            model_name='color',
            name='nombrecolor',
            field=models.CharField(blank=True, max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name='color',
            name='numbercolor',
            field=models.CharField(blank=True, max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name='color',
            name='valuecolor',
            field=models.CharField(blank=True, max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name='talla',
            name='nomtalla',
            field=models.CharField(blank=True, max_length=60, null=True),
        ),
    ]
