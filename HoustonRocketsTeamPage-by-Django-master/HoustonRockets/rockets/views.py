from django.shortcuts import get_object_or_404, render, redirect
from .models import Player, Match, Team, Player_Gallery, Comment, Profile, Ticket
from .forms import SampleForm, SignUpForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from .filter import PlayerFilter, MatchFilter
import datetime


def index(request):
    player = Player.objects.all()
    matchess = Match.objects.all()
    player_gallery = Player_Gallery.objects.all()[:6]
    matches = Match.objects.order_by('-start_day')[:3]
    comment = Comment.objects.all()[:4]
    content = {'players': player, 'matches': matches, 'matchess': matchess, 'comments': comment,
               'player_gallerys': player_gallery}
    return render(request, "rockets/index.html", content)


def about(request):
    player = Player.objects.all()
    team = Team.objects.all()
    matches = Match.objects.order_by('-start_day')
    content = {'players': player, 'matches': matches, 'teams': team}
    return render(request, "rockets/about.html", content)


def players(request):
    player = Player.objects.all()
    content = {'players': player}
    return render(request, "rockets/players.html", content)


def exp(request, player_id):
    player = get_object_or_404(Player, pk=player_id)
    content = {'player': player}
    return render(request, "rockets/exp.html", content)


def gallery(request):
    imge = Player_Gallery.objects.all()
    content = {'imges': imge}
    return render(request, "rockets/gallery.html", content)


def original_template(request):
    content = {}
    return render(request, "pluton/original_template.html", content)


def player(request, player_id, player):
    player_gallery = Player_Gallery.objects.all().filter(player=player_id)
    player = get_object_or_404(Player, pk=player_id)
    comment = Comment.objects.all().filter(player=player_id)
    if request.user.id:
        user1 = get_object_or_404(User, pk=request.user.id)
    form_errors = {}
    form_values = {"title": "", "body": ""}
    if request.POST:
        form_values["title"] = request.POST["title"]
        form_values["body"] = request.POST["yorum"]
        if len(request.POST["yorum"]) < 10:
            form_errors["body"] = "You comment is too short. It should be at least 10 characters"
        if len(request.POST["title"]) == 0:
            form_errors["title"] = "Title field is required"
        if len(form_errors) == 0:
            new_comment = Comment()
            new_comment.title = form_values["title"]
            new_comment.body = form_values["body"]
            new_comment.player = player
            new_comment.user1 = user1
            new_comment.save()
            form_values["title"] = ""
            form_values["body"] = ""
            print("SAVED YEHUHUUHUHUHUHUHUHUHU")
            print("comment=", request.POST["yorum"])
    else:
        pass

    content = {'player': player, 'player_gallerys': player_gallery, "errors": form_errors,
               "values": form_values, 'comments': comment}
    return render(request, "rockets/player.html", content)


def buy_ticket(request, match_id):
    match = get_object_or_404(Match, pk=match_id)
    ticket = get_object_or_404(Ticket, pk=match_id)
    if request.user.id:
        user = get_object_or_404(User, pk=request.user.id)
    form_errors = {}
    form_values = {"seat_number": 0, "creditcard": ""}
    if request.POST:
        form_values["seat_number"] = request.POST["seat_number"]
        form_values["creditcard"] = request.POST["creditcard"]
        if len(request.POST["creditcard"]) < 10:
            form_errors["creditcard"] = "You credit car number should be 12 characters"
        if len(request.POST["seat_number"]) == 0:
            form_errors["seat_number"] = "Seat number field is required"
        if len(form_errors) == 0:
            new_ticket = Ticket()
            new_ticket.creditcard = form_values["creditcard"]
            new_ticket.seat_number = form_values["seat_number"]
            new_ticket.match = match
            new_ticket.user = user
            new_ticket.save()
            form_values["seat_number"] = 0
            form_values["creditcard"] = ""
            print("SAVED YEHUHUUHUHUHUHUHUHUHU")
    else:
        pass
    content = {'match': match, "errors": form_errors, "values": form_values,'ticket':ticket}
    print(match_id)
    return render(request, "rockets/buy_ticket.html", content)


def filtering(request):
    f = PlayerFilter(request.GET, queryset=Player.objects.all())
    fm = MatchFilter(request.GET, queryset=Match.objects.all())
    now = datetime.date.today()
    return render(request, 'rockets/list.html', {'filter': f, 'filterm': fm,'today':now})


def matches(request):
    now = datetime.date.today()
    player = Player.objects.all()
    match = Match.objects.order_by('start_day')
    content = {'matches': match, 'today': now, 'players': player}
    return render(request, "rockets/match.html", content)


def pre_match(request):
    now = datetime.date.today()
    matches = Match.objects.all()
    player = Player.objects.all()
    pre_matches = []
    for match in matches:
        if match.start_day < now:
            pre_matches.append(match)
            content = {'today': now, 'pre_matches': pre_matches,'players': player}
        else:
            pass
    return render(request, "rockets/pre_match.html", content)


def next_match(request):
    now = datetime.date.today()
    matches = Match.objects.all()
    player = Player.objects.all()
    next_matches = []
    for match in matches:
        if (match.start_day > now):
            print(match.start_day)
            next_matches.append(match)
            print(next_matches)
            content = {'today': now, 'next_matches': next_matches,'players': player}
            print(content)
        else:
            pass
    return render(request, "rockets/next_match.html", content)


def match_page(request, match_id, match):
    now = datetime.date.today()
    match = get_object_or_404(Match, pk=match_id)
    content = {'match': match, 'today': now}
    return render(request, "rockets/match_page.html", content)


def match_video(request, match_id):
    match = get_object_or_404(Match, pk=match_id)
    content = {'match': match}
    return render(request, "rockets/match_video.html", content)


def stats(request):
    player = Player.objects.all()
    match = Match.objects.all()
    ordeby_points = Player.objects.order_by('-points')
    content = {'players': player, 'orderby_points': ordeby_points, 'matches': match}
    return render(request, "rockets/status.html", content)


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  # load the profile instance created by the signal
            user.profile.bio = form.cleaned_data.get('bio')
            print("avatar", form.cleaned_data.get('avatar'))
            print(request.FILES)
            user.profile.avatar = request.FILES['avatar']
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('/')
    else:
        form = SignUpForm()
    #
    return render(request, 'rockets/signup.html', {'form': form})


def login_view(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
    else:
        pass
    # return redirect(request.path)
    return redirect("/")


def logout_view(request):
    logout(request)
    # return redirect(request.path)
    return redirect("/")


def user_page(request, user_id):
    if request.user.id:
        user_id = request.user.id
    user = get_object_or_404(User, pk=user_id)
    comment = Comment.objects.all().filter(user1=user_id)
    ticket = Ticket.objects.all().filter(user=user_id)
    #match = get_object_or_404(Match, pk=match_id)
    content = {'user': user, 'comments': comment,'tickets':ticket}
    return render(request, "rockets/user_page.html", content)

def report(request):
    content = {}
    return render(request, "rockets/report.html", content)
