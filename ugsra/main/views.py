from django.shortcuts import render
from django.views.generic.base import View
from django.views.generic import ListView, DetailView
from .models import *
from itertools import chain


class IndexView(View):
    # главная страница
    def get(self, request):
        news = list(chain(News.objects.order_by('date')[:6], News.objects.order_by('date')[:3]))
        statistics = Statistics.objects.filter(status_pay=True)
        context = {
            "news_list": news,
            "statistics_list": statistics,
        }
        return render(request, 'ugsra/index.html', context)


class ListNews(ListView):
    template_name = 'ugsra/news/news_list.html'
    context_object_name = 'news_list'

    def get_queryset(self):
        return News.objects.order_by("-date")


class DetailNews(DetailView):
    model = News
    template_name = 'ugsra/news/news_detail.html'
    context_object_name = 'news'
    pk_url_kwarg = 'news_id'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class ReportingView(View):
    def get(self, request):
        return render(request, 'ugsra/reporting.html')


class ListManagement(ListView):
    template_name = 'ugsra/management/management_list.html'
    context_object_name = 'management_list'

    def get_queryset(self):
        return Management.objects.order_by("sorting")


class DetailManagement(DetailView):
    model = Management
    template_name = 'ugsra/management/management_detail.html'
    context_object_name = 'management'
    pk_url_kwarg = 'management_id'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class ListDepartment(View):

    def get(self, request):
        department = Department.objects.order_by("sorting")
        employee = Employee.objects.all()
        context = {
            "department_list": department,
            "employee_list": employee,
        }
        return render(request, 'ugsra/department_list.html', context)


class ListDepartmentArea(View):

    def get(self, request):
        department = DepartmentArea.objects.order_by("sorting")
        employee = EmployeeArea.objects.all()
        context = {
            "department_list": department,
            "employee_list": employee,
        }
        return render(request, 'ugsra/department_list.html', context)


class ListStatistics(ListView):
    template_name = 'ugsra/statistics/statistics_list.html'
    context_object_name = 'item_list'

    def get_queryset(self):
        return Statistics.objects.order_by("-date")


class DetailStatistics(DetailView):
    model = Statistics
    template_name = 'ugsra/statistics/statistics_detail.html'
    context_object_name = 'item'
    pk_url_kwarg = 'statistics_id'


class ListDocuments(View):

    def get(self, request):
        document_chapter = ChapterDocument.objects.order_by("sorting")
        document_file = DocumentFile.objects.all()
        context = {
            "chapter_list": document_chapter,
            "file_list": document_file,
            "title": "Документы",
        }
        return render(request, 'ugsra/document_list.html', context)


class ListReporting(View):

    def get(self, request):
        reporting_chapter = ChapterReporting.objects.order_by("sorting")
        reporting_file = ReportingFile.objects.all()
        context = {
            "chapter_list": reporting_chapter,
            "file_list": reporting_file,
            "title": "Отчетность",
        }
        return render(request, 'ugsra/document_list.html', context)


class ListVideo(View):

    def get(self, request):
        video = Video.objects.order_by("date")
        context = {
            "publication_list": video,
            "title": "Видео",
        }
        return render(request, 'ugsra/media/media_list.html', context)


class DetailVideo(DetailView):
    model = Video
    template_name = 'ugsra/media/video_detail.html'
    context_object_name = 'video'
    pk_url_kwarg = 'video_id'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class ListImg(View):

    def get(self, request):
        image = ImageModel.objects.order_by("date")
        context = {
            "publication_list": image,
            "title": "Фото",
        }
        return render(request, 'ugsra/media/media_list.html', context)


class DetailPhoto(DetailView):
    model = ImageModel
    template_name = 'ugsra/media/photo_detail.html'
    context_object_name = 'photo'
    pk_url_kwarg = 'photo_id'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        photo_list = Img.objects.filter(imagemodel=self.kwargs.get("photo_id"))
        context['photo_list'] = photo_list
        return context
