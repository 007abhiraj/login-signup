# Generated by Django 3.1.5 on 2021-01-12 06:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test_project', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coach',
            name='username',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
