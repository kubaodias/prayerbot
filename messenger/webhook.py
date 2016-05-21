#!/usr/bin/env python2
# -*- coding: UTF-8 -*-

import json
from utils import MessengerUtils as utils

class MessengerWebhook(object):

    @staticmethod
    def handle_message(sender, message):
        text = message['text']
        if text == 'modlitwa':
            response_message = utils.response_buttons(
                "Witaj user " + sender['id'] + "... Czego potrzebujesz?",
                [
                    {
                        "type":"postback",
                        "title":"Potrzebuję modlitwy",
                        "payload":"pomodl_sie_za_mnie"
                    },
                    {
                        "type":"postback",
                        "title":"Chcę się pomodlić",
                        "payload":"chce_sie_pomodlic"
                    }
                ]
            )
        else:
            response_message = utils.response_text("Bot echo: " + text)

        response = json.dumps({
            'recipient': { 'id' : sender['id'] },
            'message': response_message
        })
        return response

    @staticmethod
    def handle_postback(sender, postback):
        payload = postback['payload']
        if payload == 'pomodl_sie_za_mnie':
            response_message = utils.response_text('Jaka jest Twoja intencja?')
        elif payload == 'chce_sie_pomodlic':
            response_message = utils.response_text('TODO')

        response = json.dumps({
            'recipient': { 'id' : sender['id'] },
            'message': response_message
        })
        return response
