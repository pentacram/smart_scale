# Generated by Django 2.2.3 on 2019-07-24 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scale_set', '0011_infofields_publish_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='infofields',
            name='publish_date',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]
