# Generated by Django 4.2.2 on 2023-07-04 00:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0002_propiedades_propietario_alter_documento_descripcion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='documento',
            name='anio',
            field=models.IntegerField(db_column='anio', default=2023),
        ),
        migrations.AlterField(
            model_name='propiedades',
            name='rol',
            field=models.CharField(db_column='rol', max_length=10),
        ),
        migrations.AlterField(
            model_name='propiedades',
            name='rut',
            field=models.CharField(db_column='rut', default='111111111', max_length=10),
        ),
        migrations.AlterField(
            model_name='propietario',
            name='fono',
            field=models.CharField(db_column='fono', default='5695555555', max_length=10),
        ),
    ]