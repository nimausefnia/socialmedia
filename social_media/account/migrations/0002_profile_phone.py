# Generated by Django 3.2.4 on 2021-07-31 03:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='phone',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]