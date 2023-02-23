import mongoengine as me
from mongoengine import Document, URLField
from mongoengine import DateTimeField, StringField, ReferenceField, ListField, IntField

class Movie(me.Document):
    title = me.StringField(required=True)
    year = me.IntField()
    rated = me.StringField()
    director = me.StringField()
    actors = me.ListField()

#If the document has nested fields, use EmbeddedDocument to defined the fields of the embedded document and EmbeddedDocumentField to declare it on the parent document.

#class Imdb(me.EmbeddedDocument):
#    imdb_id = me.StringField()
#    rating = me.DecimalField()
#    votes = me.IntField()


