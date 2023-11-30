from django.urls import path
from . import views



urlpatterns = [
    path("", views.IndexView.as_view(), name='home'),
    path("electronic-reporting/", views.ReportingView.as_view(), name='reporting'),
    path("news/", views.ListNews.as_view(), name='news-list'),
    path("news/<int:news_id>/", views.DetailNews.as_view(), name='news-detail'),
    path("structure/management/", views.ListManagement.as_view(), name='management-list'),
    path("structure/management/<int:management_id>/", views.DetailManagement.as_view(), name='management-detail'),
    path("structure/department/", views.ListDepartment.as_view(), name='department-list'),
    path("structure/department-area/", views.ListDepartmentArea.as_view(), name='department-area-list'),
    path("statistics/", views.ListStatistics.as_view(), name='statistics-area-list'),
    path("statistics/<int:statistics_id>/", views.DetailStatistics.as_view(), name='statistics-detail'),
    path("document/", views.ListDocuments.as_view(), name='document-area-list'),
    path("reporting/", views.ListReporting.as_view(), name='reporting-list'),
    path("media/video/", views.ListVideo.as_view(), name='video-list'),
    path("media/video/<int:video_id>/", views.DetailVideo.as_view(), name='video-detail'),
    path("media/photo/", views.ListImg.as_view(), name='photo-list'),
    path("media/photo/<int:photo_id>/", views.DetailPhoto.as_view(), name='photo-detail'),

    # path("ab/", views.IndexView.as_view(), name='home'),
    # path("ab/electronic-reporting/", views.ReportingView.as_view(), name='reporting'),
    # path("ab/news/", views.ListNews.as_view(), name='news-list'),
    # path("ab/news/<int:news_id>/", views.DetailNews.as_view(), name='news-detail'),
    # path("ab/structure/management/", views.ListManagement.as_view(), name='management-list'),
    # path("ab/structure/management/<int:management_id>/", views.DetailManagement.as_view(), name='management-detail'),
    # path("ab/structure/department/", views.ListDepartment.as_view(), name='department-list'),
    # path("ab/structure/department-area/", views.ListDepartmentArea.as_view(), name='department-area-list'),
    # path("ab/statistics/", views.ListStatistics.as_view(), name='statistics-area-list'),
    # path("ab/document/", views.ListDocuments.as_view(), name='document-area-list'),
    # path("ab/reporting/", views.ListReporting.as_view(), name='reporting-list'),
    # path("ab/media/video/", views.ListVideo.as_view(), name='video-list'),
    # path("ab/media/video/<int:video_id>/", views.DetailVideo.as_view(), name='video-detail'),
    # path("ab/media/photo/", views.ListImg.as_view(), name='photo-list'),
    # path("ab/media/photo/<int:photo_id>/", views.DetailPhoto.as_view(), name='photo-detail'),
]
