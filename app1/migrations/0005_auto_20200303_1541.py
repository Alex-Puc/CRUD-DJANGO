# Generated by Django 2.1.15 on 2020-03-03 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0004_auto_20200303_1537'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leccion',
            name='status',
            field=models.IntegerField(blank=True, choices=[(1, 'Disponibles'), (0, 'No Disponible')], null=True),
        ),
    ]