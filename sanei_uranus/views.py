from re import template
from django.shortcuts import render, redirect
from django.views.generic import View
from django.conf import settings
from django.core.mail import BadHeaderError, EmailMessage, send_mail
from django.http import HttpResponse
import textwrap
import urllib.parse


class IndexView(View):

    def get(self, request, *args, **kwargs):
        url = request.build_absolute_uri()
        qs = urllib.parse.urlparse(url).query
        #あしあと発行桁数に応じて数字を変える、9999までは-4で統一
        id = qs[-4:]

        subject = "【あしあと／5月開催ウラノス】貴社サイトにアクセスがありました"
        message = id
        from_email = "decube.ashiato.sub@gmail.com"
        #送信先メールアドレス、複数設定の場合は「,」で区切る
        #recipient_list = ["web.decube@gmail.com"]
        recipient_list = ["decube.ashiato.sub@gmail.com"]
        try:
            send_mail(subject, message, from_email, recipient_list)
        except BadHeaderError:
            return HttpResponse('無効なヘッダが検出されました。')
        #アプリ名/に書き換える
        return render(request, 'sanei_uranus/redirect.html')
    template_name = 'index.html'

class RedirectView(View):
    template_name = 'redirect.html'
