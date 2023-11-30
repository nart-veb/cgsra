from django import forms
from django.contrib import admin
from .models import *
from ckeditor_uploader.widgets import CKEditorUploadingWidget

class NewsAdminForm(forms.ModelForm):
    description = forms.CharField(label="Описание", widget=CKEditorUploadingWidget())
    class Meta:
        model = News
        fields = '__all__'

# Register your models here.
@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    form = NewsAdminForm



class StatisticsAdminForm(forms.ModelForm):
    description = forms.CharField(label="Описание", widget=CKEditorUploadingWidget())
    class Meta:
        model = Statistics
        fields = '__all__'

# Register your models here.
@admin.register(Statistics)
class StatisticsAdmin(admin.ModelAdmin):
    form = StatisticsAdminForm


admin.site.register(Department)
admin.site.register(People)
admin.site.register(Employee)
admin.site.register(Management)
admin.site.register(DepartmentArea)
admin.site.register(EmployeeArea)
admin.site.register(AbkhaziaNumber)
admin.site.register(ReportingFile)
admin.site.register(ChapterReporting)
admin.site.register(ChapterDocument)
admin.site.register(DocumentFile)
admin.site.register(Video)


class ImageModelInline(admin.TabularInline):
    model = Img
    extra = 1

@admin.register(ImageModel)
class ImageModelAdmin(admin.ModelAdmin):
    inlines = [ImageModelInline]

admin.site.register(Img)

