from rest_framework.routers import SimpleRouter
from rest_framework.urlpatterns import format_suffix_patterns
from django.conf.urls import url, include
from api.views import *


from api.views import *

router = SimpleRouter()
router.register("country", CountryViewSet)
router.register("themes", ThemeViewSet)
router.register("settings", SettingViewSet)
router.register("users", UserViewSet)
router.register("tags", TagViewSet)
router.register("city", CityViewSet)
router.register("advertiser",AdvertiserViewSet)
router.register("themephoto",ThemePhotoViewSet)
router.register("category",CategoryViewSet)
router.register("typedwords",TypedWordViewSet)
router.register("acceptedadveritsement",AcceptedAdvertisementViewSet)
router.register("advertisement",AdvertisementViewSet)
router.register("targeted-age",TargetedAgeViewSet)
router.register("rejectedadveritsement",RejectedAdvertisementViewSet)
router.register("devices", DevicesViewSet)
router.register("target", TargetViewSet)
router.register("theme-comments", ThemesCommentsViewSet)
router.register("theme-photos", ThemePhotosLinksViewSet)
router.register("theme-rating",ThemesRatingViewSet)
router.register("user-advertisement",UserAdvertisementViewSet)

urlpatterns = router.urls
