from django.db import models

# Create your models here.
СATEGORIES_kind_of_economic_activity = (
   (1, "МКУ"),
   (2, "МКУК"),
   (3, "ФБУ"),
   (4, "МБУ"),
   (5, "ООО"),
   (6, "ИП")
)


class Organization(models.Model):
	full_org_name = models.Charfield(max_lenght = 200, verbose_name = "Полное наименование организации")
    short_org_name = models.Charfield(max_lenght = 50, verbose_name = "Краткое(внутреннее) наименование организации")
    mnemo_org_name = models.Charfield(max_lenght = 200, verbose_name = "Мнемокод организации")
    kind_of_economic_activity = models.Charfield(max_lenght = 10, choises = СATEGORIES_kind_of_economic_activity, default = 1, verbose_name = "Вид хозяйственной деятельности")
    legal_address = models.OneToOneField(Address, verbose_name = "Юридический адрес")
    post_address = models.OneToOneField(Address, verbose_name = "Почтовый адрес")
    actual_address = models.OneToOneField(Address, verbose_name = "Фактический адрес")
    inn = models.IntegerField(max_lenght = 10, verbose_name = "ИНН")
    ogrn = models.IntegerField(max_lenght = 13, verbose_name = "ОГРН")
    kpp = models.IntegerField(max_lenght = 9, verbose_name = "КПП")
    bik = models.IntegerField(max_lenght = 8, verbose_name = "БИК")
    ks = models.IntegerField(max_lenght = 20, verbose_name = "Корреспондентский счет")
    rs = models.IntegerField(max_lenght = 20, verbose_name = "Расчетный счет")
    rs_where = models.Charfield(max_lenght = 150, verbose_name = "Расчетный счет где")
    phone_number = models.ForeignKey(Phone_number, verbose_name = "Номер телефона")
    e_mail = models.ForeignKey(Email, verbose_name = "Адрес электронной почты")
    site = models.URLField(verbose_name = "Адрес действующего интернет сайта")
    note = models.Charfield(verbose_name = "Примечание (комментарии, переговоры)")
    contact_person
    class Meta:
        verbose_name = "Организация"
        verbose_name_plural = "Организации"


class Address (models.Model):
    short_adress
    region
    district
    settlement
    street
    structure
    index

class Phone_number (models.Model):
    number = models.IntegerField(max_lenght = 10, verbose_name = "Номер телефона")
    note = models.Charfield(max_lenght = 150, verbose_name = " Примечание")
                 
class Email (models.Model):
    name = models.EmailField(verbose_name = "Email")
    email_type = models.Charfield(max_lenght = 20, choises = ((1,"Основной"),(2,"Второстепенный")), verbose_name = "Тип электронного адреса")

class Person (models.Model)
    name = models.Charfield(max_lenght = 30, verbose_name = "")
    middle_name
    surname
    mnemo_person_name
