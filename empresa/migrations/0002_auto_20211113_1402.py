# Generated by Django 3.2.7 on 2021-11-13 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empresa', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cargos',
            name='create_at',
        ),
        migrations.RemoveField(
            model_name='cargos',
            name='modify_at',
        ),
        migrations.AlterField(
            model_name='cargos',
            name='salario_cargo',
            field=models.IntegerField(default=0, verbose_name='Salario'),
        ),
    ]