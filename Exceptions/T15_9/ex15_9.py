class ItemError(Exception):
    def __init__(self, item):
        self._item = item

    def __str__(self):
        return "Item {} doesn't belong this multi array".format(self._item)


class WrongDataType(Exception):
    def __init__(self, data_type):
        self._data_type = data_type

    def __str__(self):
        return "Class doesn't support this data type: {}".format(self._data_type)
