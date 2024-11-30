# Generated by Django 5.0.2 on 2024-06-06 04:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_notebook'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_added', models.DateTimeField(auto_now_add=True)),
                ('tovar', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.tovar')),
            ],
        ),
    ]