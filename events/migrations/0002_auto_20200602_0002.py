# Generated by Django 3.0.6 on 2020-06-01 18:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='event_date',
            field=models.DateField(default=datetime.date(2020, 6, 2)),
        ),
    ]