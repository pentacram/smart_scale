# Generated by Django 2.2.3 on 2019-07-23 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scale_set', '0009_auto_20190723_1606'),
    ]

    operations = [
        migrations.AlterField(
            model_name='infofields',
            name='age',
            field=models.CharField(max_length=255),
        ),
    ]
