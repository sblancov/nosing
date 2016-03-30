class StringSet(object):
    ''' This class allows to parse a list of comma separated strings '''

    def __init__(self, collection):
        ''' Constructor
            - collection: It has to be a set.
        '''
        if not isinstance(collection, set):
            raise TypeError("collection parameter should be a set instance")
        self.collection = collection

    def add(self, string):
        '''Receives 'string', it is stripped and added to the list
            - string: A string that is stripped before to be added to list
        '''
        self.__add_strip_string(string)

    def remove(self, string):
        ''' Remove 'string' from the list
            - string: A string that will be remove if it exists
        '''
        strip_string = string.strip()
        if strip_string in self.collection:
            self.collection.remove(strip_string)

    def parse(self, string):
        ''' Receives a list of comma separated strings and process it
            - string: A string that contains comma separated strings
        '''
        split_string = string.split(',')
        for item in split_string:
            self.__add_strip_string(item)

    def clean(self):
        ''' Remove all the strings '''
        self.collection.clear()

    def __iter__(self):
        for item in self.collection:
            yield item

    def __contains__(self, item):
        strip_string = item.strip()
        return strip_string in self.collection

    def __unicode__(self):
        return unicode(', '.join(sorted(self.collection)))

    def __add_strip_string(self, string):
        strip_string = string.strip()
        self.collection.add(strip_string)
