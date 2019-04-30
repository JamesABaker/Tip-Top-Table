# Generated by Django 2.2 on 2019-04-25 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tmh_db', '0029_funfamstatus_funfam_result'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tmh_residue',
            name='amino_acid_location',
        ),
        migrations.AddField(
            model_name='tmh_residue',
            name='amino_acid_location_in_to_out',
            field=models.IntegerField(default=999),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tmh_residue',
            name='amino_acid_location_n_to_c',
            field=models.IntegerField(default=999),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='tmh_residue',
            name='feature_location',
            field=models.TextField(default='Unknown'),
        ),
    ]