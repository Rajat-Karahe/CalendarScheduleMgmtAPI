from rest_framework.serializers import ModelSerializer

from events.models import Event

class EventListSerializer(ModelSerializer):
	class Meta:
		model = Event
		fields = '__all__'


class EventDetailSerializer(ModelSerializer):
    class Meta:
        model = Event
        fields = "__all__"

class EventCreateSerializer(ModelSerializer):
    class Meta:
        model = Event
        fields = [
            'title',
            'event_date',
        ]        

class EventUpdateSerializer(ModelSerializer):
    class Meta:
        model = Event
        fields = [
            'title',
            'event_date',
        ]



