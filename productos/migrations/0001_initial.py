# Generated by Django 2.0.6 on 2018-07-06 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Botas',
            fields=[
                ('color', models.CharField(blank=True, max_length=100)),
                ('size', models.CharField(blank=True, max_length=100)),
                ('cantidad', models.IntegerField(blank=True, null=True)),
                ('precio', models.DecimalField(decimal_places=2, max_digits=6)),
                ('estilo', models.CharField(blank=True, max_length=100)),
                ('genero', models.CharField(blank=True, choices=[('Hombre', 'H'), ('Mujer', 'M'), ('Unisex', 'U')], max_length=100)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
