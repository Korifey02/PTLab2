# Generated by Django 5.1.3 on 2024-11-26 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='rest',
            field=models.PositiveIntegerField(default=5),
        ),
    ]
