# Generated by Django 4.2.1 on 2023-10-11 09:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AbkhaziaNumber',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Год')),
                ('file', models.FileField(upload_to='files', verbose_name='Файл')),
            ],
            options={
                'verbose_name': 'год',
                'verbose_name_plural': 'Абхазия в цифрах',
            },
        ),
        migrations.CreateModel(
            name='ChapterDocument',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Название')),
                ('sorting', models.IntegerField(verbose_name='Сортировка')),
            ],
            options={
                'verbose_name': 'раздел',
                'verbose_name_plural': 'Документы (разделы)',
            },
        ),
        migrations.CreateModel(
            name='ChapterReporting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Название')),
                ('sorting', models.IntegerField(verbose_name='Сортировка')),
            ],
            options={
                'verbose_name': 'раздел',
                'verbose_name_plural': 'Отчетность (разделы)',
            },
        ),
        migrations.CreateModel(
            name='ChapterStatistics',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Название')),
                ('sorting', models.IntegerField(verbose_name='Сортировка')),
            ],
            options={
                'verbose_name': 'раздел',
                'verbose_name_plural': 'Официальная статистика (разделы)',
            },
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Наименование')),
                ('sorting', models.IntegerField(verbose_name='Сортировка')),
            ],
            options={
                'verbose_name': 'отдел',
                'verbose_name_plural': 'Отделы',
            },
        ),
        migrations.CreateModel(
            name='DepartmentArea',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Наименование')),
                ('sorting', models.IntegerField(verbose_name='Сортировка')),
            ],
            options={
                'verbose_name': 'районный отдел',
                'verbose_name_plural': 'Районные отделы',
            },
        ),
        migrations.CreateModel(
            name='ImageModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(blank=True, verbose_name='Заголовок')),
                ('date', models.DateTimeField(verbose_name='Дата')),
                ('image', models.ImageField(upload_to='images/', verbose_name='Обложка записи')),
            ],
            options={
                'verbose_name': 'фото',
                'verbose_name_plural': 'Фото',
            },
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(blank=True, verbose_name='Заголовок')),
                ('image', models.ImageField(upload_to='images/', verbose_name='Картинка')),
                ('description', models.TextField(blank=True, verbose_name='Описание')),
                ('date', models.DateTimeField(verbose_name='Дата')),
            ],
            options={
                'verbose_name': 'Новость',
                'verbose_name_plural': 'Новости',
            },
        ),
        migrations.CreateModel(
            name='People',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='ФИО')),
                ('job_title', models.CharField(max_length=50, verbose_name='Должность')),
                ('phone', models.CharField(max_length=50, verbose_name='Телефон')),
                ('image', models.ImageField(upload_to='images/employee', verbose_name='Фото')),
            ],
            options={
                'verbose_name': 'сотрудника',
                'verbose_name_plural': 'Люди',
            },
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(blank=True, verbose_name='Заголовок')),
                ('date', models.DateTimeField(verbose_name='Дата')),
                ('image', models.ImageField(upload_to='images/', verbose_name='Обложка видео')),
                ('video', models.FileField(upload_to='files/documents', verbose_name='Видео')),
            ],
            options={
                'verbose_name': 'видео',
                'verbose_name_plural': 'Видео',
            },
        ),
        migrations.CreateModel(
            name='StatisticsFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Наименование')),
                ('file', models.FileField(upload_to='files/statistics', verbose_name='Файл')),
                ('statistic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.chapterstatistics')),
            ],
            options={
                'verbose_name': 'документ',
                'verbose_name_plural': 'Официальная статистика (документы)',
            },
        ),
        migrations.CreateModel(
            name='ReportingFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Наименование')),
                ('file', models.FileField(upload_to='files/documents', verbose_name='Файл')),
                ('statistic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.chapterreporting')),
            ],
            options={
                'verbose_name': 'документ',
                'verbose_name_plural': 'Отчетность (документы)',
            },
        ),
        migrations.CreateModel(
            name='Management',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(blank=True, verbose_name='Описание')),
                ('sorting', models.IntegerField(verbose_name='Сортировка')),
                ('people', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.people')),
            ],
            options={
                'verbose_name': 'руководство',
                'verbose_name_plural': 'Руководство',
            },
        ),
        migrations.CreateModel(
            name='Img',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/', verbose_name='Картинка')),
                ('imagemodel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='main.imagemodel')),
            ],
        ),
        migrations.CreateModel(
            name='EmployeeArea',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sorting', models.IntegerField(verbose_name='Сортировка')),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.departmentarea')),
                ('people', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.people')),
            ],
            options={
                'verbose_name': 'сотрудника районного отдела',
                'verbose_name_plural': 'Районные сотрудники',
            },
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.department')),
                ('people', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.people')),
            ],
            options={
                'verbose_name': 'сотрудника отдела',
                'verbose_name_plural': 'Сотрудники отдела',
            },
        ),
        migrations.CreateModel(
            name='DocumentFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Наименование')),
                ('file', models.FileField(upload_to='files/documents', verbose_name='Файл')),
                ('statistic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.chapterdocument')),
            ],
            options={
                'verbose_name': 'документ',
                'verbose_name_plural': 'Документы',
            },
        ),
    ]