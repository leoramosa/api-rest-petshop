# Generated by Django 3.0.8 on 2020-10-26 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servicios', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='categoria',
            name='iconcategory',
            field=models.ImageField(blank=True, null=True, upload_to='productos'),
        ),
    ]
