from django.db import models
from django.contrib.auth.models import User

from .validators import validate_file_extension

class ECP(models.Model):
    pathESP = models.FileField(upload_to='pathESP/%Y/%m/%d/%H/%M/%S/', validators=[validate_file_extension], verbose_name="Файл ЭЦП")
    name = models.CharField(max_length=25, verbose_name="Наименование", blank=True)
    user_main = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Пользователь")

    def __str__(self):
        return self.name


class Wotermark(models.Model):
    user_main = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Пользователь")
    dataAdd = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    dataUpdate = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")
    pathOld = models.FileField(upload_to='pathOld/%Y/%m/%d/%H/%M/%S/', validators=[validate_file_extension], verbose_name="Исходный файл")
    pathNew = models.ForeignKey(ECP, verbose_name="Файл ЭЦП", on_delete=models.CASCADE)
    pathESP = models.FileField(upload_to='pathESP/%Y/%m/%d/%H/%M/%S/', validators=[validate_file_extension], verbose_name="Готовый файл", blank=True)
    status = models.CharField(max_length=25, verbose_name="Статус", blank=True, default="В очереди")


