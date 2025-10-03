import pytest

from .solution import HashTable


def test_insert_and_get_basic():
    ht = HashTable()
    ht["a"] = 1
    ht["b"] = 2
    assert ht["a"] == 1
    assert ht.get("b") == 2
    assert ht.get("c") is None
    assert len(ht) == 2


def test_update_value():
    ht = HashTable()
    ht["key"] = 1
    ht["key"] = 5
    assert ht["key"] == 5
    assert len(ht) == 1


def test_contains_and_delete():
    ht = HashTable()
    ht["x"] = 42
    assert "x" in ht
    del ht["x"]
    assert "x" not in ht
    with pytest.raises(KeyError):
        _ = ht["x"]


def test_pop_with_default():
    ht = HashTable()
    assert ht.pop("missing", 123) == 123
    ht[1] = 2
    assert ht.pop(1) == 2
    assert 1 not in ht


def test_iter_keys_values_items():
    ht = HashTable()
    data = {"a": 1, "b": 2, "c": 3}
    for k, v in data.items():
        ht[k] = v
    assert set(ht.keys()) == set(data.keys())
    assert set(ht.values()) == set(data.values())
    assert set(ht.items()) == set(data.items())


def test_resize_growth_and_access():
    ht = HashTable(initial_capacity=4, load_factor=0.75)
    n = 100
    for i in range(n):
        ht[i] = i * 2
    assert len(ht) == n
    for i in range(n):
        assert ht[i] == i * 2
    assert ht.capacity >= n // 2  # should have resized


def test_resize_shrink_on_deletes():
    ht = HashTable(initial_capacity=16, load_factor=0.75)
    for i in range(64):
        ht[i] = i
    cap_after_inserts = ht.capacity
    for i in range(64):
        del ht[i]
    assert len(ht) == 0
    # allow some shrink, but not below min capacity (initial)
    assert ht.capacity >= 16
    assert ht.capacity <= cap_after_inserts


def test_collision_handling_with_custom_hash():
    class BadHash:
        def __init__(self, value):
            self.value = value

        def __hash__(self):
            return 1  # force collisions

        def __eq__(self, other):
            return isinstance(other, BadHash) and self.value == other.value

    ht = HashTable(initial_capacity=4)
    keys = [BadHash(i) for i in range(10)]
    for i, k in enumerate(keys):
        ht[k] = i
    for i, k in enumerate(keys):
        assert ht[k] == i
    assert len(ht) == len(keys)


def test_get_and_default():
    ht = HashTable()
    assert ht.get("missing") is None
    assert ht.get("missing", 0) == 0
    ht["present"] = 10
    assert ht.get("present", 0) == 10


def test_clear():
    ht = HashTable()
    for i in range(10):
        ht[i] = i
    ht.clear()
    assert len(ht) == 0
    for i in range(10):
        with pytest.raises(KeyError):
            _ = ht[i]


def test_update_from_iterable_and_mapping():
    ht = HashTable()
    ht.update({"a": 1, "b": 2})
    assert ht["a"] == 1 and ht["b"] == 2
    ht.update([("c", 3), ("a", 5)])
    assert ht["c"] == 3 and ht["a"] == 5
    ht.update(d=7, e=8)
    assert ht["d"] == 7 and ht["e"] == 8


def test_errors_on_missing_delete_and_getitem():
    ht = HashTable()
    with pytest.raises(KeyError):
        del ht["nope"]
    with pytest.raises(KeyError):
        _ = ht["nope"]


