# Generated by Django 5.0.4 on 2024-09-01 10:05

import django.core.validators
import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CasaRural',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
                ('direccion', models.CharField(max_length=255)),
                ('descripcion', models.TextField(blank=True, null=True)),
                ('capacidad', models.PositiveIntegerField()),
                ('numero_habitaciones', models.PositiveIntegerField(blank=True, null=True)),
                ('numero_banos', models.PositiveIntegerField(blank=True, null=True)),
                ('precio_noche', models.DecimalField(decimal_places=2, max_digits=10)),
                ('imagen_url', models.URLField(blank=True, max_length=255, null=True)),
                ('servicios', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
                ('apellidos', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('telefono', models.CharField(blank=True, max_length=20, null=True)),
                ('direccion', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Contacto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_contacto', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('telefono', models.CharField(max_length=15)),
                ('asunto', models.CharField(max_length=100)),
                ('mensaje', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Reserva',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('apellidos', models.CharField(default='Apellido', max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('telefono', models.CharField(max_length=15)),
                ('direccion', models.CharField(max_length=200)),
                ('personas', models.PositiveIntegerField()),
                ('comentario', models.TextField(blank=True, null=True)),
                ('fecha_inicio', models.DateField()),
                ('fecha_fin', models.DateField()),
                ('precio_total', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comentario', models.TextField()),
                ('valoracion', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)])),
                ('fecha', models.DateField(default=django.utils.timezone.now)),
                ('casa_rural', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reservas.casarural')),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reservas.cliente')),
            ],
        ),
        migrations.CreateModel(
            name='Disponibilidad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('disponible', models.BooleanField(default=True)),
                ('casa_rural', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reservas.casarural')),
            ],
        ),
        migrations.CreateModel(
            name='Pago',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_pago', models.DateField(default=django.utils.timezone.now)),
                ('monto', models.DecimalField(decimal_places=2, max_digits=10)),
                ('metodo_pago', models.CharField(blank=True, max_length=50, null=True)),
                ('reserva', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reservas.reserva')),
            ],
        ),
    ]
