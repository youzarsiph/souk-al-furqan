""" Serializers for al_souk.products """

from rest_framework.serializers import ModelSerializer
from al_souk.products.models import Product


# Create your serializers here.
class ProductSerializer(ModelSerializer):
    """Serialize products"""

    class Meta:
        """Meta data"""

        model = Product
        fields = (
            "id",
            "url",
            "image",
            "name",
            "description",
            "price",
            "stock",
            "created_at",
            "updated_at",
        )
