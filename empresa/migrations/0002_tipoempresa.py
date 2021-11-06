# Generated by Django 3.2.6 on 2021-11-06 21:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empresa', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TipoEmpresa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_empresa', models.CharField(max_length=200, verbose_name='Nombre de Tipo de Empresa')),
                ('create_at', models.DateField(auto_now_add=True, null=True, verbose_name='Creado el')),
                ('modify_at', models.DateField(auto_now=True, verbose_name='Actualizado el')),
            ],
            options={
                'verbose_name': 'Tipo de Empresa',
                'verbose_name_plural': 'Tipo de Empresa',
            },
        ),
    ]
