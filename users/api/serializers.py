from django.contrib.contenttypes.models import ContentType
from django.contrib.auth import get_user_model
from rest_framework.validators import UniqueValidator
from django.db.models import Q


from rest_framework.serializers import (
	CharField,
	EmailField,
	HyperlinkedIdentityField,
	ModelSerializer,
	SerializerMethodField,
	ValidationError
	)


User = get_user_model()

class UserCreateSerializer(ModelSerializer):

	email = EmailField(
		required=True,
		validators=[UniqueValidator(queryset=User.objects.all())]
		)
	username = CharField(
		validators=[UniqueValidator(queryset=User.objects.all())]
		)
	password = CharField(min_length=8)

	def create(self, validated_data):
		user = User.objects.create_user(validated_data['username'], validated_data['email'],
			validated_data['password'])
		return user

	class Meta:
		model = User
		fields = ('username', 'email', 'password')
    
# 
