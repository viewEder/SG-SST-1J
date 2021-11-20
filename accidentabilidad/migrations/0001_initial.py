# Generated by Django 3.2.7 on 2021-11-20 21:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('empresa', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='AgenteAccidente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=250, null=True, verbose_name='Nombre')),
                ('created_at', models.DateField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('updated_at', models.DateField(auto_now=True, verbose_name='Fecha de actualizacion')),
                ('status', models.BooleanField(default=False, verbose_name='Estado')),
            ],
            options={
                'verbose_name': 'Agente de Accidente',
                'verbose_name_plural': 'Agentes de Accidentes',
            },
        ),
        migrations.CreateModel(
            name='CausaBasica',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=250, null=True, verbose_name='Nombre')),
                ('created_at', models.DateField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('updated_at', models.DateField(auto_now=True, verbose_name='Fecha de actualizacion')),
                ('status', models.BooleanField(default=False, verbose_name='Estado')),
            ],
            options={
                'verbose_name': 'Causa Basica',
                'verbose_name_plural': 'Causas Basicas',
            },
        ),
        migrations.CreateModel(
            name='CausaInmediata',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=250, null=True, verbose_name='Nombre')),
                ('created_at', models.DateField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('updated_at', models.DateField(auto_now=True, verbose_name='Fecha de actualizacion')),
                ('status', models.BooleanField(default=False, verbose_name='Estado')),
            ],
            options={
                'verbose_name': 'Causa Inmediata',
                'verbose_name_plural': 'Causas Inmediatas',
            },
        ),
        migrations.CreateModel(
            name='MecanismoAccidente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=250, null=True, verbose_name='Nombre')),
                ('created_at', models.DateField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('updated_at', models.DateField(auto_now=True, verbose_name='Fecha de actualizacion')),
                ('status', models.BooleanField(default=False, verbose_name='Estado')),
            ],
            options={
                'verbose_name': 'Mecanismo de Accidente',
                'verbose_name_plural': 'Mecanismos de Accidentes',
            },
        ),
        migrations.CreateModel(
            name='ParteDelCuerpo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=250, null=True, verbose_name='Nombre')),
                ('created_at', models.DateField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('updated_at', models.DateField(auto_now=True, verbose_name='Fecha de actualizacion')),
                ('status', models.BooleanField(default=False, verbose_name='Estado')),
            ],
            options={
                'verbose_name': 'Parte del Cuerpo',
                'verbose_name_plural': 'Partes del Cuerpo',
            },
        ),
        migrations.CreateModel(
            name='Peligro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=250, null=True, verbose_name='Nombre')),
                ('created_at', models.DateField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('updated_at', models.DateField(auto_now=True, verbose_name='Fecha de actualizacion')),
                ('status', models.BooleanField(default=False, verbose_name='Estado')),
            ],
            options={
                'verbose_name': 'Peligro',
                'verbose_name_plural': 'Peligros',
            },
        ),
        migrations.CreateModel(
            name='TipoAccidente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=250, null=True, verbose_name='Nombre')),
                ('created_at', models.DateField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('updated_at', models.DateField(auto_now=True, verbose_name='Fecha de actualizacion')),
                ('status', models.BooleanField(default=False, verbose_name='Estado')),
            ],
            options={
                'verbose_name': 'Tipo de Accidente',
                'verbose_name_plural': 'Tipos de Accidentes',
            },
        ),
        migrations.CreateModel(
            name='TipoLeccion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=250, null=True, verbose_name='Nombre')),
                ('created_at', models.DateField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('updated_at', models.DateField(auto_now=True, verbose_name='Fecha de actualizacion')),
                ('status', models.BooleanField(default=False, verbose_name='Estado')),
            ],
            options={
                'verbose_name': 'Tipo de Leccion',
                'verbose_name_plural': 'Tipos de Lecciones',
            },
        ),
        migrations.CreateModel(
            name='Accidentabilidad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='Fecha')),
                ('cie10', models.CharField(blank=True, max_length=250, null=True, verbose_name='Cie 10')),
                ('diagnosis', models.CharField(blank=True, max_length=255, null=True, verbose_name='Diagnóstico')),
                ('inability_days', models.IntegerField(blank=True, default=0, null=True, verbose_name='Dias de incapacidad')),
                ('intervention_measure', models.CharField(blank=True, max_length=255, null=True, verbose_name='Medida intervención')),
                ('compliance', models.IntegerField(blank=True, default=0, null=True, verbose_name='Cumplimiento')),
                ('accident_description', models.TextField(blank=True, max_length=255, null=True, verbose_name='Descripcion accidente')),
                ('created_at', models.DateField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('updated_at', models.DateField(auto_now=True, verbose_name='Fecha de actualizacion')),
                ('status', models.BooleanField(default=False, verbose_name='Estado')),
                ('accident_agent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='accidentabilidad.agenteaccidente', verbose_name='Agente accidente')),
                ('accident_mechanism', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='accidentabilidad.mecanismoaccidente', verbose_name='Mecanismo del accidente')),
                ('accident_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='accidentabilidad.tipoaccidente', verbose_name='Tipo accidente')),
                ('basic_cause', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='accidentabilidad.causabasica', verbose_name='Causa basica')),
                ('empleado', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='empresa.empleado', verbose_name='Empleado')),
                ('immediate_cause', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='accidentabilidad.causainmediata', verbose_name='Causa inmediata')),
                ('lesion_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='accidentabilidad.tipoleccion', verbose_name='Tipo lección')),
                ('part_body_affected', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='accidentabilidad.partedelcuerpo', verbose_name='Parte afectada')),
                ('peligro', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='accidentabilidad.peligro', verbose_name='Peligro')),
            ],
            options={
                'verbose_name': 'Accidentabilidad',
                'verbose_name_plural': 'Accidentabilidades',
            },
        ),
    ]
