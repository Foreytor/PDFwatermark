# Generated by Django 3.1.7 on 2021-03-21 14:06

import PDFEditor.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PDFEditor', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wotermark',
            name='pathESP',
            field=models.FileField(blank=True, upload_to='pathESP/%Y/%m/%d/', validators=[PDFEditor.validators.validate_file_extension], verbose_name='Готовый файл'),
        ),
        migrations.AlterField(
            model_name='wotermark',
            name='status',
            field=models.CharField(blank=True, max_length=25, verbose_name='Статус'),
        ),
    ]