# Generated by Django 3.1.5 on 2021-06-21 22:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tmh_db', '0035_auto_20210413_1141'),
    ]

    operations = [
        migrations.AlterField(
            model_name='structural_residue',
            name='pdb_position',
            field=models.FloatField(),
        ),
    ]
