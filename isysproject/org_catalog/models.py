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
    contact_person = models.ManyToManyField(Person, verbose_name = "Контактное лицо")
    class Meta:
        verbose_name = "Организация"
        verbose_name_plural = "Организации"


class Address (models.Model):
    composit_adr = madels. Charfield(max_lenght = 200, verbose_name = "Составной Адрес вида (404112, Краснодарский край, Еланский район, Крымковское с.п., ул. Орджоникидзе, стр. 27, оф.544) ")
    short_adr = models.Charfield(max_lenght = 30, blank = True, verbose_name ="Короткий адрес вида (Краснода.Еланский)")
    region = models.Charfield(max_lenght = 30, verbose_name ="Субъект РФ")
    city = models.Charfield(max_lenght = 30, verbose_name = "Город")
    district = models.Charfield(max_lenght = 30, verbose_name ="Район")
    settlement = models.Charfield(max_lenght = 30, verbose_name ="Поселение")
    street = models.Charfield(max_lenght = 30, verbose_name ="Улица")
    structure = models.Charfield(max_lenght = 30, verbose_name ="Строение(Дом)")
    post_index = models.Charfield(max_lenght = 6, verbose_name ="Почтовый индекс")
    class Meta:
        verbose_name = "Адрес"
        verbose_name_plural = "Адреса"

class Phone_number (models.Model):
    number = models.IntegerField(max_lenght = 10, verbose_name = "Номер телефона")
    note = models.Charfield(max_lenght = 150, verbose_name = " Примечание")
    class Meta:
        verbose_name = "Номер телефона"
        verbose_name_plural = "Номера телефонов"
                 
class Email (models.Model):
    name = models.EmailField(verbose_name = "Email")
    email_type = models.Charfield(max_lenght = 20, choises = ((1,"Основной"),(2,"Второстепенный")), verbose_name = "Тип электронного адреса")
    class Meta:
        verbose_name = "Адрес электронной почты"
        verbose_name_plural = "Адреса электронной почты"

class Person (models.Model)
    name = models.Charfield(max_lenght = 30, verbose_name = "Имя")
    middle_name = models.Charfield(max_lenght = 30, verbose_name = "Отчество")
    surname = models.Charfield(max_lenght = 30, verbose_name = "Фамилия")
    mnemo_person_name = models.Charfield(max_lenght = 100, verbose_name = "Мнемокод имени вида (Сергей Сергеевич С.)")
    note = models.Charfield(max_lenght = 150, verbose_name = " Примечание")
    class Meta:
        verbose_name = "Контактное лицо"
        verbose_name_plural = "Контактные лица"
