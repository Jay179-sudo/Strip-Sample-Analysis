from rest_framework import serializers

class AnalyzerSerializer(serializers.Serializer):
    email = serializers.EmailField(max_length=255)
    image = serializers.ImageField()

    def validate(self, attrs):
        return attrs

