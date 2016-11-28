from django.db import models

# Create your models here.
class Organization(models.Model):
	kind_of_economic_activity
    org_name
    short_org_name
    mnemo_org_name
    legal_address
    post_address
    actual_address
    requisites
        inn
        ogrn
        kpp
        bik
        ks
        rs
        rs_where
    phone_number
    e_mail
    site
    contact_person


class Address (models.Model):
    short_adress
    region
    district
    settlement
    street
    structure
    index

class Phone_number (models.Model):
    number
