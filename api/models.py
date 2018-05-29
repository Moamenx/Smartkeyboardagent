from django.db import models
import datetime
import api.nlp
from django.utils import timezone


class User(models.Model):
    username = models.CharField(null=False, max_length=45, unique=True)
    gender = models.CharField(null=False, max_length=1)
    register_date = models.CharField(blank=True, null=True, max_length=20)
    current_ip = models.CharField(blank=True, null=True, max_length=45)
    register_ip = models.CharField(blank=True, null=True, max_length=45)
    setting = models.ForeignKey('Setting', models.DO_NOTHING, blank=True, null=True)
    adv_to_show = models.ForeignKey('UserAdvertisement', models.DO_NOTHING, null=True, to_field='id',related_name='+')
    password = models.CharField(max_length=45)

    def __str__(self):
        return self.username




class UserAdvertisement(models.Model):
    user = models.ForeignKey('User', models.DO_NOTHING, to_field='id',blank=False, null=False)
    advertisement_id = models.ForeignKey('Advertisement', models.DO_NOTHING, null=False, blank=False)
    is_displayed = models.BooleanField(null=False, default=False)
    publish_date = models.DateField(null=False, default=timezone.now)

    def __str__(self):
        return "User: {} Adv:{}".format(self.user.username, self.advertisement_id)

from django.db.models.signals import post_save
from django.dispatch import receiver

# @receiver(post_save, sender=UserAdvertisement, dispatch_uid="update_ads_to_show")
# def update_ad_to_show(sender, instance, **kwargs):
#      print(instance.id)
#      instance.User.adv_to_show = instance.id
#      instance.User.save()




class Setting(models.Model):
    email = models.CharField(null=True, max_length=45)
    phone = models.CharField(null=True, max_length=25)
    language = models.CharField(default='English', max_length=45)
    themes = models.ForeignKey('Themes', models.DO_NOTHING)


class Country(models.Model):
    name = models.CharField(max_length=20, null=False)


class Category(models.Model):
    name = models.CharField(max_length=45, null=False)

    def __str__(self):
        return self.name


class City(models.Model):
    name = models.CharField(max_length=45, null=False)
    country = models.ForeignKey('Country', models.DO_NOTHING)

    def __str__(self):
        return self.name


class Themes(models.Model):
    name = models.CharField(null=False, max_length=25)
    description = models.CharField(max_length=25, null=False)

    def __str__(self):
        return self.name


class ThemePhoto(models.Model):
    link = models.CharField(max_length=255, null=False)
    theme = models.ForeignKey('Themes', models.DO_NOTHING)


class ThemePhotosLink(models.Model):
    theme = models.ForeignKey('Themes', models.DO_NOTHING)
    themephoto = models.ForeignKey('ThemePhoto', models.DO_NOTHING)


class Advertiser(models.Model):
    name = models.CharField(max_length=50, blank=True, null=False)
    email = models.CharField(max_length=50, blank=True, null=False)
    password = models.CharField(max_length=1024, null=False)
    budget = models.FloatField(null=False)
    phone = models.CharField(max_length=20, null=False)

    def __str__(self):
        return self.name


class TypedWords(models.Model):
    sentence = models.CharField(max_length=1000, null=True)
    user = models.ForeignKey(User, models.DO_NOTHING)
    date = models.DateTimeField(default=datetime.datetime.now())

    def __str__(self):
        return self.sentence[:25]


class TargetedAge(models.Model):
    min_age = models.IntegerField(null=False)
    max_age = models.IntegerField(null=False)
    advertisement = models.ForeignKey('Advertisement', models.DO_NOTHING)


class AdvertisementCategory(models.Model):
    advertisement = models.ForeignKey('Advertisement', models.DO_NOTHING, null=False)
    category = models.ForeignKey('Category', models.DO_NOTHING, null=False)


class AdvertisementTag(models.Model):
    advertisement = models.ForeignKey('Advertisement', models.DO_NOTHING, null=False)
    tag = models.ForeignKey('Tag', models.DO_NOTHING, null=False)


class Tag(models.Model):
    tag = models.CharField(max_length=50, null=False)
    category = models.ForeignKey('Category', models.DO_NOTHING, null=False)

    def save(self, *args, **kwargs):
        nlp = api.nlp.NaturalLanguageProcessing()
        result = nlp.DoTokenizeProcess(self.tag)
        self.tag = result
        super(Tag, self).save(*args, **kwargs)

    def __str__(self):
        return self.tag


class Target(models.Model):
    targeted_age = models.ForeignKey('TargetedAge', models.DO_NOTHING)
    country = models.ForeignKey('Country', models.DO_NOTHING)
    city = models.ForeignKey('City', models.DO_NOTHING)



class Advertisement(models.Model):
    name = models.CharField(max_length=60, null=False)
    description = models.CharField(max_length=255, null=False)
    pub_date = models.DateField(null=False)
    target = models.ForeignKey('Target', models.DO_NOTHING, to_field='id', null=True)
    acceptance_id = models.IntegerField(null=True)
    rejection_id = models.IntegerField(null=True)
    advertiser = models.ForeignKey('Advertiser', models.DO_NOTHING, null=True)
    media = models.FileField(null=True)

    def __str__(self):
        return self.name


class AcceptedAdvertisement(models.Model):
    accept_date = models.DateField(null=False)
    advertisement = models.ForeignKey('Advertisement', models.DO_NOTHING, null=True)
    advertiser = models.ForeignKey('Advertiser', models.DO_NOTHING)


class RejectedAdvertisement(models.Model):
    reason = models.CharField(max_length=255, null=False)
    date = models.DateField(null=False)
    advertisement = models.ForeignKey('Advertisement', models.DO_NOTHING, null=True)
    advertiser = models.ForeignKey('Advertiser', models.DO_NOTHING)

    def __str__(self):
        return self.reason


class ThemesComments(models.Model):
    comment = models.CharField(max_length=999, null=True)
    theme = models.ForeignKey('Themes', models.DO_NOTHING)
    rating = models.IntegerField(null=False, default=0)
    date = models.DateField(blank=False)
    user = models.ForeignKey('User', to_field='username', on_delete=models.CASCADE)


class ThemeRating(models.Model):
    rating = models.IntegerField(null=True)
    theme = models.ForeignKey('Themes', models.DO_NOTHING)


class Device(models.Model):
    mac_address = models.CharField(max_length=255)
    user = models.ForeignKey('User', models.DO_NOTHING)

@receiver(post_save, sender=UserAdvertisement, dispatch_uid="ad_to_show")
def update_ad_to_show(sender, instance, **kwargs):
     id = instance.id
     print(id)
     userobj = User.objects.get(id=instance.user_id)
     userobj.adv_to_show = instance
     userobj.save()
     print(userobj.adv_to_show)
