# Generated by Django 4.1 on 2022-11-18 13:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tractor',
            fields=[
                ('tractor_id', models.AutoField(primary_key=True, serialize=False)),
                ('tractor_name', models.CharField(default=1, max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Farmer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('farmer_name', models.CharField(max_length=50)),
                ('farmer_addr', models.CharField(max_length=50)),
                ('tractor_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='krishikhojapp.tractor')),
            ],
        ),
    ]