from django.contrib.auth.models import User
from django.contrib.postgres.fields import JSONField
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from django.utils.translation import ugettext as _
from localflavor.us.models import USStateField


GENDER_CHOICES = (
    ('m', 'Male'),
    ('f', 'Female'),
)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    prescriber = models.ForeignKey('Prescriber', verbose_name='Prescriber', related_name='profiles', on_delete=models.CASCADE, null=True)
    insurer = models.ForeignKey('Insurer', verbose_name='Insurer', related_name='profiles', on_delete=models.CASCADE, null=True)
    #profile_id = models.ForeignKey('Insurer', related_name='profiles', on_delete=models.CASCADE)
    shopify_id = models.IntegerField(blank=True, null=True)
    truepill_id = models.IntegerField(blank=True, null=True)
    medications = models.ManyToManyField('Medication', verbose_name='Medications', related_name='profiles', null=True)
    current_pharmacy = models.CharField(max_length=255, blank=True, null=True)
    current_pharmacy_phone = models.CharField(max_length=255, blank=True, null=True)
    dob = models.DateField(max_length=8, blank=True, null=True)
    last_fill_date = models.DateTimeField(blank=True, null=True)
    refills_left = models.IntegerField(blank=True, null=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, blank=True, null=True)
    phone_number = models.CharField(max_length=255, blank=True, null=True)
    address_to_name = models.CharField(_("To name"), max_length=255, blank=True, null=True)
    address_to_company = models.CharField(_("To company"), max_length=255, blank=True, null=True)
    address_to_street1 = models.CharField(_("address"), max_length=255, blank=True, null=True)
    address_to_street2 = models.CharField(_("address cont'd"), max_length=255, blank=True, null=True)
    address_to_city = models.CharField(_("city"), max_length=255, blank=True, null=True)
    address_to_state = USStateField(_("state"), blank=True, null=True)
    address_to_zip = models.CharField(_("zip code"), max_length=10, blank=True, null=True)
    address_to_country = models.CharField(_("country"), max_length=2, default='US', blank=True, null=True)
    insurance_member_name = models.CharField(max_length=255, blank=True, null=True)
    insurance_member_id = models.CharField(max_length=255, blank=True, null=True)
    patient_known_allergies = JSONField(blank=True, null=True)
    other_medications = JSONField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username


class Prescriber(models.Model):
    name = models.CharField(max_length=255)
    npi = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Insurer(models.Model):
    name = models.CharField(max_length=255)
    group_number = models.CharField(max_length=255)
    bin_number = models.CharField(max_length=255)
    pcn_number = models.CharField(max_length=255)
    rx_group_number = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Medication(models.Model):
    name = models.CharField(max_length=255)
    national_code = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
