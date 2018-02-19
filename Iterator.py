class ClassCastException(Exception):
    pass


class TypedIterator(object):

    def __init__(self, it, type):
        self.imp = it
        self.type = type

    def hasNext(self):
        return self.imp.has_next()

    def remove(self):
        self.imp.remove()
        
    def next(self):
        obj = self.imp.next()
        if not type.isInstance(obj):
            raise ClassCastException(
              "TypedIterator for type " + type +
              " encountered type: " + obj.getClass())
        return obj
