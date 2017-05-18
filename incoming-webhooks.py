# coding:utf-8
'''This program is class for incoming webhooks'''

import requests
import json


class IncomingWebhooks:
    """Incoming webhooks"""

    def __init__(self, url='', text=u'', username=u'', icon_emoji=u'', link_names=0):
        """Set Property"""
        self.url = url
        self.data = json.dumps({
            'text':         text,               # text
            'username':     username,           # user name
            'icon_emoji':   icon_emoji,         # profile emoji
            'link_names':   link_names,         # mention
        })

    def send(self):
        """Send to Slack"""
        # send
        requests.post(
            self.url,
            self.data
        )
