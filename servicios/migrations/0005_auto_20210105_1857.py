# Generated by Django 3.0.8 on 2021-01-05 23:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servicios', '0004_producto_stateportada'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='stateportada',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
