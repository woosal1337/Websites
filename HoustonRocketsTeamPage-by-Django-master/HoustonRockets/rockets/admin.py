from django.contrib import admin
from .models import Player,Team,Match,Ticket,Player_Gallery,Comment,Profile


class PlayerAdmin(admin.ModelAdmin):
    model = Player
    list_display = ['name', 'number']


admin.site.register(Player, PlayerAdmin)


class TeamAdmin(admin.ModelAdmin):
    model = Team
    list_display = ['id', 'name']


admin.site.register(Team, TeamAdmin)


class MatchAdmin(admin.ModelAdmin):
    model = Match
    list_display = ['name','id']


admin.site.register(Match, MatchAdmin)


class ProfileAdmin(admin.ModelAdmin):
  model = Profile
  # list_display = ['id', 'name']


admin.site.register(Profile, ProfileAdmin)


class TicketAdmin(admin.ModelAdmin):
  model = Ticket
  list_display = ['id']

admin.site.register(Ticket, TicketAdmin)


class Player_GalleryAdmin(admin.ModelAdmin):
  model = Player_Gallery
  list_display = ['id']

admin.site.register(Player_Gallery, Player_GalleryAdmin)


class CommentAdmin(admin.ModelAdmin):
  model = Comment
  list_display = ['title']

admin.site.register(Comment, CommentAdmin)



