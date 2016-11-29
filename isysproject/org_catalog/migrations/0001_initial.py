# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('composit_adr', models.CharField(max_length=200, verbose_name='Составной Адрес вида (404112, Краснодарский край, Еланский район, Крымковское с.п., ул. Орджоникидзе, стр. 27, оф.544) ')),
                ('short_adr', models.CharField(blank=True, max_length=30, verbose_name='Короткий адрес вида (Краснода.Еланский)')),
                ('region', models.CharField(max_length=30, verbose_name='Субъект РФ')),
                ('city', models.CharField(max_length=30, verbose_name='Город')),
                ('district', models.CharField(max_length=30, verbose_name='Район')),
                ('settlement', models.CharField(max_length=30, verbose_name='Поселение')),
                ('street', models.CharField(max_length=30, verbose_name='Улица')),
                ('structure', models.CharField(max_length=30, verbose_name='Строение(Дом)')),
                ('post_index', models.CharField(max_length=6, verbose_name='Почтовый индекс')),
                ('address_type', models.CharField(choices=[(1, 'Фактический'), (2, 'Юридический'), (3, 'Почтовый')], max_length=30, verbose_name='Тип адреса')),
            ],
            options={
                'verbose_name_plural': 'Адреса',
                'verbose_name': 'Адрес',
            },
        ),
        migrations.CreateModel(
            name='Email',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('name', models.EmailField(max_length=254, verbose_name='Email')),
                ('email_type', models.CharField(choices=[(1, 'Основной'), (2, 'Второстепенный')], max_length=20, verbose_name='Тип электронного адреса')),
            ],
            options={
                'verbose_name_plural': 'Адреса электронной почты',
                'verbose_name': 'Адрес электронной почты',
            },
        ),
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('full_org_name', models.CharField(max_length=200, verbose_name='Полное наименование организации')),
                ('short_org_name', models.CharField(max_length=50, verbose_name='Краткое(внутреннее) наименование организации')),
                ('mnemo_org_name', models.CharField(max_length=200, verbose_name='Мнемокод организации')),
                ('kind_of_economic_activity', models.CharField(choices=[(1, 'МКУ'), (2, 'МКУК'), (3, 'ФБУ'), (4, 'МБУ'), (5, 'ООО'), (6, 'ИП')], default=1, max_length=10, verbose_name='Вид хозяйственной деятельности')),
                ('inn', models.IntegerField(verbose_name='ИНН')),
                ('ogrn', models.IntegerField(verbose_name='ОГРН')),
                ('kpp', models.IntegerField(verbose_name='КПП')),
                ('bik', models.IntegerField(verbose_name='БИК')),
                ('ks', models.IntegerField(verbose_name='Корреспондентский счет')),
                ('rs', models.IntegerField(verbose_name='Расчетный счет')),
                ('rs_where', models.CharField(max_length=150, verbose_name='Расчетный счет где')),
                ('site', models.URLField(verbose_name='Адрес действующего интернет сайта')),
                ('note', models.CharField(max_length=500, verbose_name='Примечание (комментарии, переговоры)')),
                ('address', models.ForeignKey(to='org_catalog.Address', verbose_name='Адрес')),
            ],
            options={
                'verbose_name_plural': 'Организации',
                'verbose_name': 'Организация',
            },
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=30, verbose_name='Имя')),
                ('middle_name', models.CharField(max_length=30, verbose_name='Отчество')),
                ('surname', models.CharField(max_length=30, verbose_name='Фамилия')),
                ('mnemo_person_name', models.CharField(max_length=100, verbose_name='Мнемокод имени вида (Сергей Сергеевич С.)')),
                ('note', models.CharField(max_length=150, verbose_name=' Примечание')),
                ('e_mail', models.ForeignKey(to='org_catalog.Email', verbose_name='Адрес электронной почты')),
            ],
            options={
                'verbose_name_plural': 'Контактные лица',
                'verbose_name': 'Контактное лицо',
            },
        ),
        migrations.CreateModel(
            name='Phone_number',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('number', models.IntegerField(verbose_name='Номер телефона')),
                ('note', models.CharField(max_length=150, verbose_name=' Примечание')),
            ],
            options={
                'verbose_name_plural': 'Номера телефонов',
                'verbose_name': 'Номер телефона',
            },
        ),
        migrations.AddField(
            model_name='person',
            name='phone_number',
            field=models.ForeignKey(to='org_catalog.Phone_number', verbose_name='Номер телефона'),
        ),
        migrations.AddField(
            model_name='organization',
            name='contact_person',
            field=models.ManyToManyField(to='org_catalog.Person', verbose_name='Контактное лицо'),
        ),
        migrations.AddField(
            model_name='organization',
            name='e_mail',
            field=models.ForeignKey(to='org_catalog.Email', verbose_name='Адрес электронной почты'),
        ),
        migrations.AddField(
            model_name='organization',
            name='phone_number',
            field=models.ForeignKey(to='org_catalog.Phone_number', verbose_name='Номер телефона'),
        ),
    ]
