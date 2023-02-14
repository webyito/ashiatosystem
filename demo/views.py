from re import template
from django.shortcuts import render, redirect
from django.views.generic import View
from django.conf import settings
from django.core.mail import BadHeaderError, EmailMessage, send_mail
from django.http import HttpResponse
import textwrap
import urllib.parse
import gspread
from google.oauth2.service_account import Credentials
import datetime
from ashiatosystem.settings import BASE_DIR
import os

class IndexView(View):

    def get(self, request, *args, **kwargs):

        url = request.build_absolute_uri()
        qs = urllib.parse.urlparse(url).query
        #あしあと発行桁数に応じて数字を変える、9999までは-4で統一
        id = qs[-4:]

        dt_now = datetime.datetime.now()
        tstr = dt_now.strftime('%Y-%m-%d %H:%M:%S')

        path = os.getcwd()

        scope = ['https://www.googleapis.com/auth/spreadsheets','https://www.googleapis.com/auth/drive']
        credentials = Credentials.from_service_account_file(path + '/ashiatosystem.pythonanywhere.com/demo/my-project-ashiato-a46161a2b295.json', scopes=scope)
        gc = gspread.authorize(credentials)

        SPREADSHEET_KEY = '1PUyAkuStUb0osDVGNrEeBDN5oGiyP7rEIN-PnYIqXy8'
        workbook = gc.open_by_key(SPREADSHEET_KEY)

        worksheet = workbook.worksheet('アクセス履歴')

        def next_available_row(worksheet):
                str_list = list(filter(None, worksheet.col_values(1)))
                return str(len(str_list)+1)

        next_row = next_available_row(worksheet)

        worksheet.update_cell(next_row, 1, tstr)
        worksheet.update_cell(next_row, 2, id)

        #subject = "【あしあと】貴社サイトにアクセスがありました"
        #message = id
        #from_email = "decube.ashiato@gmail.com"
        #送信先メールアドレス、複数設定の場合は「,」で区切る
        #recipient_list = ["web.decube@gmail.com"]
        #try:
            #send_mail(subject, message, from_email, recipient_list)
        #except BadHeaderError:
            #return HttpResponse('無効なヘッダが検出されました。')
        #アプリ名/に書き換える

        return render(request, 'demo/redirect.html')
    template_name = 'index.html'

class RedirectView(View):
    template_name = 'redirect.html'