from django.db import models

# Create your models here.

class Address (models.Model):
    composit_adr = models. CharField(max_length = 200, verbose_name = "Составной Адрес вида (404112, Краснодарский край, Еланский район, Крымковское с.п., ул. Орджоникидзе, стр. 27, оф.544) ")
    short_adr = models.CharField(max_length = 30, blank = True, verbose_name ="Короткий адрес вида (Краснода.Еланский)")
    region = models.CharField(max_length = 30, verbose_name ="Субъект РФ")
    city = models.CharField(max_length = 30, blank = True, null = True, verbose_name = "Город")
    district = models.CharField(max_length = 30, verbose_name ="Район")
    settlement = models.CharField(max_length = 30, verbose_name ="Поселение")
    street = models.CharField(max_length = 30, verbose_name ="Улица")
    structure = models.CharField(max_length = 30, verbose_name ="Строение(Дом)")
    post_index = models.CharField(max_length = 6, verbose_name ="Почтовый индекс")
    address_type = models.CharField(max_length = 30, choices = ((1,"Фактический"),(2,"Юридический"),(3,"Почтовый")), verbose_name = "Тип адреса")
    class Meta:
        verbose_name = "Адрес"
        verbose_name_plural = "Адреса"

class Phone_number (models.Model):
    number = models.IntegerField(verbose_name = "Номер телефона")
    note = models.CharField(max_length = 150, verbose_name = " Примечание")
    class Meta:
        verbose_name = "Номер телефона"
        verbose_name_plural = "Номера телефонов"
                 
class Email (models.Model):
    name = models.EmailField(verbose_name = "Email")
    email_type = models.CharField(max_length = 20, choices = ((1,"Основной"),(2,"Второстепенный")), verbose_name = "Тип электронного адреса")
    class Meta:
        verbose_name = "Адрес электронной почты"
        verbose_name_plural = "Адреса электронной почты"

class Person (models.Model):
    name = models.CharField(max_length = 30, verbose_name = "Имя")
    middle_name = models.CharField(max_length = 30, verbose_name = "Отчество")
    surname = models.CharField(max_length = 30, verbose_name = "Фамилия")
    mnemo_person_name = models.CharField(max_length = 100, verbose_name = "Мнемокод имени вида (Сергей Сергеевич С.)")
    note = models.CharField(max_length = 150, verbose_name = " Примечание")
    phone_number = models.ForeignKey(Phone_number, verbose_name = "Номер телефона")
    e_mail = models.ForeignKey(Email, verbose_name = "Адрес электронной почты")
    class Meta:
        verbose_name = "Контактное лицо"
        verbose_name_plural = "Контактные лица"

СATEGORIES_kind_of_economic_activity = (
   (1, "МКУ"),
   (2, "МКУК"),
   (3, "ФБУ"),
   (4, "МБУ"),
   (5, "ООО"),
   (6, "ИП")
)

class Organization(models.Model):
    full_org_name = models.CharField(max_length = 200, verbose_name = "Полное наименование организации")
    short_org_name = models.CharField(max_length = 50, verbose_name = "Краткое(внутреннее) наименование организации")
    mnemo_org_name = models.CharField(max_length = 200, verbose_name = "Мнемокод организации")
    kind_of_economic_activity = models.CharField(max_length = 10, choices = СATEGORIES_kind_of_economic_activity, default = 1, verbose_name = "Вид хозяйственной деятельности")
    address = models.ForeignKey(Address, verbose_name = "Адрес")
    inn = models.IntegerField(verbose_name = "ИНН")
    ogrn = models.IntegerField(verbose_name = "ОГРН")
    kpp = models.IntegerField(verbose_name = "КПП")
    bik = models.IntegerField(verbose_name = "БИК")
    ks = models.IntegerField(verbose_name = "Корреспондентский счет")
    rs = models.IntegerField(verbose_name = "Расчетный счет")
    rs_where = models.CharField(max_length = 150, verbose_name = "Расчетный счет где")
    phone_number = models.ForeignKey(Phone_number, verbose_name = "Номер телефона")
    e_mail = models.ForeignKey(Email, verbose_name = "Адрес электронной почты")
    site = models.URLField(verbose_name = "Адрес действующего интернет сайта")
    note = models.CharField(max_length = 500, verbose_name = "Примечание (комментарии, переговоры)")
    contact_person = models.ManyToManyField(Person, verbose_name = "Контактное лицо")
    class Meta:
        verbose_name = "Организация"
        verbose_name_plural = "Организации"
    def __unicode__(self):
        return self.short_org_name