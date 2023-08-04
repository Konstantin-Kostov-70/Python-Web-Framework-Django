from rest_framework import serializers

from DjangoRESTDemo.demo_api.models import Book


class BookSerializer(serializers.ModelSerializer):
    def validate(self, data):
        if data.get('title'):
            if not data.get('title')[0].isupper():
                raise serializers.ValidationError('title must be start with capital')
        return data

    class Meta:
        model = Book
        fields = '__all__'



