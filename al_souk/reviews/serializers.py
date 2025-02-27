""" Serializers for al_souk.reviews """

from rest_framework.serializers import ModelSerializer
from al_souk.reviews.models import Review


# Create your serializers here.
class ReviewSerializer(ModelSerializer):
    """Review Serializer"""

    class Meta:
        """Meta data"""

        model = Review
        read_only_fields = ("user", "product")
        fields = (
            "id",
            "url",
            "user",
            "product",
            "rating",
            "content",
            "created_at",
            "updated_at",
        )
