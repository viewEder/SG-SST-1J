# Generated by Django 3.2.6 on 2021-10-05 01:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import registration.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avatar', models.ImageField(blank=True, null=True, upload_to=registration.models.custom_upload_to)),
                ('biografia', models.TextField(blank=True, verbose_name='Perfil del Usuario')),
                ('personalURL', models.URLField(blank=True, null=True, verbose_name='URL Personal (mipag.com)')),
                ('usuario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Perfil de Usuario',
                'verbose_name_plural': 'Perfiles de Usuario',
                'ordering': ['usuario__username'],
            },
        ),
    ]
