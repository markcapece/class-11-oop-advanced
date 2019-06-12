class OrderedDict(object):
    @classmethod
    def from_keys(cls, keys):
        new_dict = OrderedDict()
        for k in keys:
            new_dict[k] = None
        return new_dict

    def __init__(self):
        self._keys = []
        self._values = []
        self._items = []

    def keys(self):
        return self._keys

    def values(self):
        return self._values

    def items(self):
        self._items = list(zip(self._keys, self._values))
        return self._items

    def __setitem__(self, key, value):
        if key not in self.keys():
            self.keys().append(key)
            self.values().append(value)
            self.items().append((key, value))
        else:
            index = self.keys().index(key)
            self.values()[index] = value
            self.items()

    def __len__(self):
        return len(self.items())

    def __getitem__(self, key):
        for k, v in self.items():
            if k == key:
                return v
        raise KeyError

    def __delitem__(self, key):
        index = self.keys().index(key)
        self.keys().pop(index)
        self.values().pop(index)
        self.items().pop(index)

    def __contains__(self, key):
        return key in self.keys()

    def __eq__(self, other):
        return self.items() == list(other.items())

    def __str__(self):
        string_items = []
        for k, v in self.items():
            string_items.append(f"{repr(k)}: {repr(v)}")
        return "{"+', '.join(string_items)+"}"

    def __repr__(self):
        return str(self)

    def __add__(self, other):
        new_dict = OrderedDict()
        all_keys = self.keys() + other.keys()
        all_values = self.values() + other.values()
        all_items = list(zip(all_keys, all_values))
        for k, v in all_items:
            new_dict[k] = v
        return new_dict
