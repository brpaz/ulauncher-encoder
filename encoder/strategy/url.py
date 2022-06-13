from encoder.strategy.base import BaseEncoder
from encoder.strategy.types import ENCODER_TYPE_URL
import urllib.parse


class UrlEncoder(BaseEncoder):

    def get_type(self):
        return ENCODER_TYPE_URL

    def get_formatted_type(self):
        return "Url"

    def encode(self, text):
        return urllib.parse.quote(text)

    def decode(self, text):
        return urllib.parse.unquote(text)
