# Generated by Django 3.1.7 on 2021-04-10 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PDFEditor', '0005_auto_20210410_1752'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wotermark',
            name='status',
            field=models.CharField(blank=True, default='В очереди', max_length=25, verbose_name='Статус'),
        ),
    ]
