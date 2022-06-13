import logging
from ulauncher.api.client.Extension import Extension
from ulauncher.api.shared.event import KeywordQueryEvent
from ulauncher.api.shared.item.ExtensionResultItem import ExtensionResultItem
from ulauncher.api.shared.action.CopyToClipboardAction import CopyToClipboardAction
from encoder.listeners.query_listener import KeywordQueryEventListener
from encoder.strategy.base64 import Base64Encoder
from encoder.strategy.html import HtmlEncoder
from encoder.strategy.url import UrlEncoder

LOGGER = logging.getLogger(__name__)


class EncoderExtension(Extension):
    """ Main Extension class """

    def __init__(self):
        """ Initialize the extension """
        LOGGER.info('Starting Encoder Extension')
        super(EncoderExtension, self).__init__()
        self.subscribe(KeywordQueryEvent, KeywordQueryEventListener())
        self.strategies = [Base64Encoder(), HtmlEncoder(), UrlEncoder()]
        self.icon_path = 'images/icon.png'

    def get_encoder_strategy(self, type):
        """ Returns the encoding strategy for the given type"""
        for strategy in self.strategies:
            if strategy.get_type() == type:
                return strategy

        raise RuntimeError("Unknown encoding strategy type: %s" % type)

    def encode(self, text, type=None):
        """Encodes the specified text"""

        items = []
        if type is not None:
            strategy = self.get_encoder_strategy(type)

            try:
                encoded_text = strategy.encode(text)
            except Exception:
                encoded_text = "Cannot encode text as {}".format(
                    strategy.get_formatted_type())

            items = [
                ExtensionResultItem(
                    icon=self.icon_path,
                    name=encoded_text,
                    description=strategy.get_formatted_type(),
                    highlightable=False,
                    on_enter=CopyToClipboardAction(encoded_text))
            ]
        else:
            for strategy in self.strategies:
                try:
                    encoded_text = strategy.encode(text)
                except Exception:
                    encoded_text = "Cannot encode text as {}".format(
                        strategy.get_formatted_type())
                items.append(
                    ExtensionResultItem(
                        icon=self.icon_path,
                        name=encoded_text,
                        description=strategy.get_formatted_type(),
                        highlightable=False,
                        on_enter=CopyToClipboardAction(encoded_text)))

        return items

    def decode(self, text, type=None):
        """Decodes the specified text"""

        items = []
        if type is not None:
            strategy = self.get_encoder_strategy(type)

            try:
                decoded_text = strategy.decode(text)
            except Exception:
                decoded_text = "Cannot decode text as {}".format(
                    strategy.get_formatted_type())

            items = [
                ExtensionResultItem(
                    icon=self.icon_path,
                    name=decoded_text,
                    description=strategy.get_formatted_type(),
                    highlightable=False,
                    on_enter=CopyToClipboardAction(decoded_text))
            ]
        else:
            for strategy in self.strategies:
                try:
                    decoded_text = strategy.decode(text)
                except Exception:
                    decoded_text = "Cannot decode text as {}".format(
                        strategy.get_formatted_type())
                items.append(
                    ExtensionResultItem(
                        icon=self.icon_path,
                        name=decoded_text,
                        description=strategy.get_formatted_type(),
                        highlightable=False,
                        on_enter=CopyToClipboardAction(decoded_text)))

        return items
