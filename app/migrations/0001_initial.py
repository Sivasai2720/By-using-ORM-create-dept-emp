# Generated by Django 4.2.7 on 2024-01-30 08:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dept',
            fields=[
                ('deptno', models.IntegerField(primary_key=True, serialize=False)),
                ('dname', models.CharField(max_length=100)),
                ('dlocation', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='SalGrade',
            fields=[
                ('grade', models.IntegerField(primary_key=True, serialize=False)),
                ('lowsal', models.DecimalField(decimal_places=2, max_digits=7)),
                ('highsal', models.DecimalField(decimal_places=2, max_digits=7)),
            ],
        ),
        migrations.CreateModel(
            name='Emp',
            fields=[
                ('empno', models.IntegerField(primary_key=True, serialize=False)),
                ('ename', models.CharField(max_length=80)),
                ('job', models.CharField(max_length=150)),
                ('hiredate', models.DateField()),
                ('sal', models.DecimalField(decimal_places=2, max_digits=7)),
                ('comm', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('deptno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.dept')),
                ('mgr', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.emp')),
            ],
        ),
    ]
