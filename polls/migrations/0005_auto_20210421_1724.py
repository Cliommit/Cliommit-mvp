# Generated by Django 3.1.7 on 2021-04-21 15:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0004_auto_20210419_1817'),
    ]

    operations = [
        migrations.CreateModel(
            name='AccountDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account_name', models.CharField(default='Null', max_length=100)),
                ('bank_name', models.CharField(default='Null', max_length=100)),
                ('bic', models.CharField(default='Null', max_length=100)),
                ('iban', models.CharField(default='Null', max_length=100)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.registrationdata')),
            ],
            options={
                'ordering': ['user'],
            },
        ),
        migrations.DeleteModel(
            name='Choice',
        ),
        migrations.DeleteModel(
            name='Question',
        ),
    ]