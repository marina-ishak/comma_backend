# Generated by Django 4.2.6 on 2023-10-20 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('username', models.CharField(blank=True, max_length=50, null=True)),
                ('password', models.CharField(blank=True, max_length=128, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, unique=True)),
                ('phone', models.CharField(blank=True, max_length=15)),
                ('age', models.PositiveIntegerField(blank=True)),
                ('job', models.CharField(blank=True, max_length=100)),
                ('address', models.TextField(blank=True)),
                ('role', models.CharField(max_length=50)),
                ('national_id', models.CharField(blank=True, max_length=20, null=True, unique=True)),
            ],
        ),
    ]