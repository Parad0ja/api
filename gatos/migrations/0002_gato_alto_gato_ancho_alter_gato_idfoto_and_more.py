# Generated by Django 4.2.4 on 2023-08-03 01:46

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('gatos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='gato',
            name='alto',
            field=models.CharField(default=django.utils.timezone.now, max_length=5000, verbose_name='alto'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='gato',
            name='ancho',
            field=models.CharField(default=7.46, max_length=5000, verbose_name='ancho'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='gato',
            name='idfoto',
            field=models.CharField(max_length=10, verbose_name='foto'),
        ),
        migrations.AlterField(
            model_name='gato',
            name='url',
            field=models.CharField(max_length=250, verbose_name='urlgato'),
        ),
    ]
