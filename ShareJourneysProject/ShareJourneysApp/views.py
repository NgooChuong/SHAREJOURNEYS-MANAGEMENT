<<<<<<< HEAD
import secrets
from datetime import datetime
import json
import random
from ShareJourneysApp.ImageCheck.Training import load_and_train_model

from django.contrib.auth import authenticate
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Avg, Subquery, OuterRef
=======
from datetime import datetime
import json

import requests
from django.contrib.auth.models import AnonymousUser
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Avg, Subquery, OuterRef, Q
from django.shortcuts import render
from django.utils import timezone
>>>>>>> c6347c8742469fe044d9f4b96bbf4a5d20e7ac2b

# Create your views here.
from django.shortcuts import render
from django.conf import settings
from django.core.mail import EmailMessage
<<<<<<< HEAD
from rest_framework.permissions import IsAuthenticated
=======
>>>>>>> c6347c8742469fe044d9f4b96bbf4a5d20e7ac2b
from rest_framework.views import APIView
from rest_framework import permissions, viewsets, generics, status
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from ShareJourneysApp import serializers,paginators, perm
<<<<<<< HEAD
from ShareJourneysApp.ImageCheck.main import change_dir
from ShareJourneysApp.models import *
from rest_framework.decorators import action
import cloudinary.uploader
from django.utils import timezone
from oauth2_provider.models import AccessToken, Application
import cloudinary
import joblib
import os
from pyvi import ViTokenizer

model_path = os.path.join(os.path.dirname(__file__), 'TextCheck\\content_model.pkl')
model = joblib.load(model_path)
import re
=======
from ShareJourneysApp.models import *
from rest_framework.decorators import action
from django.utils import timezone
import cloudinary.uploader

import cloudinary

>>>>>>> c6347c8742469fe044d9f4b96bbf4a5d20e7ac2b
# Create your views here.

from ShareJourneysApp.serializers import ReportSerializer


def index(request):
    return render(request, 'index.html', context={'name': 'Tuan'})

class  GetPostUser:
    @staticmethod
    def get_post_user(request,user):
<<<<<<< HEAD

=======
>>>>>>> c6347c8742469fe044d9f4b96bbf4a5d20e7ac2b
        posts = Posts.objects.filter(user=user).order_by('-id')
        paginator = paginators.UserPostsPaginator()
        page = paginator.paginate_queryset(posts, request)
        if page is not None:
            serializer = serializers.PostSerializer(page, many=True)
            return paginator.get_paginated_response(serializer.data)
        return Response(serializers.PostSerializer.data)

<<<<<<< HEAD
    @staticmethod
    def get_post_userNV(request, user):
        posts = Posts.objects.filter(user_NV=user, state='').order_by('-id')
        print(posts)
        paginator = paginators.UserPostsPaginator()
        page = paginator.paginate_queryset(posts, request)
        if page is not None:
            serializer = serializers.PostDetailSerializer(page, many=True)
            return paginator.get_paginated_response(serializer.data)
        return Response(serializers.PostDetailSerializer.data)


def get_or_create_access_token(user):
    # Tìm application để cấp phát access token
    try:
        # Chọn ứng dụng mặc định hoặc theo logic của bạn
        application = Application.objects.get(name='LTHD')
    except Application.DoesNotExist:
        # Xử lý khi không tìm thấy ứng dụng
        return None

    # Kiểm tra nếu đã có access token cho người dùng này
    access_token = AccessToken.objects.filter(user=user, application=application).first()

    # Nếu không có, tạo mới access token
    if not access_token:
        # Tạo access token mới
        access_token = AccessToken.objects.create(
            user=user,
            token= secrets.token_urlsafe(32),
            application=application,
            expires=timezone.now() + timezone.timedelta(days=365)  # Thời gian hết hạn (ví dụ: 1 năm)
        )

    return access_token
=======
>>>>>>> c6347c8742469fe044d9f4b96bbf4a5d20e7ac2b

class UserViewSet(viewsets.ViewSet,generics.CreateAPIView, generics.RetrieveAPIView):
    # lay profile thi hien cac bai post cua user dc chon
    queryset = User.objects.filter(is_active=True)
    serializer_class = serializers.UserSerializer
    parser_classes = [MultiPartParser, ]

<<<<<<< HEAD
    @staticmethod
    def get_access_token(user):
        access_token = AccessToken.objects.filter(user=user).first()
        return access_token
=======
>>>>>>> c6347c8742469fe044d9f4b96bbf4a5d20e7ac2b

    def get_permissions(self):
        if self.action in ['get_current_user']:
            return [permissions.IsAuthenticated()]

        return [permissions.AllowAny()]

