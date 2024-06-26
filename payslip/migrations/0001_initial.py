# Generated by Django 5.0.6 on 2024-06-20 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Payslip',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_title', models.CharField(max_length=100)),
                ('net_salary', models.DecimalField(decimal_places=2, max_digits=10)),
                ('currency', models.CharField(default='ZMW', max_length=10)),
                ('other_info', models.TextField(blank=True, null=True)),
                ('employment_type', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
                ('file', models.FileField(blank=True, null=True, upload_to='payslips/')),
                ('upload_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
