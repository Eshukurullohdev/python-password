# Generated by Django 5.0.6 on 2024-07-04 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0026_alter_thumbsup_options_cart_unique_id_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Smm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(max_length=200)),
            ],
        ),
    ]
