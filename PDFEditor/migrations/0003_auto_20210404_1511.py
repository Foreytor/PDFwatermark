# Generated by Django 3.1.7 on 2021-04-04 12:11

import PDFEditor.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PDFEditor', '0002_auto_20210321_1706'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ecp',
            name='pathESP',
            field=models.FileField(upload_to='pathESP/%Y/%m/%d/H/M/S/', validators=[PDFEditor.validators.validate_file_extension], verbose_name='Файл ЭЦП'),
        ),
        migrations.AlterField(
            model_name='wotermark',
            name='pathESP',
            field=models.FileField(blank=True, upload_to='pathESP/%Y/%m/%d/H/M/S/', validators=[PDFEditor.validators.validate_file_extension], verbose_name='Готовый файл'),
        ),
        migrations.AlterField(
            model_name='wotermark',
            name='pathOld',
            field=models.FileField(upload_to='pathOld/%Y/%m/%d/H/M/S/', validators=[PDFEditor.validators.validate_file_extension], verbose_name='Исходный файл'),
        ),
    ]
