# Generated by Django 3.1.7 on 2021-04-19 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_auto_20210413_1701'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='registrationdata',
            name='username',
        ),
        migrations.AlterField(
            model_name='registrationdata',
            name='company',
            field=models.CharField(max_length=100),
        ),
    ]