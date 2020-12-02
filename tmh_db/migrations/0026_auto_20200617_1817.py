# Generated by Django 3.0.3 on 2020-06-17 18:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tmh_db', '0025_auto_20200615_1605'),
    ]

    operations = [
        migrations.CreateModel(
            name='FunfamResidue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('scorecons', models.FloatField()),
                ('funfam_position', models.IntegerField()),
                ('funfam', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tmh_db.Funfam')),
                ('residue', models.ManyToManyField(to='tmh_db.Residue')),
            ],
            options={
                'unique_together': {('funfam', 'funfam_position')},
            },
        ),
        migrations.DeleteModel(
            name='Funfam_residue',
        ),
    ]