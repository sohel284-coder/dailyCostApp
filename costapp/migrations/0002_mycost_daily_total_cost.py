# Generated by Django 4.0.3 on 2022-04-09 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('costapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='mycost',
            name='daily_total_cost',
            field=models.PositiveIntegerField(default=0),
        ),
    ]