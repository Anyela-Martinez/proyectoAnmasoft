# Generated by Django 4.1.2 on 2022-12-06 18:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('usuarios', '0001_initial'),
        ('docentes', '0001_initial'),
        ('grado', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreCurso', models.CharField(max_length=20, verbose_name='Nombre Curso')),
                ('numCurso', models.CharField(max_length=40, verbose_name='Número Curso')),
                ('estado', models.CharField(choices=[('1', 'Activo'), ('0', 'Inactivo')], default='1', max_length=1, verbose_name='Estado')),
                ('docente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='docentes.docente', verbose_name='Docente')),
                ('grado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='grado.grado', verbose_name='Grado')),
                ('usuario', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='usuarios.usuario', verbose_name='Usuario')),
            ],
        ),
    ]
