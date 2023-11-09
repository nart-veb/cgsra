from django.db import models


# Create your models here.

class News(models.Model):
    """Новости"""
    title = models.TextField("Заголовок", blank=True)
    image = models.ImageField("Картинка", upload_to="images/")
    description = models.TextField("Описание", blank=True)
    date = models.DateTimeField("Дата")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"


class Department(models.Model):
    """Отдел"""
    title = models.CharField("Наименование", max_length=50)
    sorting = models.IntegerField("Сортировка")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "отдел"
        verbose_name_plural = "Отделы"


class DepartmentArea(models.Model):
    """Районный отдел"""
    title = models.CharField("Наименование", max_length=50)
    sorting = models.IntegerField("Сортировка")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "районный отдел"
        verbose_name_plural = "Районные отделы"


class People(models.Model):
    """Люди"""
    name = models.CharField("ФИО", max_length=50)
    job_title = models.CharField("Должность", max_length=50)
    phone = models.CharField("Телефон", max_length=50)
    image = models.ImageField("Фото", upload_to="images/employee")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "сотрудника"
        verbose_name_plural = "Люди"


class Employee(models.Model):
    """Сотрудники отделов"""
    people = models.ForeignKey(People, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.people.name)

    class Meta:
        verbose_name = "сотрудника отдела"
        verbose_name_plural = "Сотрудники отдела"


class Management(models.Model):
    """Руководство"""
    people = models.ForeignKey(People, on_delete=models.CASCADE)
    description = models.TextField("Описание", blank=True)
    sorting = models.IntegerField("Сортировка")

    def __str__(self):
        return self.people.name

    class Meta:
        verbose_name = "руководство"
        verbose_name_plural = "Руководство"


class EmployeeArea(models.Model):
    """Сотрудник районного отдела"""
    people = models.ForeignKey(People, on_delete=models.CASCADE)
    department = models.ForeignKey(DepartmentArea, on_delete=models.CASCADE)
    sorting = models.IntegerField("Сортировка")

    def __str__(self):
        return self.people.name

    class Meta:
        verbose_name = "сотрудника районного отдела"
        verbose_name_plural = "Районные сотрудники"


class AbkhaziaNumber(models.Model):
    """Абхазия в цифрах"""
    title = models.CharField("Год", max_length=50)
    file = models.FileField("Файл", upload_to="files")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "год"
        verbose_name_plural = "Абхазия в цифрах"


class ChapterStatistics(models.Model):
    """Сфера статистики"""
    title = models.CharField("Название", max_length=50)
    sorting = models.IntegerField("Сортировка")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "раздел"
        verbose_name_plural = "Официальная статистика (разделы)"


class StatisticsFile(models.Model):
    """Файл статистики"""
    statistic = models.ForeignKey(ChapterStatistics, on_delete=models.CASCADE)
    title = models.CharField("Наименование", max_length=50)
    file = models.FileField("Файл", upload_to="files/statistics")


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "документ"
        verbose_name_plural = "Официальная статистика (документы)"


class ChapterDocument(models.Model):
    """Раздел документов"""
    title = models.CharField("Название", max_length=50)
    sorting = models.IntegerField("Сортировка")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "раздел"
        verbose_name_plural = "Документы (разделы)"


class DocumentFile(models.Model):
    """Документ"""
    statistic = models.ForeignKey(ChapterDocument, on_delete=models.CASCADE)
    title = models.CharField("Наименование", max_length=50)
    file = models.FileField("Файл", upload_to="files/documents")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "документ"
        verbose_name_plural = "Документы"


class ChapterReporting(models.Model):
    """Раздел отчетности"""
    title = models.CharField("Название", max_length=50)
    sorting = models.IntegerField("Сортировка")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "раздел"
        verbose_name_plural = "Отчетность (разделы)"


class ReportingFile(models.Model):
    """Документ отчетности"""
    statistic = models.ForeignKey(ChapterReporting, on_delete=models.CASCADE)
    title = models.CharField("Наименование", max_length=50)
    file = models.FileField("Файл", upload_to="files/documents")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "документ"
        verbose_name_plural = "Отчетность (документы)"


class Video(models.Model):
    """Видео"""
    title = models.TextField("Заголовок", blank=True)
    date = models.DateTimeField("Дата")
    image = models.ImageField("Обложка видео", upload_to="images/")
    video = models.FileField("Видео", upload_to="files/documents")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "видео"
        verbose_name_plural = "Видео"


class ImageModel(models.Model):
    """Видео"""
    title = models.TextField("Заголовок", blank=True)
    date = models.DateTimeField("Дата")
    image = models.ImageField("Обложка записи", upload_to="images/")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "фото"
        verbose_name_plural = "Фото"


class Img(models.Model):
    imagemodel = models.ForeignKey("ImageModel", on_delete=models.CASCADE, related_name="images")
    image = models.ImageField("Картинка", upload_to="images/")






