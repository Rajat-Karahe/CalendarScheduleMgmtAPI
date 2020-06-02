from events.models import Event
from rest_framework.generics import (
    CreateAPIView,
    DestroyAPIView,
    ListAPIView, 
    UpdateAPIView,
    RetrieveAPIView,
    RetrieveUpdateAPIView
    )
from .permissions import IsOwner

from rest_framework.filters import (
        SearchFilter,
        OrderingFilter,
    )

from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
    IsAdminUser,
    IsAuthenticatedOrReadOnly,
    # IsOwnerOrReadOnly,
    )  
    
from .serializers import (
    EventUpdateSerializer, 
    EventDetailSerializer, 
    EventListSerializer,
    EventCreateSerializer
    )  


class EventCreateAPIView(CreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventCreateSerializer
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
    	queryset = Event.objects.all()
    	queryset = queryset.filter(author=self.request.user)
    	return queryset
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
	

class EventDetailAPIView(RetrieveAPIView):
    queryset = Event.objects.all()
    serializer_class = EventDetailSerializer
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
    	queryset = Event.objects.all()
    	queryset = queryset.filter(author=self.request.user)
    	return queryset

class EventUpdateAPIView(RetrieveUpdateAPIView):
    serializer_class = EventUpdateSerializer
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
    	queryset = Event.objects.all()
    	queryset = queryset.filter(author=self.request.user)
    	return queryset

    # def perform_update(self, serializer):
    #     serializer.save(user=self.request.user)


class EventDeleteAPIView(DestroyAPIView):
    serializer_class = EventDetailSerializer
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
    	queryset = Event.objects.all()
    	queryset = queryset.filter(author=self.request.user)
    	return queryset


class EventListAPIView(ListAPIView):
	serializer_class = EventListSerializer
	permission_classes = [IsAuthenticated]
	def get_queryset(self):
		queryset = Event.objects.all().order_by('-event_date')
		queryset = queryset.filter(author=self.request.user)
		# filter_backends = [OrderingFilter]
		# ordering_fields = ['event_date']
		return queryset
        # user = self.request.query_params.get('user')

        

        

    	