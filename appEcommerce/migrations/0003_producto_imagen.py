# Generated by Django 5.0.1 on 2024-01-11 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appEcommerce', '0002_producto_precio'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='productos/'),
        ),
    ]
