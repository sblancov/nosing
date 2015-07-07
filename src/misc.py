class StringSet(object):

    def __init__(self, collection):
        if not isinstance(collection, set):
            raise TypeError("collection parameter should be a set instance")
        self.collection = collection

    def add(self, string):
        self.collection.add(string)

    def remove(self, string):
        pass

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
