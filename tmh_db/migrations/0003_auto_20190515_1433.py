# Generated by Django 2.2 on 2019-05-15 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tmh_db', '0002_auto_20190510_1254'),
    ]

    operations = [
        migrations.AlterField(
            model_name='structure',
            name='pdb_id',
            field=models.CharField(default='', max_length=10, unique=True),
        ),
    ]