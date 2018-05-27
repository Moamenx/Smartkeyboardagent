from rest_framework.routers import SimpleRouter


from api.views import *

router = SimpleRouter()
router.register("country", CountryViewSet)
router.register("themes", ThemeViewSet)
router.register("settings", SettingViewSet)
router.register("users", UserViewSet)
router.register("city", CityViewSet)
router.register("advertiser",AdvertiserViewSet)
router.register("themephoto",ThemePhotoViewSet)
router.register("category",CategoryViewSet)
router.register("typedwords",TypedWordViewSet)
router.register("acceptedadveritsement",AcceptedAdvertisementViewSet)
router.register("rejectedadveritsement",RejectedAdvertisementViewSet)
router.register("devices", DevicesViewSet)
router.register("theme-comments", ThemesCommentsViewSet)
router.register("theme-photos", ThemePhotosLinksViewSet)
router.register("theme-rating",ThemesRatingViewSet)

urlpatterns = router.urls
