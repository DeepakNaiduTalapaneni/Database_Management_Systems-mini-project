# Generated by Django 3.2.9 on 2022-02-01 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pmapp', '0011_auto_20220201_1519'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='last_updated',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
