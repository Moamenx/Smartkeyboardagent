from .serializers import *
from .models import *

from rest_framework.viewsets import ModelViewSet


class SettingViewSet(ModelViewSet):
    serializer_class = SettingSerializer
    queryset = Setting.objects.all()


class UserViewSet(ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()



class ThemeViewSet(ModelViewSet):
    serializer_class = ThemeSerializer
    queryset = Themes.objects.all()


class CountryViewSet(ModelViewSet):
    serializer_class = CountrySerializer
    queryset = Country.objects.all()


class CityViewSet(ModelViewSet):
    serializer_class = CitySerlaizer
    queryset = City.objects.all()


class AdvertiserViewSet(ModelViewSet):
    serializer_class = AdvertiserSerializer
    queryset = Advertiser.objects.all()


class CategoryViewSet(ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class ThemePhotoViewSet(ModelViewSet):
    serializer_class = ThemePhotoSerializer
    queryset = ThemePhoto.objects.all()


class TypedWordViewSet(ModelViewSet):
    serializer_class = TypedWordSerializer
    queryset = TypedWords.objects.all()


class AcceptedAdvertisementViewSet(ModelViewSet):
    serializer_class = AcceptedAdvertisementSerializer
    queryset = AcceptedAdvertisement.objects.all()


class RejectedAdvertisementViewSet(ModelViewSet):
    serializer_class = RejectedAdvertisementSerializer
    queryset = RejectedAdvertisement.objects.all()

class ThemesRatingViewSet(ModelViewSet):
    serializer_class = ThemesRatingSerializer
    queryset = ThemeRating.objects.all()


class ThemesCommentsViewSet(ModelViewSet):
    serializer_class = ThemesCommentsSerializer
    queryset = ThemesComments.objects.all()


class ThemePhotosLinksViewSet(ModelViewSet):
    serializer_class = ThemesPhotosLinkSerializer
    queryset = ThemePhotosLink.objects.all()

class DevicesViewSet(ModelViewSet):
    serializers_class = DevicesSerializer
    queryset = Device.objects.all()

