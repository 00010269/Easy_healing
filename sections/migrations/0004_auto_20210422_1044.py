# Generated by Django 3.2 on 2021-04-22 05:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sections', '0003_medicine'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Medicine',
        ),
        migrations.AlterField(
            model_name='pharmacy',
            name='phone_number',
            field=models.IntegerField(),
        ),
    ]