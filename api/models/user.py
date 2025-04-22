from django.db import models
import mongoengine as me
from datetime import date

class User(me.Document):
    firstName = me.StringField(required=True, max_length=30, min_length=3)
    lastName = me.StringField(required=True, max_length=50, min_length=3)
    birthday = me.DateField(required=True)
    age = me.IntField(min_value=1, max_value=120)
    goal = me.StringField(required=True)
    height = me.FloatField(min_value=30, max_value=300)
    weight = me.FloatField()

    @property
    def age(self):
        today = date.today()
        return today.year - self.birthday.year - (
                (today.month, today.day) < (self.birthday.month, self.birthday.day)
        )