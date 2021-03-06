# Generated by Django 2.2.1 on 2019-12-01 05:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_auto_20191201_0551'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='dob',
            field=models.DateField(blank=True, max_length=8, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='last_fill_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='refills_left',
            field=models.IntegerField(),
        ),
    ]
