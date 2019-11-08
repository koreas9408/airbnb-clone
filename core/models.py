from django.db import models


class TimeStampedModel(models.Model):

    """ Time Stamped Model """

    # auto_now_add 생설될때 자동으로 날짜를 넣어줌
    # auto_now 업데이트 할때마다 넣어줌
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    """ abstract로 등록하면 DB에 맵핑이 안된다 """

    class Meta:
        abstract = True

