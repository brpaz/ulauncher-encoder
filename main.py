"""
Ulauncher Encoder extension
"""
import logging
import base64
import urllib
import html
from ulauncher.api.client.Extension import Extension
from ulauncher.api.client.EventListener import EventListener
from ulauncher.api.shared.event import KeywordQueryEvent
from ulauncher.api.shared.item.ExtensionResultItem import ExtensionResultItem
from ulauncher.api.shared.action.RenderResultListAction import RenderResultListAction
from ulauncher.api.shared.action.CopyToClipboardAction import CopyToClipboardAction

LOGGER = logging.getLogger(__name__)

class EncoderExtension(Extension):
    """ Main Extension class """

    def __init__(self):
        LOGGER.info('Starting Encoder Extension')
        super(EncoderExtension, self).__init__()
        self.subscribe(KeywordQueryEvent, KeywordQueryEventListener())

    def decode(self, text):
        """ Decode a string into multiple formats """

        try:
            decoded_base64 = base64.b64decode(text).decode()
        except: # pylint: disable=bare-except
            decoded_base64 = "Cannot decode input text as base64."

        try:
            decoded_url = urllib.parse.unquote_plus(text)
        except: # pylint: disable=bare-except
            decoded_url = "Cannot decode input text"

        decoded_html = html.unescape(text)

        try:
            decoded_hex = bytes.fromhex(text).decode()
        except ValueError:
            decoded_hex = "Cannot decode input text as hex string"

        return [
            ExtensionResultItem(icon='images/icon.png',
                                name=decoded_hex,
                                description='HEX Decoded',
                                highlightable=False,
                                on_enter=CopyToClipboardAction(decoded_hex)),
            ExtensionResultItem(icon='images/icon.png',
                                name=decoded_base64,
                                description='Base64 Decoded',
                                highlightable=False,
                                on_enter=CopyToClipboardAction(decoded_base64)),
            ExtensionResultItem(icon='images/icon.png',
                                name=decoded_url,
                                description='URL Decoded',
                                highlightable=False,
                                on_enter=CopyToClipboardAction(decoded_url)),
            ExtensionResultItem(icon='images/icon.png',
                                name=decoded_html,
                                description='HTML Decoded',
                                highlightable=False,
                                on_enter=CopyToClipboardAction(decoded_html))
        ]

    def encode(self, text):
        """ Encodes a string into multiple formats """

        encoded_base64 = base64.b64encode(bytes(text, "utf-8")).decode("utf-8")
        encoded_url = urllib.parse.quote_plus(text)
        encoded_html = html.escape(text)
        encoded_hex = text.encode().hex().upper()

        return [
            ExtensionResultItem(icon='images/icon.png',
                                name=encoded_hex,
                                description='HEX Encoded',
                                highlightable=False,
                                on_enter=CopyToClipboardAction(encoded_hex)),
            ExtensionResultItem(icon='images/icon.png',
                                name=encoded_base64,
                                description='Base64 Encoded',
                                highlightable=False,
                                on_enter=CopyToClipboardAction(encoded_base64)),
            ExtensionResultItem(icon='images/icon.png',
                                name=encoded_url,
                                description='URL Encoded',
                                highlightable=False,
                                on_enter=CopyToClipboardAction(encoded_url)),
            ExtensionResultItem(icon='images/icon.png',
                                name=encoded_html,
                                description='HTML Encoded',
                                highlightable=False,
                                on_enter=CopyToClipboardAction(encoded_html))
        ]


class KeywordQueryEventListener(EventListener):
    """ Handles input events """
    def on_event(self, event, extension):
        """ Handles event """
        items = []

        text = event.get_argument() or ""
        if event.get_keyword() == "encode":
            items = extension.encode(text)
        else:
            items = extension.decode(text)

        return RenderResultListAction(items)


if __name__ == '__main__':
    EncoderExtension().run()
