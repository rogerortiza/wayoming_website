# Generated by Django 2.0.6 on 2018-07-06 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0002_botas_producto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='botas',
            name='genero',
            field=models.CharField(blank=True, choices=[('H', 'Hombre'), ('M', 'Mujer'), ('U', 'Unisex')], max_length=100),
        ),
    ]