<<<<<<< HEAD
    @action(methods=['get'], url_path='postsXetDuyet', detail=True,
            permission_classes=[IsAuthenticated])  # user/id/posts: cho xem trang cá nhan ng khac
    def get_posts_userNV(self, request, pk=None):
        user = self.get_object()
        print(user)
        print(request.user)
        # Kiểm tra xem người dùng đã đăng nhập chưa
        if not request.user.is_authenticated:
            return Response({"detail": "Authentication credentials were not provided."},
                            status=status.HTTP_401_UNAUTHORIZED)

        # Kiểm tra xem người dùng có phải là nhân viên không
        if not request.user.is_staff:
            return Response({"detail": "You do not have permission to perform this action."},
                            status=status.HTTP_403_FORBIDDEN)

        return GetPostUser.get_post_userNV(request=request, user=user)


    @action(methods=['post'], url_path="loginStaff", detail=False)
    def login(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        print(username, password)
        if not username or not password:
            return Response({'error': 'Please provide both username and password'}, status=400)

        user = authenticate(username=username, password=password)
        print("userr", user);
        access_token = get_or_create_access_token(user)
        if user is None:
            return Response({'error': 'User not found'}, status=404)

        if not user.is_staff:
            return Response({'error': 'Unauthorized access'}, status=403)

        if not user.check_password(password):
            return Response({'error': 'Invalid credentials'}, status=401)
        if not access_token:
            return Response({'error': 'Access token not found'}, status=status.HTTP_404_NOT_FOUND)
        serialized_user = serializers.UserSerializer(user).data
        response_data = {
            'user': serialized_user,
            'access_token': access_token.token,
            'expires': access_token.expires,
        }
        # If authentication is successful, serialize the user data
        return Response(response_data)

=======
>>>>>>> c6347c8742469fe044d9f4b96bbf4a5d20e7ac2b
    @action(methods=['get'], url_path='posts', detail=True) # user/id/posts: cho xem trang cá nhan ng khac
    def get_posts_user(self, request,pk):
        user = self.get_object()
        return GetPostUser.get_post_user(request=request, user=user)


    @action(methods=['get'], url_path='current-user/posts', detail=False) #Lấy post của current
    def get_posts_current_user(self, request):
        print(request.user)
        user = request.user
        return GetPostUser.get_post_user(request=request, user=user)


    @action(methods=['get', 'patch'], url_path='current-user', detail=False) # Lấy current
    def get_current_user(self, request):
        user = request.user
        if request.method.__eq__('PATCH'):
            for k, v in request.data.items():
                setattr(user, k, v)
            user.save()

        return Response(serializers.UserSerializer(user).data)



class HistoryPost(viewsets.ViewSet): # Lấy các post đã đi và da đăng ký

    @action(methods=['get'], url_path='hisPost', detail=False, description="Lấy lịch sử")
    def listHisPost(self, request):
        user = self.request.user
        print(user.id)
        # Subquery to get the rate from Rating
        rate_subquery = Rating.objects.filter(
            posts_id=OuterRef('pk'), # trỏ tới bảng post (giong outer join)
            user_id=user.id
        ).values('rate')
        # rating_value = Rating.objects.filter(pk=Subquery(rate_subquery)).values_list('rate', flat=True).first()

        # Main queryset
        queryset = TravelCompanion.objects.filter(
            user_id=user.id,
            posts__journey__ngayDen__lt=timezone.now()
        ).select_related(
            'posts', 'posts__journey'
        ).annotate(

            rate=Subquery(rate_subquery)
        ).values(
            'posts__id',
            'posts__created_date',
            'posts__title',
            'posts__content',
            'timeselect',
            'rate',
            'posts__journey__ngayDen',
            'user_id'
        ).distinct()
        serializer = serializers.HistoryOutComeSerializer(queryset, many=True, context={'request': request})
        return Response(serializer.data)

    @action(methods=['get'], url_path='hisPostRegister', detail=False, description="da dang ky")
    def listHisPostRegister(self, request):
        user = self.request.user
        print(user.id)


        # Main queryset
        queryset = TravelCompanion.objects.filter(
            user_id=user.id,
            posts__journey__ngayDen__gte=timezone.now()
        ).select_related(
            'posts', 'posts__journey'
        ).values(
            'posts__id',
            'posts__created_date',
            'posts__title',
            'posts__content',
            'active'
        ).distinct()
        serializer = serializers.HistorySerializer(queryset, many=True, context={'request': request})
        return Response(serializer.data)




class PostViewSet(viewsets.ViewSet, generics.DestroyAPIView, generics.RetrieveAPIView):
    queryset = Posts.objects.prefetch_related('tags')
    serializer_class = serializers.PostDetailSerializer

    # Xóa hoặc lấy chi tiết bài viết
    def get_permissions(self):
        if self.action in ['add_comments', ' add_comment_reply', 'add_rating', 'destroy','update_post_user']:
            return [permissions.IsAuthenticated()]
        return [permissions.AllowAny()]
    @action(methods=["patch"], url_path="updatePost", detail=True, description="để khóa comment")
    def update_post(self, request, pk):
        print("Vo xem")
        try:
            lc = Posts.objects.get(id=pk)
            print(lc.active)
            if lc:
                print("Vo cap nhat active")
                lc.active = not lc.active
                lc.save()
        except Exception:
            return Response({'status': False, 'message': 'Bài post không tìm thấy'})

        return Response(serializers.PostDetailSerializer(lc).data)

<<<<<<< HEAD
    # Check dao van cua bai post chi dinh
    @action(methods=['post'], url_path='checkBaiViet', detail=True,
            description="Lay 1 bai viet kem so luong rep voi cai dau tick")
    def check_BaiViet(self, request,pk, *args, **kwargs):
        sensitive_content = []
        sensitive_title = []
        print(self.get_object())
        title = request.data.get('title')
        content = request.data.get('content')
        print('content',content)
        # Check sensitive content for title and content
        title_prob = predict_sensitive_content(title) if title else 0
        content_prob = predict_sensitive_content(content) if content else 0
        print(title_prob, content_prob)
        # Determine if the post is sensitive based on amucdo
        mucdo = 0.6
        is_sensitive = (
                title_prob >= mucdo or
                content_prob >= mucdo
        )  # kiem tra nhay cam 1 trong 2 thang co
        if title_prob >= mucdo:
            sensitive_title = identify_sensitive_words(model, title, mucdo)
        if content_prob >= mucdo:
            sensitive_content = identify_sensitive_words(model, content, mucdo)
            print("sdsdas", sensitive_content)

        #Kiem tra ảnh
        images_url =  request.data.get("images")
        sensitive_image = []
        for i in images_url:
            print(change_dir(i.get('picture'))=="sensitive")
            if (change_dir(i.get('picture')).__eq__("sensitive")):
                sensitive_image.append(i)
        print('dadawd',sensitive_image)
        load_and_train_model()
        print(images_url)
        response_data = {'title': title, 'content': content,
            'sensitive_content_probabilities': {
                'title': title_prob,
                'content': content_prob,
                'sensitive_title': sensitive_title,
                'sensitive_content': sensitive_content,
                'pic_sensitive': sensitive_image
            }, 'is_sensitive': is_sensitive}


        return Response(response_data)

=======
>>>>>>> c6347c8742469fe044d9f4b96bbf4a5d20e7ac2b

    @action(methods=['post'], url_path='rates', detail=True,
            description="Lưu rating của user đó thuộc bài đăng đó")
    def add_rating(self, request, pk):
        c = self.get_object().rating_set.create(rate=request.data.get('rate'),
                                                user=request.user)
        return Response(serializers.RatingSerializer(c).data, status=status.HTTP_201_CREATED)

    @action(methods=['post','get'], url_path='comments', detail=True, description="them và lấy comment cho post")
    def add_comment(self, request, pk):
        if request.method.__eq__('POST'):
            c = self.get_object().comments_set.create(content=request.data.get('content'),
                                                     user=request.user)
            return Response(serializers.CommentSerializer(c).data, status=status.HTTP_201_CREATED)
        elif request.method.__eq__('GET'):
            comments = self.get_object().comments_set.select_related('user').order_by('-id')
            paginator = paginators.CommentPaginator()
            page = paginator.paginate_queryset(comments, request)
            if page is not None:
                serializer = serializers.CommentSerializer(page, many=True)
                return paginator.get_paginated_response(serializer.data)
            return Response(serializers.CommentSerializer(comments, many=True).data)

    @action(methods=['post'], url_path='comments/(?P<comment_id>[0-9]+)/tick', detail=True,
            description='Lưu ds nguời đi cùng được tick đồng thời lưu tạo mới tick ')
    def travelCompanion(self, request, pk, comment_id):
        # if comment_id:
        #     li, created =CommentTick.objects.get_or_create(cmtTick=)
        #     if not created:
        #         li.active = not li.active
        #         li.save()
        comment = Comments.objects.get(id=comment_id)
        if request.method.__eq__("POST"):
            print("vao duoc")
            print(self.get_object())
            print(request.user)
            li, created = TravelCompanion.objects.get_or_create(posts=self.get_object(),
                                                                user=User.objects.get(id=request.data.get("idUser")))
            lc, created_tic = CommentTick.objects.get_or_create(cmtTick=comment)
            print("chay duoc")
            print(lc)
            # cap nhat cai active
            if not created_tic:
                lc.active = not lc.active
                lc.save()
                if not lc.active:
                    print("voduoc xoa")
                    travelCompanion_Del = self.get_object().travelcompanion_set.filter(user=User.objects.get(id=request.data.get("idUser")))
                    travelCompanion_Del.delete()
                print("thoat dc")

            return Response(serializers.CommentSerializer(comment).data)

    @action(methods=["delete"], url_path='travelCompanion', detail=True,
            description="Xoa danh người đi cùng của bài post đó và có thể dùng trong trường hợp hủy lời mời")
    def del_travelCompanion(self, request, pk):
        if request.method.__eq__("DELETE"):
            print("vao xoa user di cung")
            print(self.get_object())
            travelCompanion_Del = self.get_object().travelcompanion_set.filter(
                user=User.objects.get(id=request.data.get("idUser")))
            print(travelCompanion_Del)
            travelCompanion_Del.delete()

            comments = self.get_object().comments_set.filter(user=User.objects.get(id=request.data.get("idUser")))
            try:
                CommentTick.objects.filter(cmtTick__in=comments).update(active=False)

            except ObjectDoesNotExist:
                return Response({"error": "Không tìm thấy CommentTick cho comment"},
                                status=status.HTTP_404_NOT_FOUND)
            return Response(status=status.HTTP_204_NO_CONTENT)

<<<<<<< HEAD


=======
>>>>>>> c6347c8742469fe044d9f4b96bbf4a5d20e7ac2b
    @action(methods=["patch"], url_path="editpost", detail=True, description="để chỉnh sửa bài viết")
    def update_post_user(self, request, pk):
        print("Vo xem")
        try:
            post_patch = self.get_object()
            start = Local.objects.get(pk=request.data.get('diemDi'))
            end = Local.objects.get(pk=request.data.get('diemDen'))
            router, bool_create = Route.objects.get_or_create(
                id_noiDi=start,
                id_noiDen=end
            )
            chiphi = request.data.get('chiPhi') if request.data.get('chiPhi') is not None else 0
            transport = Transportation.objects.get(pk=request.data.get('phuongtien'))
            journey, b = Journey.objects.get_or_create(
                chiPhi=chiphi,
                ngayDi=request.data.get('ngayDi'),
                ngayDen=request.data.get('ngayDen'),
                id_tuyenDuong=router,
                id_PhuongTien=transport
            )
            post_patch.content = request.data.get('content')
            post_patch.title = request.data.get('title')
            post_patch.journey = journey
            #tag
            tags_data = request.data.getlist('tag')
            tags_instances = []
            for tag in tags_data:
                tags_instances.append(Tag.objects.get(pk=int(tag)))
            post_patch.tags.set(tags_instances)


            # dia diem trung gian
            # for stop_data in json.loads(request.data.get('diaDiemTrungGian')):
            #     print('abcaida', type(stop_data))
            #     lc = Local.objects.get(pk=stop_data.get('iddiaDiem'))
            #     DiaDiemDungChan.objects.get_or_create(ThoiGianDuKien=stop_data.get('timedung')
            #                                           , id_DiaDiem_id=lc.id,
            #                                           id_HanhTrinh_id=journey.id)
            ## hình ảnh

            arrayPic = []
            # he thong
            for pic_data in request.data.getlist('pictureDaChon'):
                pc = JourneyPictures.objects.get(pk=int(pic_data))
                arrayPic.append(pc)

            # từ máy
            files = request.FILES.getlist('pictureUserSelect')
            base_url = f'https://res.cloudinary.com/{cloudinary.config().cloud_name}/'
            for file in files:
                result = cloudinary.uploader.upload(file)
                picture_url = result.get('secure_url').replace(base_url, '')
                if picture_url:
                    pic_instance = JourneyPictures(picture=picture_url)
                    arrayPic.append(pic_instance)
                    pic_instance.save()
            post_patch.pic.set(arrayPic)
            # xoa ảnh dc chọn từ máy
            # JourneyPictures.objects.filter(id__in=request.data.getlist('delPic')).delete()
            post_patch.save()




        except Exception :
            return Response({'status': False, 'message': 'Bài post không tìm thấy'})

        return Response(serializers.PostDetailSerializer(post_patch).data)

    @action(methods=["get"], url_path="Userroute", detail=True, description="lay duong di cua cac travel companion")
    def get_route(self,request, pk):
        user_routes = UserRoute.objects.select_related('id_User__user','id_User__posts','id_Don', 'id_Den').filter(id_User__posts=pk)
        username = self.request.query_params.get('u')
        c = self.request.query_params.get('c')
        a = self.request.query_params.get('a')
        if username and username != 'undefined':
            id_username = User.objects.filter(username__icontains=username)
            user_ids = id_username.values_list('id', flat=True)
            user_routes = user_routes.filter(id_User__user__in=user_ids)
        if c and c != 'undefined':
            print('1')
            print(c)
            user_routes = user_routes.filter(id_Don=c)
            print(user_routes)

        if a and a != 'undefined':
            print('2')
            print(a)
            user_routes = user_routes.filter(id_Den=a)
            print(user_routes)
        paginator = paginators.CommentPaginator()
        page = paginator.paginate_queryset(user_routes, request)
        if page is not None:
            serializer = serializers.UserRouteSerializer(page, many=True)
            return paginator.get_paginated_response(serializer.data)
        return Response(serializers.UserRouteSerializer(user_routes, many=True).data)

    @action(methods=["post"], url_path="updateAcceptPost", detail=True,
            description="Cập nhật active của người đi cùng và thêm dữ liệu cho bảng UserRoute")
    def update_UserRoute(self, request, pk):
        print("Vô xem")
        try:
            lc = self.get_object().travelcompanion_set.get(user=request.user)
            lc.active = True
            id_NoiDi = None
            id_NoiDen = None
            if request.data.get("id_NoiDi"):
                id_NoiDi = Local.objects.get(id=request.data.get("id_NoiDi"))
            if request.data.get("id_NoiDen"):
                id_NoiDen = Local.objects.get(id=request.data.get("id_NoiDen"))

            if id_NoiDi and id_NoiDen:
                  UserRoute.objects.get_or_create(
                    id_Don=id_NoiDi, id_Den=id_NoiDen, id_User=lc
                )


            lc.save()
        except Local.DoesNotExist:
            return Response({'status': False, 'message': 'Địa điểm không tìm thấy'})
        except TravelCompanion.DoesNotExist:
            return Response({'status': False, 'message': 'Người đi cùng không tìm thấy'})
        except Exception as e:
            print(f"Error: {str(e)}")
            return Response({'status': False, 'message': 'Có lỗi xảy ra'})

        return Response({'status': True, 'message': 'Cập nhật trạng thái thành công'})

<<<<<<< HEAD
    @action(methods=["patch"], url_path="updateXetDuyetPost", detail=True,
            description="cập nhật bài post để xét duyêt post")
    def update_XetDuyetPost(self, request, pk):
        print("Vo xem")
        try:
            lc = Posts.objects.get(id=pk)
            print(lc.state)
            if lc:
                print("Vo cap nhat active")
                lc.state = request.data.get("state")
                lc.save()
        except Exception:
            return Response({'status': False, 'message': 'Bài post không tìm thấy'})

        return Response({'status': True, 'message': 'Cập nhật trạng thái thành công'})
=======
>>>>>>> c6347c8742469fe044d9f4b96bbf4a5d20e7ac2b

class ListPostViewSet(viewsets.ViewSet, generics.ListAPIView):
    queryset = Posts.objects.select_related('user','journey').filter(journey__ngayDi__gte = datetime.now()).order_by('-created_date')
    serializer_class = serializers.Posts_userSerializer
    # Lấy tat ca cac post
    def get_queryset(self): # Lọc post
        queryset = Posts.objects.select_related('user','journey').filter(journey__ngayDi__gte =  datetime.now()).order_by('-created_date')
        print('dawdawdadwd',timezone.now().date())
        print(queryset)
        if self.action.__eq__('list'):
            jn = self.request.query_params.get('q')
            c = self.request.query_params.get('c')
            a = self.request.query_params.get('a')
            t = self.request.query_params.get('t')
            ti = self.request.query_params.get('ti')
            avg_rate_param = self.request.query_params.get('r')  # Tham số cho avgRate
            if jn and jn!='undefined':
                print('1')
                print(jn)
                queryset = queryset.filter(title__icontains=jn)
                print(queryset)

            if c and c!='undefined':
                print('2')
                print(queryset)
                queryset = queryset.filter( journey__id_tuyenDuong__id_noiDi__id = c)
                print(queryset)
            if a and a!='undefined':
                print('3')
                print(queryset)
                queryset = queryset.filter(journey__id_tuyenDuong__id_noiDen__id = a)
                print(queryset)
            if t and t!='undefined':
                print('4')
                print(queryset)
                queryset = queryset.filter(tags__id = t)
                print(queryset)
            if ti and ti!='undefined':
                print('4')
                print(queryset)
                ti = datetime.strptime(ti, "%Y-%m-%d").date()
                print(ti)
                queryset = queryset.filter(journey__ngayDi__date__gte=ti)
                print(queryset)
            if avg_rate_param and avg_rate_param!='undefined':  # Kiểm tra nếu avgRate được truyền làm query parameter
                avg_rate = float(avg_rate_param)  # Chuyển đổi thành số dấu phẩy động
                queryset = queryset.annotate(avg_rate=Avg('rating__rate')).filter(avg_rate__range=[ avg_rate,  avg_rate+1]) # Tính trung bình các đánh giá

        return queryset



class LocalViewSet(viewsets.ViewSet, generics.ListAPIView): # Lay ds dia diem
    queryset = Local.objects.all()
    serializer_class = serializers.LocalSerializer


class TransportationViewSet(viewsets.ViewSet, generics.ListAPIView): # lay ds phuong tien
    queryset = Transportation.objects.all()
    serializer_class = serializers.TransportationsSerilializer



class TagViewSet(viewsets.ViewSet, generics.ListAPIView): # Lay ds tag
    queryset = Tag.objects.all()
    serializer_class = serializers.TagSerializer

    @action(methods=['get'], url_path='posts', detail=True, description="lay post theo tag")
    def get_posts_by_tag(self,request,pk):
        post_with_tag = Posts.objects.filter(tags__id=pk).select_related('user','journey').filter(journey__ngayDi__gte = timezone.now())
        jn = self.request.query_params.get('q')
        c = self.request.query_params.get('c')
        a = self.request.query_params.get('a')
        ti = self.request.query_params.get('ti')
        avg_rate_param = self.request.query_params.get('r')  # Tham số cho avgRate
        if jn and jn!='undefined':
            print('1')
            print(jn)
            post_with_tag = post_with_tag.filter(title__icontains=jn)
        if c and c!='undefined':
            print('2')
            post_with_tag = post_with_tag.filter( journey__id_tuyenDuong__id_noiDi__id = c)
        if a and a!='undefined':
            print('3')
            post_with_tag = post_with_tag.filter(journey__id_tuyenDuong__id_noiDen__id = a)
        if ti and ti!='undefined':
            print('4')
            ti = datetime.strptime(ti, "%Y-%m-%d").date()
            print(ti)
            post_with_tag = post_with_tag.filter(journey__ngayDi__date__gte=ti)
        if avg_rate_param and avg_rate_param!='undefined':  # Kiểm tra nếu avgRate được truyền làm query parameter
            avg_rate = float(avg_rate_param)  # Chuyển đổi thành số dấu phẩy động
            post_with_tag = post_with_tag.annotate(avg_rate=Avg('rating__rate')).filter(avg_rate__range=[ avg_rate,  avg_rate+1]) # Tính trung bình các đánh giá
        paginator = paginators.ListPostsPaginator()
        serializer = serializers.PostSerializer(post_with_tag, many=True)
        sorted_data = sorted(serializer.data, key=lambda x: x['avgRate'], reverse=True)
        page = paginator.paginate_queryset(sorted_data, request)
        if page is not None:
            return paginator.get_paginated_response(page)
        print('anc')

        return Response(sorted_data, status=status.HTTP_200_OK)


# class TagViewSet(viewsets.ViewSet, generics.RetrieveAPIView):
#     queryset = Posts.objects.filter(tags__id=d).select_related('user')
#     serializer_class = serializers.PostSerializer

class PictureViewSet(viewsets.ViewSet, generics.ListAPIView): # lay ds hinh anh
    queryset = JourneyPictures.objects.all()
    serializer_class = serializers.ImageSerializer
    pagination_class = paginators.PicturePaginator



class PostALlViewSet(APIView):
    parser_classes = (MultiPartParser, FormParser)
    # luu bai post
    def post(self, request):
        start = Local.objects.get(pk=request.data.get('diemDi'))
        end = Local.objects.get(pk=request.data.get('diemDen'))
        router, bool_create = Route.objects.get_or_create(
            id_noiDi=start,
            id_noiDen=end
        )
        chiphi = request.data.get('chiPhi') if request.data.get('chiPhi') is not None else 0
        transport = Transportation.objects.get(pk=request.data.get('phuongtien'))
        journey , b= Journey.objects.get_or_create(
            chiPhi= chiphi,
            ngayDi=request.data.get('ngayDi'),
            ngayDen=request.data.get('ngayDen'),
            id_tuyenDuong=router,
            id_PhuongTien=transport
        )

        tags_data = request.data.getlist('tag')


        content_data = request.data.get('content')

        # # stops_data = Local.objects.filter(diaChi = request.data.get('stop'))
        # # print('2')
        # #
        # #
        # # # Tạo mới các đối tượng user, journey và tags từ dữ liệu tương ứng
        # # # user_instance = User.objects.get_or_create(**user_data)
        # #
        tags_instances = []
        print(tags_data)
        print(request.data.get('pictureDaChon'))
        for tag in tags_data:
            tags_instances.append(Tag.objects.get(pk = int(tag)))
        #


        for stop_data in json.loads(request.data.get('diaDiemTrungGian')):
           print('abcaida',type(stop_data))
           lc =  Local.objects.get(pk = stop_data.get('iddiaDiem'))
           DiaDiemDungChan.objects.get_or_create(ThoiGianDuKien=stop_data.get('timedung')
                                                 , id_DiaDiem_id=lc.id,
                                                 id_HanhTrinh_id=journey.id)
        #
        # # # Tạo mới đối tượng Post từ request.data và các đối tượng đã tạo
        post_instance = Posts.objects.create(
            title = request.data.get('title'),
            user=request.user, #doi lai request user
            content=content_data,
            journey=journey,
        )
        arrayPic = []

        for pic_data in request.data.getlist('pictureDaChon'):
            pc = JourneyPictures.objects.get(pk=int(pic_data))
            arrayPic.append(pc)
        files = request.FILES.getlist('pictureUserSelect')
        base_url = f'https://res.cloudinary.com/{cloudinary.config().cloud_name}/'
        for file in files:
            result = cloudinary.uploader.upload(file)
            picture_url = result.get('secure_url').replace(base_url, '')
            if picture_url:
                pic_instance = JourneyPictures(picture=picture_url)
                arrayPic.append(pic_instance)
                pic_instance.save()

        # Gán tags cho post_instance (n-n)
        post_instance.pic.set(arrayPic)
        post_instance.tags.set(tags_instances)
<<<<<<< HEAD

        # Gán nhân viên ngẫu nhiên làm người phê duyệt
        staff_users = User.objects.filter(is_staff=True)
        print('caocinaoifnoiaf',staff_users)
        if staff_users.exists():
            assigned_staff = random.choice(staff_users)
            print(assigned_staff)
            post_instance.user_NV = assigned_staff

=======
>>>>>>> c6347c8742469fe044d9f4b96bbf4a5d20e7ac2b
        post_instance.save()
        return Response(serializers.PostDetailSerializer(post_instance).data,status=status.HTTP_201_CREATED)


class CommentViewSet(viewsets.ViewSet, generics.DestroyAPIView):
    queryset = Comments.objects.all()
    serializer_class = serializers.CommentSerializer
    permission_classes = [perm.CommentOwner]
    def get_permissions(self):
        if self.action in ['add_and_get_comment_reply'] and self.request.POST:
            return [permissions.IsAuthenticated()]
        return [permissions.AllowAny()]

    @action(methods=['patch'], url_path='', detail=True)
    def patch_comment(self, request,pk):
        comment = Comments.objects.get(pk =self.get_object().id)
        print(comment)
        print(self.get_object())
        if request.method.__eq__('PATCH'):
            updated_data = request.data

            # Cập nhật dữ liệu của comment từ dữ liệu mới
            comment.content = updated_data.get('content', comment.content)
            # Cập nhật các trường khác nếu cần thiết

            # Lưu lại comment đã cập nhật vào cơ sở dữ liệu
            comment.save()

        return Response(serializers.CommentSerializer(self.get_object()).data)


    @action(methods=['post', 'get'], url_path='replies', detail=True,
            description="Lay va luu danh sach rep cua 1 comment")
    def add_and_get_comment_reply(self, request, pk):
        comment = self.get_object()
        if request.method.__eq__('POST'):
            reply = CommentReply.objects.create(cmtRep=comment,content=request.data.get('content'), user=request.user)
            return Response(serializers.CommentSerializer(comment).data, status=status.HTTP_201_CREATED)
        if request.method.__eq__('GET'):
            rep = comment.comment_reply.all().order_by("-created_date")
            return Response(serializers.ReplySerializer(rep, many=True).data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_408_REQUEST_TIMEOUT)



# class UserRouteViewSet(viewsets.ViewSet, generics.ListAPIView):
#     queryset =
#     serializer_class = serializers.PostDetailSerializer




class ReportViewSet(viewsets.ViewSet, generics.ListAPIView):
    queryset = Reports.objects.all()
    serializers_class = serializers.ReportSerializer

    def get_serializer_class(self):
        return ReportSerializer

    @action(methods=['post'], url_path='userReport', detail=True, description="Lưu user nào bị report nào")
    def UserReport(self, request, pk):
        ur_create = Users_Report.objects.create(report=self.get_object(),
                                                user=User.objects.get(id=request.data.get("idUser")))
        return Response(status=status.HTTP_201_CREATED)



class SendEmail(APIView): #  send mail
    def post(self, request):
        if request.method == 'POST':
<<<<<<< HEAD
            print(0)
            if request.data.get("user"):
                print(1)
=======
            if request.data.get("user"):
>>>>>>> c6347c8742469fe044d9f4b96bbf4a5d20e7ac2b
                client_email = "tuannguyen13@gmail.com"
                email = request.data
                nd = email.get('nd') + "\n" + "Người Vi pham:" + email.get('user')
                print(email)
                email_word = EmailMessage('Report user',
                                          nd,
                                          client_email,
                                          [settings.EMAIL_HOST_USER])
                email_word.send(fail_silently=False)
                return Response({'status': True, 'message': 'Email send sucesss'})
            if request.data.get("emailUser"):
<<<<<<< HEAD
                print(2)
=======
>>>>>>> c6347c8742469fe044d9f4b96bbf4a5d20e7ac2b
                email = request.data
                client_email = request.data.get("emailUser")
                user = User.objects.get(username=client_email)
                if not user:
                    return Response({'status': True, 'message': 'Email khong ton tai'})
                print("dada", client_email)
                nd = email.get('nd')
                print(email)
                email_word = EmailMessage('Reset Password',
                                          nd,
                                          settings.EMAIL_HOST_USER,
                                          [client_email])
                email_word.send(fail_silently=False)
                return Response({'status': True, 'message': 'Email send sucesss'})
            if request.data.get("emailClient") and request.data.get("ghiChu"):
<<<<<<< HEAD
                print(3)
                print("dadadsa", request.data.get("emailClient"))
                email = request.data
                print(request.data)
                client_email = request.data.get("emailClient")
                user = User.objects.get(username=client_email)

=======
                print("dadadsa", request.data.get("emailClient"))
                email = request.data
                client_email = request.data.get("emailClient")
                user = User.objects.get(username=client_email)
>>>>>>> c6347c8742469fe044d9f4b96bbf4a5d20e7ac2b
                if not user:
                    return Response({'status': True, 'message': 'Email khong ton tai'})
                print("dadadada", client_email)
                nd = email.get('ghiChu') + "\n" + "Cảm ơn bạn đã xem email này"
                print(email)
                email_word = EmailMessage('XÉT DUYỆT BÀI ĐĂNG HÀNH TRÌNH' + " " + request.data.get("title"),
                                          nd,
                                          settings.EMAIL_HOST_USER,
                                          [client_email])

                email_word.send(fail_silently=False)
                return Response({'status': True, 'message': 'Email send sucesss'})



class ChangePasswordView(generics.GenericAPIView):
    serializer_class = serializers.ChangePasswordSerializer
    model = User
    permission_classes = (permissions.IsAuthenticated,)

    def get_object(self, queryset=None):
        return self.request.user

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        print(request.data)
        serializer = self.get_serializer(data=request.data)
        print(serializer)
        print(serializer.is_valid())
        if serializer.is_valid():
            # Old password validation is already handled in serializer
            print('            # Old password validation is already handled in serializer')

            self.object.set_password(serializer.validated_data.get("new_password"))
            self.object.save()
            return Response({"detail": "Password updated successfully"}, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PasswordResetView(APIView):
    serializer_class = serializers.PasswordResetSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            try:
                user = User.objects.get(username=email)
                new_password = serializer.validated_data['new_password']
            except User.DoesNotExist:
                return Response({"error": "Người dùng với địa chỉ email này không tồn tại."},
                                status=status.HTTP_404_NOT_FOUND)

            # Tạo mật khẩu tạm thời
            user.set_password(new_password)
            user.save()

            # Trả về mật khẩu tạm thời
            return Response({"detail": "Đổi mật khẩu thành công"}, status=status.HTTP_200_OK)

<<<<<<< HEAD
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




def preprocess_text(text):
    # Xóa các ký tự đặc biệt, các số và các dấu câu
    text = re.sub(r'[^a-zA-ZÀ-Ỹà-ỹ0-9\s]', '', text)
    # Xóa các khoảng trắng thừa
    text = ' '.join(text.split())
    print(text)
    return text

def preprocess_text_with_pyvi(text):
    # Tách từ với pyvi
    words = ViTokenizer.tokenize(text)
    print("dada", words)
    # Loại bỏ các ký tự đặc biệt và số
    words = ' '.join([word for word in words.split() if word.isalpha()])
    return words

def identify_sensitive_words(model, text, mucdo=0.6):
    words = text.split()  # Tách văn bản thành các từ
    sensitive_words = []

    for word in words:
        preprocessed_word = word
        tienDoan = model.predict_proba([preprocessed_word])[0][1]
        if tienDoan >= mucdo:
            sensitive_words.append(word)

    return sensitive_words

def predict_sensitive_content(text):
    print("adjasdas", text)
    # processed_text = preprocess_text(text)

    print("dadads", text)
    tienDoan = model.predict_proba([text])[0][1]
    print(tienDoan)
    return tienDoan
=======
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
>>>>>>> c6347c8742469fe044d9f4b96bbf4a5d20e7ac2b
