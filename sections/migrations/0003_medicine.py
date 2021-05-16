# Generated by Django 3.2 on 2021-04-22 04:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sections', '0002_alter_pharmacy_table'),
    ]

    operations = [
        migrations.CreateModel(
            name='Medicine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1024)),
                ('shape', models.CharField(choices=[('pill', 'pill'), ('kapsula', 'kapsula'), ('gel', 'gel'), ('ampula', 'ampula')], max_length=256)),
            ],
            options={
                'db_table': 'medicine',
            },
        ),
    ]
