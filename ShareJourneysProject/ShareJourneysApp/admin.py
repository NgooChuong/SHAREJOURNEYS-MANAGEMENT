import math

from django.contrib import admin

# Register your models here.
import cloudinary
from django.contrib import admin
<<<<<<< HEAD
from django.contrib.auth.hashers import make_password
from django.db.models.functions import ExtractYear
from django.utils.html import mark_safe
from oauth2_provider.models import AccessToken

=======
from django.db.models.functions import ExtractYear
from django.utils.html import mark_safe
>>>>>>> c6347c8742469fe044d9f4b96bbf4a5d20e7ac2b
from ShareJourneysApp.models import *
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django.db import connection
from django.utils.html import mark_safe
from django.urls import path
from django.db.models import Count, Sum, Avg, Subquery, OuterRef, ExpressionWrapper, F, FloatField
from django.template.response import TemplateResponse
from datetime import datetime



class MyAdminSite(admin.AdminSite):
    site_header = 'shareJourney'

    def get_urls(self):
        return [path('stats/', self.stats_view)] + super().get_urls()

    def stats_view(self, request): # danh gia user dua tren so rating thuoc 1 month
        if request.GET.get("month"):
            month = request.GET.get("month", datetime.now())
        else:
            month = datetime.now().month
        # 1.dau tien tinh trung binh cua 1 bài dang của 1 user => lấy ra tất cả trung bình đó ứng user đó
        # 2.xong so luong post thong qua id user và sum rate dua tren id user
        # 3.sum/avg: tinh tb user
        # select nhỏ nhất: 1
        # select giữa: 2
        # select ngoài cùng: 3
        sql = """
        SELECT (SUM / COUNT) AS 'trung_binh_danh_gia', f.username
        FROM (
            SELECT COUNT(user_id) AS count, SUM(tb) AS sum, d.user_id
            FROM (
                SELECT AVG(rate) AS tb, b.created_date, a.user_id
                FROM sharejourneysapp_rating b
                JOIN sharejourneysapp_posts a ON posts_id = a.id
                WHERE MONTH(b.created_date) = %s
                GROUP BY b.created_date, a.user_id
            ) d
            GROUP BY d.user_id
        ) e
        JOIN sharejourneysapp_user f ON e.user_id = f.id
        GROUP BY f.username
        """
        with connection.cursor() as cursor:
            cursor.execute(sql,[month])
            results = cursor.fetchall()
        data = [
            {"trung_binh_danh_gia": round( row[0],2), "username": row[1]}
            for row in results
        ]

        return TemplateResponse(request, 'admin/stats.html', {
            'stats': data,
            'stats2': self.stast2(month),
            'so_luong':range(len(data)),
            'm': month
        })
    def stast2(self, month): # thống kê rating của các bài post thuộc 1 monthp
        stats = (Posts.objects.filter(created_date__month=month).
        exclude(rating__rate__isnull=True).
        annotate(avg_rating=Avg('rating__rate')).
        values('title', 'avg_rating').order_by(
            '-avg_rating'))

        return stats

admin_site = MyAdminSite(name='shareJourney')

class PostForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorUploadingWidget)

    class Meta:
        model = Posts
        fields = '__all__'


class MyPostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'created_date', 'updated_date', 'active']
    search_fields = ['title', 'content']
    list_filter = ['id', 'created_date', 'title']
    readonly_fields = ['my_image']
    form = PostForm

    def my_image(self, instance):
        if instance:
            if instance.image is cloudinary.CloudinaryResource:
                return mark_safe(f"<img width='120' src='{instance.image.url}' />")

            return mark_safe(f"<img width='120' src='/static/{instance.image.name}' />")

    class Media:
        css = {
            'all': ('/static/css/style.css',)
        }


<<<<<<< HEAD
class AccessTokenAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'expires', 'created')
    search_fields = ('user__username',)
    list_filter = ('user', 'created', 'user__is_staff')
class UserCreationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'password','is_staff','avatar']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.password = make_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user
class UserAdmin(admin.ModelAdmin):
    form = UserCreationForm
    list_display = ['username', 'is_staff', 'is_active', 'date_joined']
    search_fields = ['username']
    list_filter = ['is_staff', 'is_active']

admin_site.register(Posts, MyPostAdmin)
=======
admin_site.register(Posts, MyPostAdmin)
admin_site.register(User)
>>>>>>> c6347c8742469fe044d9f4b96bbf4a5d20e7ac2b
admin_site.register(Tag)
admin_site.register(Comments)
admin_site.register(JourneyPictures)
admin_site.register(CommentReply)
admin_site.register(TravelCompanion)
admin_site.register(CommentTick)
admin_site.register(Rating)
admin_site.register(Reports)
admin_site.register(Users_Report)
admin_site.register(Local)
admin_site.register(Transportation)
admin_site.register(UserRoute)
<<<<<<< HEAD
admin_site.register(User, UserAdmin)
admin_site.register(AccessToken, AccessTokenAdmin)
=======

>>>>>>> c6347c8742469fe044d9f4b96bbf4a5d20e7ac2b
