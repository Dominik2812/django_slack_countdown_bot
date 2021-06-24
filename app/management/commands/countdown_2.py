from django.core.management.base import BaseCommand, CommandError
import requests
from app import models, settings
from time import sleep
import datetime
from django.http import HttpResponseRedirect
from django.shortcuts import render
# from polls.models import Question as Poll


class Command(BaseCommand):

    def db_to_slack_migration(self):
        db_countdowns=models.CountDown.objects.all()
        for countdown in db_countdowns:
            if countdown.slack_timestamp =="not migrated yet":
                channel_id=models.Channel.objects.filter(title=countdown.channel)[0].slack_id
                timestamp=self.sendMessage(countdown.c_happening,channel_id)
                countdown.slack_timestamp=timestamp
                countdown.save()

    def choose_channel(self,contains):
        list_of_all_channels_response = requests.get(
        'https://slack.com/api/conversations.list',
        headers=settings.auth_headers
        )
        json_data = list_of_all_channels_response.json()
        channels=json_data['channels']
        desired_channel_id=[channel['id'] for channel in channels if channel['name']==contains] [0]
        return desired_channel_id


    def sendMessage(self,message, channel_id):
        try:
            response = requests.post(
            'https://slack.com/api/chat.postMessage',
            headers=settings.auth_headers,
            json={'channel': channel_id, 'text': message},
            )
            return(response.json()['ts'])
        except:
            settings.error=True
            return 
            #HttpResponseRedirect('error')


    def sendUpDateToSlack(self,channel_id,timestamp,new_text):
        response = requests.post(
        'https://slack.com/api/chat.update',
        headers=settings.auth_headers,
        json={'channel': channel_id, 'ts': timestamp, 'text': f'{new_text}!'},
        )
        return response.json()

    def countdown(self, channel_id, timestamp, countdown):
        event=countdown.c_happening
        start=datetime.datetime.strptime(str(countdown.c_start).split("+")[0], '%Y-%m-%d %H:%M:%S')
        now=datetime.datetime.strptime(str(datetime.datetime.now()).split(".")[0], '%Y-%m-%d %H:%M:%S')
        delta=start-now
        if '-1' in str(delta):
            countdown.c_status = 'done' 
            countdown.save()
            end_message="der Countdown ist abgelaufen"
            self.sendUpDateToSlack(channel_id,timestamp,end_message)
            return

        new_text=f'{event} starts in{delta} seconds'
        self.sendUpDateToSlack(channel_id,timestamp,new_text)


    def handle(self, *args, **options):
        while True:
            countdowns_to_delete=models.CountDown.objects.filter(c_status="deleting")
            countdowns_to_start=models.CountDown.objects.filter(c_status="upcoming").order_by('c_start')
            for countdown in countdowns_to_start:
                if countdown.slack_timestamp=="not migrated yet":
                    self.db_to_slack_migration()
                channel_id=models.Channel.objects.filter(title=countdown.channel)[0].slack_id
                timestamp=countdown.slack_timestamp
                self.countdown(channel_id, timestamp,countdown)

            for countdown in countdowns_to_delete:
                channel_id=models.Channel.objects.filter(title=countdown.channel)[0].slack_id
                timestamp=countdown.slack_timestamp
                self.sendUpDateToSlack(channel_id,timestamp,'countdown was deleted')
                countdown.c_status="deleted"
                countdown.save()


            if len(countdowns_to_start)==0 and len(countdowns_to_delete)==0:
                print('found nothing, sleeping')
                sleep(1)
                continue

            sleep(1)




