# Generated by Django 2.0.6 on 2018-07-06 16:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0004_auto_20180706_1602'),
        ('productos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='botas',
            name='producto',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='inventario.Productos'),
            preserve_default=False,
        ),
    ]
