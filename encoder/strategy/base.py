class BaseEncoder(object):

    def get_type(self):
        raise NotImplementedError(
            "Implement this method on subclass instances")

    def encode(self, text):
        raise NotImplementedError(
            "Implement this method on subclass instances")

    def decode(self, text):
        raise NotImplementedError(
            "Implement this method on subclass instances")
