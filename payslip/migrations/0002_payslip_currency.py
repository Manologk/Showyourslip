# Generated by Django 5.0.6 on 2024-06-14 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payslip', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='payslip',
            name='currency',
            field=models.CharField(default='ZMW', max_length=10),
        ),
    ]
