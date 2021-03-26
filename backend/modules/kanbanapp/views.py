from django.http import JsonResponse
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from rest_auth.registration.views import SocialLoginView, SocialAccountListView
from rest_framework import viewsets, views
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
import json

from .models import Card
from .serializers import CardSerializer


class GoogleLogin(SocialLoginView):
    adapter_class = GoogleOAuth2Adapter


class CardViewSet(viewsets.ModelViewSet):
    serializer_class = CardSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.request.user.cards.all()
    
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def resortCards(request):
    data = json.loads(request.body)
    for status, column in enumerate(data):
        for index, card_id in enumerate(column):
            card = Card.objects.get(id=card_id)
            card.status = status+1
            card.position = index
            card.save()
    return JsonResponse(data={'success': True}, safe=True)
