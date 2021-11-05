from django.db import models

class Rsvp(models.Model):
  class Meta:
    db_table = 'rsvp'

  create_at = models.DateTimeField(verbose_name='日時', null=True)
  guest = models.CharField(verbose_name='ゲスト', max_length=10)
  name = models.CharField(verbose_name='名前', max_length=30)
  furi = models.CharField(verbose_name='ふりがな', max_length=50)
  tel = models.CharField(verbose_name='電話番号', max_length=13)
  mail = models.EmailField(verbose_name='メールアドレス', max_length=100)
  post = models.CharField(verbose_name='郵便番号', max_length=8)
  address = models.CharField(verbose_name='住所', max_length=100)
  bus = models.CharField(verbose_name='送迎バス', blank=True, null=True, max_length=10)
  message = models.TextField(verbose_name='メッセージ', blank=True, null=True, max_length=1000)
  allergy = models.CharField(verbose_name='アレルギー', blank=True, null=True, max_length=500)
  conpanion1 = models.CharField(verbose_name='お連れ様１', blank=True, null=True, max_length=50)
  conpanion2 = models.CharField(verbose_name='お連れ様２', blank=True, null=True, max_length=50)
  conpanion3 = models.CharField(verbose_name='お連れ様３', blank=True, null=True, max_length=50)
  attendance = models.CharField(verbose_name='出欠', max_length=10)

  def __str__(self):
    return 'ゲスト：' + self.guest + '　|　名前：' +  self.name
