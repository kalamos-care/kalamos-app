# Generated by Django 2.2.1 on 2019-11-27 19:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import localflavor.us.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Insurer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('group_number', models.CharField(max_length=255)),
                ('bin_number', models.CharField(max_length=255)),
                ('pcn_number', models.CharField(max_length=255)),
                ('rx_group_number', models.CharField(max_length=255)),
                ('phone_number', models.CharField(max_length=255)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Medication',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('national_code', models.CharField(max_length=255)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Prescriber',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('npi', models.CharField(max_length=255)),
                ('phone_number', models.CharField(max_length=255)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shopify_id', models.IntegerField(default=0)),
                ('truepill_id', models.IntegerField(default=0)),
                ('current_pharmacy', models.CharField(max_length=255)),
                ('current_pharmacy_phone', models.CharField(max_length=255)),
                ('dob', models.DateField(max_length=8)),
                ('last_fill_date', models.DateTimeField()),
                ('refills_left', models.IntegerField()),
                ('gender', models.CharField(max_length=255)),
                ('phone_number', models.CharField(max_length=255)),
                ('address_to_name', models.CharField(max_length=255, verbose_name='name')),
                ('address_to_company', models.CharField(blank=True, max_length=255, verbose_name='company')),
                ('address_to_street1', models.CharField(max_length=255, verbose_name='address')),
                ('address_to_street2', models.CharField(blank=True, max_length=255, verbose_name="address cont'd")),
                ('address_to_city', models.CharField(max_length=255, verbose_name='city')),
                ('address_to_state', localflavor.us.models.USStateField(max_length=2, verbose_name='state')),
                ('address_to_zip', models.CharField(max_length=10, verbose_name='zip code')),
                ('address_to_country', models.CharField(default='US', max_length=2, verbose_name='country')),
                ('insurance_member_name', models.CharField(max_length=255)),
                ('insurance_member_id', models.CharField(max_length=255)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('insurer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='profiles', to='myapp.Insurer')),
                ('medications', models.ManyToManyField(related_name='profiles', to='myapp.Medication')),
                ('prescriber', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='profiles', to='myapp.Prescriber')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]