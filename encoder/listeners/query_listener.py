from ulauncher.api.client.EventListener import EventListener
from ulauncher.api.shared.action.RenderResultListAction import RenderResultListAction
from encoder.strategy.types import ENCODER_TYPE_BASE64, ENCODER_TYPE_HTML, ENCODER_TYPE_URL


class KeywordQueryEventListener(EventListener):
    """ Handles input events """

    def on_event(self, event, extension):
        """ Handles event """
        items = []

        text = event.get_argument() or ""
        keyword = event.get_keyword()
        if keyword == "encode":
            items = extension.encode(text)
        elif keyword == "decode":
            items = extension.decode(text)
        elif keyword == "b64:encode":
            items = extension.encode(text, ENCODER_TYPE_BASE64)
        elif keyword == "b64:decode":
            items = extension.decode(text, ENCODER_TYPE_BASE64)
        elif keyword == "html:encode":
            items = extension.encode(text, ENCODER_TYPE_HTML)
        elif keyword == "html:decode":
            items = extension.decode(text, ENCODER_TYPE_HTML)
        elif keyword == "url:encode":
            items = extension.encode(text, ENCODER_TYPE_URL)
        elif keyword == "url:decode":
            items = extension.decode(text, ENCODER_TYPE_URL)

        return RenderResultListAction(items)
