# Generated by Django 5.0.2 on 2024-06-03 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_expesiv'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notebook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=200)),
                ('cost', models.CharField(max_length=200)),
                ('skitka', models.CharField(max_length=200)),
            ],
        ),
    ]
