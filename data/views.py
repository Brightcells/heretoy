# Create your views here.

from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from CodeConvert import CodeConvert

from data.models import TestTokenInfo, Html5GamesInfo, Html5GamesPlayInfo, Html5GamesPlayLog, Html5GamesNailLog, Html5GamesLikeInfo, Html5GamesUnlikeInfo, TopicGamesInfo, LunbotuInfo
from utils.json_utils import JsonHttpResponse

import ast
import copy
import json
import random
import requests

from datetime import datetime


GAME_NUM_PER_PAGE = settings.GAME_NUM_PER_PAGE
PLAY = settings.PLAY_NUM_PER_CLICK
LIKE = settings.LIKE_NUM_PER_CLICK

RESULT_BASE = {
    'status': 0,
    'data': {
        'msg': 'Success'
    }
}


def get_my_play_num(token, h5game):
    try:
        return Html5GamesPlayInfo.objects.get(token=token, h5game=h5game).play
    except:
        return 0


def get_game_info(token, h5game):
    game_info = h5game.data
    game_info['like_flag'] = have_already_like(token, h5game)
    game_info['unlike_flag'] = have_already_unlike(token, h5game)
    game_info['myplay'] = get_my_play_num(token, h5game)
    game_info['nail_flag'] = have_already_nail(token, h5game)
    return game_info


def deal_with_sort(rec, token):
    if rec['sort'] == 0:
        rec['h5game'] = get_game_info(token, rec['h5game'])
    else:
        rec.pop('h5game')
    return rec


def get_left_game_num(total, end):
    return max(total - end, 0)


def games(request):
    token = request.GET.get('token', '')
    _type = int(request.GET.get('type', 0))
    p = int(request.GET.get('page', 1))

    start = GAME_NUM_PER_PAGE * (p - 1)
    end = GAME_NUM_PER_PAGE * p

    if _type in [0, 1]:
        testokens = [d['token'] for d in TestTokenInfo.objects.filter(status=True).values('token')]

        if token in testokens:
            allh5games = Html5GamesInfo.objects.filter(status=True).exclude(onshalf='off')
        else:
            allh5games = Html5GamesInfo.objects.filter(status=True, onshalf='on')

        if _type == 0:
            h5games = allh5games.order_by('-play', '-like', 'unlike')[start:end]
            lunbotu = LunbotuInfo.objects.filter(lbt_classify='hot', status=True).order_by('-modify_at')
        else:
            h5games = allh5games.order_by('-create_at')[start:end]
            lunbotu = LunbotuInfo.objects.filter(lbt_classify='new', status=True).order_by('-modify_at')

        h5games = [get_game_info(token, h5game) for h5game in h5games]
        recommend = [deal_with_sort(lbt.data, token) for lbt in lunbotu]
    else:
        start = GAME_NUM_PER_PAGE * 2 * (p - 1)
        end = GAME_NUM_PER_PAGE * 2 * p

        allh5games = Html5GamesPlayInfo.objects.filter(token=token)
        h5games = allh5games.order_by('-nail', '-modify_at')[start:end]
        h5games = [get_game_info(token, h5.h5game) for h5 in h5games]
        recommend = []

    return JsonHttpResponse(
        dict(
            status=0,
            data=h5games,
            left=get_left_game_num(len(allh5games), end),
            recommend=recommend,
        )
    )


def mine(request):
    token = request.GET.get('token', '')
    p = int(request.GET.get('page', 1))

    start = GAME_NUM_PER_PAGE * 2 * (p - 1)
    end = GAME_NUM_PER_PAGE * 2 * p

    h5gamesplay = Html5GamesPlayInfo.objects.filter(token=token).order_by('-modify_at')[start:end]
    h5gamesplay = [h5.data for h5 in h5gamesplay]

    all_games_play = len(Html5GamesPlayInfo.objects.all())
    left = max(all_games_play - end, 0)

    return JsonHttpResponse(dict(status=0, data=h5gamesplay, left=left))


def have_already_like(token, h5game):
    return Html5GamesLikeInfo.objects.filter(token=token, h5game=h5game).exists()


def have_already_unlike(token, h5game):
    return Html5GamesUnlikeInfo.objects.filter(token=token, h5game=h5game).exists()


def play(request):
    RESULT = copy.deepcopy(RESULT_BASE)

    token = request.GET.get('token', '')
    pk = request.GET.get('pk', '')

    try:
        h5game = Html5GamesInfo.objects.get(md5=pk)
        h5game.play += PLAY
        h5game.real_play += 1
        h5game.save()
        try:
            h5gameplay = Html5GamesPlayInfo.objects.get(token=token, h5game=h5game)
            h5gameplay.play += 1
            h5gameplay.save()
        except:
            Html5GamesPlayInfo.objects.create(token=token, h5game=h5game)
        Html5GamesPlayLog.objects.create(token=token, h5game=h5game)
    except:
        RESULT['status'] = 1
        RESULT['data']['msg'] = 'Game of this pk doesn\'t exists!'

    return JsonHttpResponse(RESULT)


def have_already_like_or_unlike(token, h5game):
    return have_already_like(token, h5game) or have_already_unlike(token, h5game)


