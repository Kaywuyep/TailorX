from rest_framework import serializers
from .models import Tailor, Picture, Message

class PictureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Picture
        fields = ('id', 'image', 'uploaded_at')

class TailorSerializer(serializers.ModelSerializer):
    portfolio_images = PictureSerializer(many=True, read_only=True)

    class Meta:
        model = Tailor
        fields = ('id', 'user', 'location', 'tailor_pictures')

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ('id', 'sender', 'recipient', 'timestamp', 'content')
