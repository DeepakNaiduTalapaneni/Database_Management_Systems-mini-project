# Generated by Django 3.2.9 on 2022-02-01 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pmapp', '0010_alter_project_deadline'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='deadline',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='last_updated',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
