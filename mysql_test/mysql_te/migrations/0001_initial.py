# Generated by Django 4.1 on 2023-11-09 13:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='sale_M',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shopname', models.CharField(max_length=10)),
                ('call', models.CharField(max_length=20)),
                ('cashier', models.CharField(max_length=10)),
                ('saletime', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='test1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='sale_Date',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('price', models.CharField(max_length=100)),
                ('number', models.DateField()),
                ('Mlink', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mysql_te.sale_m')),
            ],
        ),
    ]