# Generated by Django 4.1.2 on 2022-12-06 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('docentes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='docente',
            name='correo',
            field=models.EmailField(max_length=80, verbose_name='Correo Electrónico'),
        ),
        migrations.AlterField(
            model_name='docente',
            name='genero',
            field=models.CharField(choices=[('MASCULINO', 'Masculino'), ('FEMENINO', 'Femenino'), ('INDEFINIDO', 'Indefinido')], default='MASCULINO', max_length=20, verbose_name='Género'),
        ),
    ]
