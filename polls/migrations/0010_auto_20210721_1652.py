# Generated by Django 3.1.7 on 2021-07-21 14:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0009_paymentdata_user'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='paymentdata',
            options={'ordering': ['user']},
        ),
    ]
