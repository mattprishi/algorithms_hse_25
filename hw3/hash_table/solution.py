from typing import Generic, Iterable, Iterator, List, MutableMapping, Optional, Tuple, TypeVar, Union


K = TypeVar("K")
V = TypeVar("V")


class HashTable(Generic[K, V], MutableMapping[K, V]):
    """
    A list-backed hash table with separate chaining and dynamic resizing.

    - Buckets are lists of [key, value] pairs; empty buckets are stored as None.
    - Collisions are handled via chaining (per-bucket lists).
    - Table grows when load factor exceeds threshold; can shrink on heavy deletions.

    Only built-in lists are used for storage of buckets and entries.
    """

    __slots__ = ("_buckets", "_size", "_capacity", "_load_factor", "_min_capacity")

    def __init__(self, initial_capacity: int = 8, load_factor: float = 0.75) -> None:
        if initial_capacity < 4:
            initial_capacity = 4
        if not (0.25 <= load_factor <= 0.95):
            raise ValueError("load_factor must be between 0.25 and 0.95")

        # Use plain Python lists for buckets
        self._capacity: int = int(initial_capacity)
        self._buckets: List[Optional[List[List[object]]]] = [None] * self._capacity
        self._size: int = 0
        self._load_factor: float = load_factor
        self._min_capacity: int = self._capacity

    # Introspection
    @property
    def capacity(self) -> int:
        """Current number of buckets."""
        return self._capacity

    def __len__(self) -> int:  # type: ignore[override]
        return self._size

    def __contains__(self, key: object) -> bool:  # type: ignore[override]
        idx = self._index_for_key(key)
        bucket = self._buckets[idx]
        if bucket is None:
            return False
        for pair in bucket:
            if pair[0] == key:
                return True
        return False

    # Core operations
    def _index_for_key(self, key: object) -> int:
        # Will raise TypeError for unhashable keys, which is desired
        h = hash(key)
        # Make index non-negative and within capacity
        return (h & 0x7FFFFFFF) % self._capacity

    def _maybe_resize_up(self) -> None:
        if self._size > int(self._capacity * self._load_factor):
            self._resize(self._capacity * 2)

    def _maybe_resize_down(self) -> None:
        # Shrink if load < 0.2, but never below min_capacity
        if self._capacity > self._min_capacity and self._size * 5 < self._capacity:
            new_capacity = max(self._min_capacity, max(4, self._capacity // 2))
            # Avoid thrashing: only shrink if still below 0.4 after halving
            if self._size * 5 < new_capacity * 2:
                self._resize(new_capacity)

    def _resize(self, new_capacity: int) -> None:
        old_buckets = self._buckets
        self._capacity = int(new_capacity)
        self._buckets = [None] * self._capacity
        old_size = self._size
        self._size = 0

        for bucket in old_buckets:
            if bucket is None:
                continue
            for pair in bucket:
                # Reinsert into new buckets
                self._insert_pair(pair[0], pair[1])

        # size should remain the same after rehashing
        self._size = old_size

    def _insert_pair(self, key: object, value: object) -> bool:
        """Insert or update a key-value pair. Returns True if new key was added."""
        idx = self._index_for_key(key)
        bucket = self._buckets[idx]
        if bucket is None:
            bucket = []
            self._buckets[idx] = bucket
        # Update if key exists
        for pair in bucket:
            if pair[0] == key:
                pair[1] = value
                return False  # existing key updated
        # Insert new pair
        bucket.append([key, value])
        return True  # new key added

    def __setitem__(self, key: K, value: V) -> None:  # type: ignore[override]
        is_new = self._insert_pair(key, value)
        if is_new:
            self._size += 1
            self._maybe_resize_up()

    # Provide explicit method names as well
    def put(self, key: K, value: V) -> None:
        self[key] = value

    def set(self, key: K, value: V) -> None:
        self[key] = value

    def __getitem__(self, key: K) -> V:  # type: ignore[override]
        idx = self._index_for_key(key)
        bucket = self._buckets[idx]
        if bucket is None:
            raise KeyError(key)
        for pair in bucket:
            if pair[0] == key:
                return pair[1]  # type: ignore[return-value]
        raise KeyError(key)

    def get(self, key: K, default: Optional[V] = None) -> Optional[V]:  # type: ignore[override]
        try:
            return self[key]
        except KeyError:
            return default

    def pop(self, key: K, default: object = ...):  # type: ignore[override]
        try:
            value = self[key]
        except KeyError:
            if default is ...:
                raise
            return default
        del self[key]
        return value

    def __delitem__(self, key: K) -> None:  # type: ignore[override]
        idx = self._index_for_key(key)
        bucket = self._buckets[idx]
        if bucket is None:
            raise KeyError(key)
        for i, pair in enumerate(bucket):
            if pair[0] == key:
                # Remove by index to keep list type
                bucket.pop(i)
                self._size -= 1
                if not bucket:
                    self._buckets[idx] = None
                self._maybe_resize_down()
                return
        raise KeyError(key)

    def clear(self) -> None:  # type: ignore[override]
        self._buckets = [None] * self._capacity
        self._size = 0

    def update(self, other: Optional[Union[Iterable[Tuple[K, V]], MutableMapping[K, V]]] = None, **kwargs: V) -> None:  # type: ignore[override]
        if other is not None:
            if hasattr(other, "items"):
                for k, v in other.items():  # type: ignore[attr-defined]
                    self[k] = v
            else:
                for k, v in other:
                    self[k] = v
        for k, v in kwargs.items():
            self[k] = v

    # Iteration helpers
    def __iter__(self) -> Iterator[K]:  # type: ignore[override]
        return self.keys()

    def keys(self) -> Iterator[K]:  # type: ignore[override]
        for bucket in self._buckets:
            if bucket is None:
                continue
            for pair in bucket:
                yield pair[0]  # type: ignore[yield-type]

    def values(self) -> Iterator[V]:  # type: ignore[override]
        for bucket in self._buckets:
            if bucket is None:
                continue
            for pair in bucket:
                yield pair[1]  # type: ignore[yield-type]

    def items(self) -> Iterator[Tuple[K, V]]:  # type: ignore[override]
        for bucket in self._buckets:
            if bucket is None:
                continue
            for pair in bucket:
                yield (pair[0], pair[1])  # type: ignore[misc]

    # Utility
    def load(self) -> float:
        """Return current load factor (size / capacity)."""
        return 0.0 if self._capacity == 0 else self._size / self._capacity


