# Generated by Django 3.2.7 on 2021-11-22 01:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Areas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_area', models.CharField(max_length=255, verbose_name='Nombre Area')),
                ('create_at', models.DateField(auto_now_add=True, null=True, verbose_name='Creado el')),
                ('modify_at', models.DateField(auto_now=True, verbose_name='Actualizado el')),
            ],
            options={
                'verbose_name': 'Nombre Area',
                'verbose_name_plural': 'Areas de la empresa',
            },
        ),
        migrations.CreateModel(
            name='Capacitaciones',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Cargos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cargo', models.CharField(max_length=255, verbose_name='Cargo')),
                ('salario_cargo', models.IntegerField(default=0, verbose_name='Salario')),
                ('create_at', models.DateField(auto_now_add=True, null=True, verbose_name='Creado el')),
                ('modify_at', models.DateField(auto_now=True, verbose_name='Actualizado el')),
            ],
            options={
                'verbose_name': 'Cargo',
                'verbose_name_plural': 'Cargos',
            },
        ),
        migrations.CreateModel(
            name='NivelAcademico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nivel', models.CharField(max_length=255, verbose_name='Nivel Académico')),
                ('create_at', models.DateField(auto_now_add=True, null=True, verbose_name='Creado el')),
                ('modify_at', models.DateField(auto_now=True, verbose_name='Actualizado el')),
            ],
            options={
                'verbose_name': 'Nivel Académico',
                'verbose_name_plural': 'Niveles Académicos',
            },
        ),
        migrations.CreateModel(
            name='Responsabilidades',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('responsabilidad', models.TextField(blank=True, null=True, verbose_name='Responsabilidad')),
                ('create_at', models.DateField(auto_now_add=True, null=True, verbose_name='Creado el')),
                ('modify_at', models.DateField(auto_now=True, verbose_name='Actualizado el')),
            ],
            options={
                'verbose_name': 'Responsabiliad',
                'verbose_name_plural': 'Responsabiliades',
            },
        ),
        migrations.CreateModel(
            name='Sanidad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('enfermedad', models.CharField(max_length=255, verbose_name='Tipo de Enfermedad')),
                ('pandemia', models.CharField(choices=[('Si', 'Si'), ('No', 'No')], max_length=255, verbose_name='Es Pandemia?')),
                ('create_at', models.DateField(auto_now_add=True, verbose_name='Creado el')),
                ('modify_at', models.DateField(auto_now=True, verbose_name='Actualizado el')),
            ],
            options={
                'verbose_name': 'Sanidad (COVID-19 u otras)',
                'verbose_name_plural': 'Sanidades (COVID-19 u otras)',
            },
        ),
        migrations.CreateModel(
            name='TipoEmpresa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_empresa', models.CharField(max_length=200, verbose_name='Tipo de Empresa')),
                ('create_at', models.DateField(auto_now_add=True, null=True, verbose_name='Creado el')),
                ('modify_at', models.DateField(auto_now=True, verbose_name='Actualizado el')),
            ],
            options={
                'verbose_name': 'Tipo de Empresa',
                'verbose_name_plural': 'Tipo de Empresa',
            },
        ),
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200, verbose_name='Nombre de Empresa')),
                ('nit', models.CharField(max_length=15, verbose_name='NIT')),
                ('actividad', models.CharField(max_length=255, verbose_name='Actividad Económica')),
                ('nivel_riesgo', models.CharField(max_length=255, verbose_name='Nivel de Riesgo')),
                ('direccion', models.CharField(max_length=255, verbose_name='Dirección')),
                ('ciudad', models.CharField(blank=True, max_length=255, null=True, verbose_name='Ciudad')),
                ('departamento', models.CharField(blank=True, max_length=255, null=True, verbose_name='Departamento')),
                ('naturaleza_empresa', models.CharField(max_length=100, verbose_name='Naturaleza jurídica')),
                ('telefonos', models.CharField(max_length=40, verbose_name='Teléfonos de contacto')),
                ('correo', models.EmailField(max_length=255, verbose_name='Correo electrónico')),
                ('create_at', models.DateField(auto_now_add=True, null=True, verbose_name='Creado el')),
                ('modify_at', models.DateField(auto_now=True, verbose_name='Actualizado el')),
                ('tipo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='empresa.tipoempresa', verbose_name='Tipo Empresa')),
            ],
            options={
                'verbose_name': 'Empresa',
                'verbose_name_plural': 'Empresa',
            },
        ),
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo_empleado', models.CharField(max_length=20, verbose_name='Código de Empleado')),
                ('fecha_ingreso', models.DateField(verbose_name='Fecha de ingreso')),
                ('salario_basico', models.DecimalField(decimal_places=2, max_digits=12, verbose_name='Salario')),
                ('arl', models.CharField(max_length=100, verbose_name='ARL')),
                ('ssp', models.CharField(max_length=100, verbose_name='EPS')),
                ('sss', models.CharField(max_length=100, verbose_name='Fondo Pensiones')),
                ('ccf', models.CharField(default='N/A', max_length=100, verbose_name='Caja de Compensación')),
                ('sufre_enfermedad', models.CharField(choices=[('Si', 'Si'), ('No', 'No')], max_length=255, null=True, verbose_name='Sufre Alguna Enfermedad')),
                ('cual_enfermedad', models.CharField(default='N/A', max_length=255, verbose_name='Que enfermedad Sufre?')),
                ('toma_medicamentos', models.CharField(choices=[('Si', 'Si'), ('No', 'No')], max_length=255, null=True, verbose_name='Toma Medicamentos?')),
                ('cual_medicamento', models.CharField(default='N/A', max_length=255, null=True, verbose_name='Que Medicamento toma?')),
                ('tipo_contrato', models.CharField(choices=[('Fijo', 'Fijo'), ('Indefinido', 'Indefinido'), ('Obra Labor', 'Obra Labor'), ('Otro', 'Otro')], max_length=255, null=True, verbose_name='Tipo Contrato')),
                ('cuenta_bancaria', models.CharField(max_length=20, verbose_name='Número de cuenta')),
                ('barrio', models.CharField(max_length=255, null=True, verbose_name='Barrio')),
                ('ciudad', models.CharField(max_length=255, null=True, verbose_name='Ciudad')),
                ('departamento', models.CharField(max_length=255, null=True, verbose_name='Departamento')),
                ('estrato', models.IntegerField(blank=True, null=True, verbose_name='Estrato')),
                ('fecha_retiro', models.DateField(null=True, verbose_name='Fecha de Retiro')),
                ('create_at', models.DateField(auto_now_add=True, null=True, verbose_name='Creado el')),
                ('modify_at', models.DateField(auto_now=True, null=True, verbose_name='Actualizado el')),
                ('area', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='empresa.areas')),
                ('cargo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='empresa.cargos')),
                ('nivel_academico', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='empresa.nivelacademico')),
            ],
            options={
                'verbose_name': 'Empleado',
                'verbose_name_plural': 'Empleados',
            },
        ),
        migrations.CreateModel(
            name='DetalleSanidad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vacuna', models.CharField(max_length=144, verbose_name='Vacuna')),
                ('dosis', models.IntegerField(blank=True, null=True, verbose_name='Número Dosis')),
                ('fecha_dosis', models.DateField(verbose_name='Fecha de aplicación')),
                ('create_at', models.DateField(auto_now_add=True, verbose_name='Creado el')),
                ('modify_at', models.DateField(auto_now=True, verbose_name='Actualizado el')),
                ('empleado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='empresa.empleado')),
            ],
            options={
                'verbose_name': 'Detalle Tratamiento',
                'verbose_name_plural': 'Detalle Tratamientos',
            },
        ),
        migrations.AddField(
            model_name='areas',
            name='empresa',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='empresa.empresa'),
        ),
    ]
