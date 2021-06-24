from django.core.management.base import BaseCommand, CommandError
import requests
from app import models, settings



class Command(BaseCommand):


    def get_all_slack_channels(self):
        list_of_all_channels_response = requests.get(
        'https://slack.com/api/conversations.list',
        headers=settings.auth_headers
        )
        json_data = list_of_all_channels_response.json()
        # if 'error' in json_data:
        #     print(json_data['error'])
        channels=json_data['channels']
        return channels

    def slack_db_migration(self):
        slack_channels=self.get_all_slack_channels()
        db_channels=models.Channel.objects.all()
        db_channel_ids=[channel.slack_id for channel in db_channels]
        for sl_channel in slack_channels:
            if sl_channel['id'] not in db_channel_ids:
                channel=models.Channel(title=sl_channel['name'],slack_id=sl_channel['id'])
                channel.save() 



    def handle(self, *args, **options):
        self.slack_db_migration()
        # print('mycomansoad')