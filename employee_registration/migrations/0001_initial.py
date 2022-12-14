# Generated by Django 4.1 on 2022-08-14 09:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='EmployeeForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('em_code', models.CharField(max_length=5)),
                ('mobile', models.CharField(max_length=15)),
                ('position', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee_registration.position')),
            ],
        ),
    ]
