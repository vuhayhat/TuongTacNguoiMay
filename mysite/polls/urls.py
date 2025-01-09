from django.urls import path
from . import views

app_name = 'polls'

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),  # Trang chính
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),  # Chi tiết câu hỏi
    path("<int:pk>/results/", views.ResultsView.as_view(), name="results"),  # Kết quả
    path("<int:question_id>/vote/", views.vote, name="vote"),  # Bình chọn
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),  # Hiển thị giao diện detail.html
    path("<int:pk>/results/", views.ResultsView.as_view(), name="results"),  # Hiển thị giao diện results.html
]
