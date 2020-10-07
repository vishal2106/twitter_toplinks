from pymodm import MongoModel,EmbeddedMongoModel, fields
from .models_manager import DefaultManager

class Tweets(MongoModel):
    tweets_list = fields.ListField(fields.DictField())
    objects = DefaultManager()

    class Meta:
        collection_name = 'Tweets'
        final = True