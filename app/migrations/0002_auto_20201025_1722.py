# Generated by Django 3.1.2 on 2020-10-25 20:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='conta',
            name='saldo',
            field=models.FloatField(),
        ),
    ]
