# Generated by Django 2.2.3 on 2019-07-30 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scale_set', '0024_delete_newmodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='infofields',
            name='age',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='infofields',
            name='special_case',
            field=models.CharField(blank=True, choices=[('vitamin', 'Vitamin'), ('derman', 'Dərman')], max_length=100, null=True),
        ),
    ]