def like(request):
    RESULT = copy.deepcopy(RESULT_BASE)

    token = request.GET.get('token', '')
    pk = request.GET.get('pk', '')

    try:
        h5game = Html5GamesInfo.objects.get(md5=pk)
        if have_already_like_or_unlike(token, h5game):
            RESULT['status'] = 1
            RESULT['data']['msg'] = 'You have already like/unlike game of this pk!'
        else:
            h5game.like += LIKE
            h5game.real_like += 1
            h5game.save()
            Html5GamesLikeInfo.objects.create(token=token, h5game=h5game)
    except:
        RESULT['status'] = 1
        RESULT['data']['msg'] = 'Game of this pk doesn\'t exists!'

    return JsonHttpResponse(RESULT)


def unlike(request):
    RESULT = copy.deepcopy(RESULT_BASE)

    token = request.GET.get('token', '')
    pk = request.GET.get('pk', '')

    try:
        h5game = Html5GamesInfo.objects.get(md5=pk)
        if have_already_like_or_unlike(token, h5game):
            RESULT['status'] = 1
            RESULT['data']['msg'] = 'You have already like/unlike game of this pk!'
        else:
            h5game.unlike += 1
            h5game.save()
            Html5GamesUnlikeInfo.objects.create(token=token, h5game=h5game)
    except:
        RESULT['status'] = 1
        RESULT['data']['msg'] = 'Game of this pk doesn\'t exists!'

    return JsonHttpResponse(RESULT)


@csrf_exempt
def plu(request):
    RESULT = copy.deepcopy(RESULT_BASE)

    if request.method == 'GET':
        token = request.GET.get('token', '')
        _type = int(request.GET.get('type', 0))
        pk = request.GET.get('pk', '')
    else:
        if request.POST == {} and request.body != '':
            try:
                request.POST = json.loads(request.body)
            except:
                pass
        else:
            pass
        token = request.POST.get('token', '')
        _type = int(request.POST.get('type', 0))
        pk = request.POST.get('pk', '')

    try:
        h5game = Html5GamesInfo.objects.get(md5=pk)
        if _type == 0:
            h5game.play += random.randint(5, 10)
            h5game.real_play += 1
            h5game.save()
            try:
                h5gameplay = Html5GamesPlayInfo.objects.get(token=token, h5game=h5game)
                h5gameplay.play += 1
                h5gameplay.save()
            except:
                Html5GamesPlayInfo.objects.create(token=token, h5game=h5game)
            Html5GamesPlayLog.objects.create(token=token, h5game=h5game)
        elif _type == 1:
            if have_already_like_or_unlike(token, h5game):
                RESULT['status'] = 1
                RESULT['data']['msg'] = 'You have already like/unlike game of this pk!'
            else:
                h5game.like = min(h5game.like + random.randint(5, 10), h5game.play - h5game.unlike)
                h5game.real_like += 1
                h5game.save()
                Html5GamesLikeInfo.objects.create(token=token, h5game=h5game)
        else:
            if have_already_like_or_unlike(token, h5game):
                RESULT['status'] = 1
                RESULT['data']['msg'] = 'You have already like/unlike game of this pk!'
            else:
                h5game.unlike += 1
                h5game.save()
                Html5GamesUnlikeInfo.objects.create(token=token, h5game=h5game)
    except:
        RESULT['status'] = 1
        RESULT['data']['msg'] = 'Game of this pk doesn\'t exists!'

    return JsonHttpResponse(RESULT)


def have_already_nail(token, h5game):
    return Html5GamesPlayInfo.objects.filter(token=token, h5game=h5game, nail=True).exists()


def set_or_remove_nail(token, h5game, flag):
    h5gameplay, created = Html5GamesPlayInfo.objects.get_or_create(token=token, h5game=h5game)
    h5gameplay.nail = flag
    h5gameplay.save()
    Html5GamesNailLog.objects.create(token=token, h5game=h5game, nail=False)


@csrf_exempt
def nail(request):
    RESULT = copy.deepcopy(RESULT_BASE)

    if request.method == 'GET':
        token = request.GET.get('token', '')
        nail = int(request.GET.get('nail', 0))
        pk = request.GET.get('pk', '')
    else:
        if request.POST == {} and request.body != '':
            try:
                request.POST = json.loads(request.body)
            except:
                pass
        else:
            pass
        token = request.POST.get('token', '')
        nail = int(request.POST.get('nail', 0))
        pk = request.POST.get('pk', '')

    try:
        h5game = Html5GamesInfo.objects.get(md5=pk)
        if nail == 0:
            if have_already_nail(token, h5game):
                RESULT['status'] = 1
                RESULT['data']['msg'] = 'You have already nail game of this pk!'
            else:
                set_or_remove_nail(token, h5game, True)
        else:
            if not have_already_nail(token, h5game):
                RESULT['status'] = 1
                RESULT['data']['msg'] = 'You have not nail game of this pk!'
            else:
                set_or_remove_nail(token, h5game, False)
    except:
        RESULT['status'] = 1
        RESULT['data']['msg'] = 'Game of this pk doesn\'t exists!'

    return JsonHttpResponse(RESULT)


def topic(request, tp=''):
    token = request.GET.get('token', '')

    h5games = TopicGamesInfo.objects.filter(topic__tp=tp, status=True).order_by('-modify_at')
    h5games = [get_game_info(token, h5.h5game) for h5 in h5games]

    return JsonHttpResponse(
        dict(
            status=0,
            data=h5games,
        )
    )


def lunbotu(request):
    lunbotu = LunbotuInfo.objects.filter(status=True).order_by('-modify_at')
    lunbotu = [lbt.data for lbt in lunbotu]

    return JsonHttpResponse(
        dict(
            status=0,
            data=lunbotu,
        )
    )
