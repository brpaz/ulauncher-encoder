from encoder.strategy.base import BaseEncoder
from encoder.strategy.types import ENCODER_TYPE_HTML
import html


class HtmlEncoder(BaseEncoder):

    def get_type(self):
        return ENCODER_TYPE_HTML

    def get_formatted_type(self):
        return "Html"

    def encode(self, text):
        return html.escape(text)

    def decode(self, text):
        return html.unescape(text)
