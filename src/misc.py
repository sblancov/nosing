class StringSet(object):

    def __init__(self, collection):
        if not isinstance(collection, set):
            raise TypeError("collection parameter should be a set instance")
        self.collection = collection

    def add(self, string):
        self.__add_strip_string(string)

    def remove(self, string):
        strip_string = string.strip()
        if strip_string in self.collection:
            self.collection.remove(strip_string)

    def parse(self, string):
        split_string = string.split(',')
        for item in split_string:
            self.__add_strip_string(item)

    def clean(self):
        self.collection.clear()

    def __iter__(self):
        pass

    def __contains__(self, item):
        return item in self.collection

    def __unicode__(self):
        return unicode(', '.join(sorted(self.collection)))

    def __add_strip_string(self, string):
        strip_string = string.strip()
        self.collection.add(strip_string)
