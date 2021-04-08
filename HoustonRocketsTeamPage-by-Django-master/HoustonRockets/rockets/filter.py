import django_filters
from .models import Player,Match

class PlayerFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='iexact')

    class Meta:
        model = Player
        fields = ['height', 'position']

class MatchFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='iexact')

    class Meta:
        model = Match
        fields = ['arena']
