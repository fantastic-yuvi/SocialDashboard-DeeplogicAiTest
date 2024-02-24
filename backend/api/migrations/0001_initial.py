# Generated by Django 5.0.2 on 2024-02-22 13:40

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
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100, unique=True)),
                ('password', models.CharField(max_length=100)),
                ('fb_name', models.CharField(blank=True, max_length=100, null=True)),
                ('ig_name', models.CharField(blank=True, max_length=100, null=True)),
                ('x_name', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]
