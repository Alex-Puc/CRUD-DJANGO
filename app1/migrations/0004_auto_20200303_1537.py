# Generated by Django 2.1.15 on 2020-03-03 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0003_leccion_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leccion',
            name='status',
            field=models.IntegerField(blank=True, choices=[('Disponible', 'Disponible'), ('No Disponible', 'No Disponible')], null=True),
        ),
    ]
