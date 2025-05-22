class CustomSet:
    def __init__(self):
        self._elements = []

    def add(self, element):
        if not self.contains(element):
            self._elements.append(element)

    def contains(self, element):
        for item in self._elements:
            if item == element:
                return True
        return False

    def get_elements(self):
        return list(self._elements)

    def remove(self, element):
        try:
            self._elements.remove(element)
        except ValueError:
            raise ValueError(f"Element {element} not found in CustomSet")

    def __len__(self):
        return len(self._elements)

    def __iter__(self):
        return iter(self._elements)

    def __str__(self):
        return f"CustomSet({self._elements})"


class CustomHashTable:
    def __init__(self, size=101):
        self._size = size
        self._buckets = [[] for _ in range(self._size)]

    def _hash(self, key):
        return hash(key) % self._size

    def put(self, key, value):
        bucket_index = self._hash(key)
        bucket = self._buckets[bucket_index]
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return
        bucket.append((key, value))

    def get(self, key):
        bucket_index = self._hash(key)
        bucket = self._buckets[bucket_index]
        for k, v in bucket:
            if k == key:
                return v
        raise KeyError(f"Key '{key}' not found")

    def remove(self, key):
        bucket_index = self._hash(key)
        bucket = self._buckets[bucket_index]
        for i, (k, v) in enumerate(bucket):
            if k == key:
                del bucket[i]
                return
        raise KeyError(f"Key '{key}' not found to remove")

    def __setitem__(self, key, value):
        self.put(key, value)

    def __getitem__(self, key):
        return self.get(key)

    def __delitem__(self, key):
        self.remove(key)

    def __str__(self):
        items = []
        for bucket in self._buckets:
            for k, v in bucket:
                items.append(f"{repr(k)}: {repr(v)}")
        return "CustomHashTable({" + ", ".join(items) + "})"

    def __len__(self):
        count = 0
        for bucket in self._buckets:
            count += len(bucket)
        return count