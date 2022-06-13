import base64
from encoder.strategy.base import BaseEncoder
from encoder.strategy.types import ENCODER_TYPE_BASE64


class Base64Encoder(BaseEncoder):

    def get_type(self):
        return ENCODER_TYPE_BASE64

    def get_formatted_type(self):
        return "Base64"

    def encode(self, text):
        return base64.b64encode(bytes(text, "utf-8")).decode("utf-8")

    def decode(self, text):
        return base64.b64decode(text).decode()
