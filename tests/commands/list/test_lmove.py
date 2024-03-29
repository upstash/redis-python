import pytest

from upstash_redis import Redis


@pytest.fixture(autouse=True)
def flush_mylists(redis: Redis):
    mylists = ["mylist1", "mylist2", "mylist3", "mylist4", "mylist5", "mylist6"]

    for mylist in mylists:
        redis.delete(mylist)


def test_lmove_existing_key(redis: Redis):
    source = "mylist1"
    destination = "mylist2"
    values = ["value1", "value2", "value3"]

    redis.rpush(source, *values)

    result = redis.lmove(source, destination, "LEFT")
    assert result == "value1"
    assert redis.lrange(source, 0, -1) == ["value2", "value3"]
    assert redis.lrange(destination, 0, -1) == ["value1"]

    redis.delete(source)
    redis.delete(destination)


def test_lmove_nonexistent_key(redis: Redis):
    source = "mylist2"
    destination = "mylist3"

    result = redis.lmove(source, destination, "LEFT")
    assert result is None

    redis.delete(destination)


def test_lmove_invalid_direction(redis: Redis):
    source = "mylist3"
    destination = "mylist4"
    values = ["value1", "value2", "value3"]

    redis.rpush(source, *values)

    with pytest.raises(Exception):
        redis.lmove(source, destination, "INVALID_DIRECTION")  # type: ignore[arg-type]

    redis.delete(source)


def test_lmove_same_source_and_destination(redis: Redis):
    source = "mylist5"
    destination = "mylist6"
    values = ["value1", "value2", "value3"]

    redis.rpush(source, *values)

    result = redis.lmove(source, destination, "LEFT")
    assert result == "value1"
    assert redis.lrange(source, 0, -1) == ["value2", "value3"]
    assert redis.lrange(destination, 0, -1) == ["value1"]

    redis.delete(source)
    redis.delete(destination)
