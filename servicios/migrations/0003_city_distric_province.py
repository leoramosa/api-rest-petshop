# Generated by Django 3.0.8 on 2020-11-24 22:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('servicios', '0002_categoria_iconcategory'),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=60, null=True)),
                ('delivery', models.CharField(blank=True, max_length=200, null=True)),
                ('costo', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Province',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=60, null=True)),
                ('delivery', models.CharField(blank=True, max_length=200, null=True)),
                ('costo', models.IntegerField(blank=True, null=True)),
                ('statedisponible', models.BooleanField(blank=True, default=True, null=True)),
                ('idcity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='servicios.City')),
            ],
        ),
        migrations.CreateModel(
            name='Distric',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=60, null=True)),
                ('delivery', models.CharField(blank=True, max_length=200, null=True)),
                ('costo', models.IntegerField(blank=True, null=True)),
                ('statedisponible', models.BooleanField(blank=True, default=True, null=True)),
                ('idprovince', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='servicios.Province')),
            ],
        ),
    ]
