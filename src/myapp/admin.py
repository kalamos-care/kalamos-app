from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from .models import Profile, Insurer, Prescriber, Medication


class CustomModelAdminMixin:

    def __init__(self, model, admin_site):
        self.list_display = [field.name for field in model._meta.fields if field.name != "id"]
        super(CustomModelAdminMixin, self).__init__(model, admin_site)


class ProfileAdmin(ImportExportModelAdmin):
    list_display = ('get_username', 'get_user_email', 'get_user_firstname', 'get_user_lastname', 'phone_number',
                    'get_insurer', 'get_prescriber', 'last_fill_date', 'shopify_id', 'truepill_id',  'created')

    readonly_fields = ('get_user_email', 'get_user_firstname', 'get_user_lastname', 'created', 'updated')


    def get_username(self, obj):
        return obj.user.username
    get_username.short_description = 'Username'
    get_username.admin_order_field = 'user__username'

    def get_user_email(self, obj):
        return obj.user.email
    get_user_email.short_description = 'Email address'
    get_user_email.admin_order_field = 'user__email'

    def get_user_firstname(self, obj):
        return obj.user.first_name
    get_user_firstname.short_description = 'First name'
    get_user_firstname.admin_order_field = 'user__first_name'

    def get_user_lastname(self, obj):
        return obj.user.last_name
    get_user_lastname.short_description = 'Last name'
    get_user_lastname.admin_order_field = 'user__last_name'

    def get_prescriber(self, obj):
        return obj.prescriber.name if obj.prescriber else '-'
    get_prescriber.short_description = 'Prescriber'
    get_prescriber.admin_order_field = 'prescriber__name'

    def get_insurer(self, obj):
        return obj.insurer.name if obj.insurer else '-'
    get_insurer.short_description = 'Insurer'
    get_insurer.admin_order_field = 'insurer__name'

    list_filter = ['medications__name', 'insurer__name', 'prescriber__name']
    search_fields = ('user__email', 'user__username', 'user__first_name', 'insurer__name', 'prescriber__name',
                     'user__last_name', 'shopify_id', 'truepill_id', 'phone_number')

    fieldsets = [
        (None, {'fields': ['user', 'get_user_email', 'get_user_firstname', 'get_user_lastname', 'dob', 'gender',
                           'phone_number']}),

        ('Medications', {
            'fields': [
                'medications',
                'patient_known_allergies',
                'other_medications',
                'last_fill_date',
                'refills_left',
            ]}),

        ('External Links', {
            'fields': [
                'shopify_id',
                'truepill_id',
            ]}),
        ('Insurance', {
            'fields': [
                'insurer',
                'insurance_member_name',
                'insurance_member_id',
            ]}),

        ('Prescriber', {
            'fields': [
                'prescriber',
                'current_pharmacy',
                'current_pharmacy_phone',
            ]}),

        ('Shipping Address', {
            'fields': [
                'address_to_name',
                'address_to_company',
                'address_to_street1',
                'address_to_street2',
                'address_to_city',
                'address_to_state',
                'address_to_zip',
                'address_to_country',
            ]}),

        ('Metadata', {
            # 'classes': ('suit-tab', 'suit-tab-general',),
            'fields': [
                'created',
                'updated',
            ]}),

    ]


class InsurerAdmin(CustomModelAdminMixin, ImportExportModelAdmin):
    pass


class PrescriberAdmin(CustomModelAdminMixin, ImportExportModelAdmin):
    pass


class MedicationAdmin(CustomModelAdminMixin, ImportExportModelAdmin):
    pass


admin.site.register(Profile, ProfileAdmin)
admin.site.register(Insurer, InsurerAdmin)
admin.site.register(Prescriber, PrescriberAdmin)
admin.site.register(Medication, MedicationAdmin)
