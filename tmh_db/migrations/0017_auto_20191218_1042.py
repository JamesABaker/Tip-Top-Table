# Generated by Django 2.2.5 on 2019-12-18 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tmh_db', '0016_auto_20191217_1613'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='uniref',
            name='representative_id',
        ),
        migrations.AddField(
            model_name='uniref',
            name='representative_uniprot_code',
            field=models.CharField(default='x', max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='uniref',
            name='representative_uniref_code',
            field=models.CharField(default='x', max_length=50),
            preserve_default=False,
        ),
    ]