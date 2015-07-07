class StringSet(object):

    def __init__(self, collection):
        if not isinstance(collection, set):
            raise TypeError("collection parameter should be a set instance")
        self.collection = collection

    def add(self, string):
        strip_string = string.strip()
        self.collection.add(strip_string)

    def remove(self, string):
        strip_string = string.strip()
        if strip_string in self.collection:
            self.collection.remove(strip_string)

    def parse(self, string):
        pass

    def clean(self):
        pass

    def __iter__(self):
        pass

    def __contains__(self):
        pass

    def __str__(self):
        pass
