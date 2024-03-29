import pytest

from upstash_redis import Redis


@pytest.fixture(autouse=True)
def flush_mylists(redis: Redis):
    mylists = ["mylist1", "mylist2", "mylist3", "mylist4"]

    for mylist in mylists:
        redis.delete(mylist)


def test_linsert_before_existing_value(redis: Redis):
    mylist = "mylist1"
    values = ["value1", "value2", "value3"]

    redis.rpush(mylist, *values)

    result = redis.linsert(mylist, "BEFORE", "value2", "new_value")
    assert result == 4
    assert redis.lrange(mylist, 0, -1) == ["value1", "new_value", "value2", "value3"]


def test_linsert_after_existing_value(redis: Redis):
    mylist = "mylist2"
    values = ["value1", "value2", "value3"]

    redis.rpush(mylist, *values)

    result = redis.linsert(mylist, "AFTER", "value2", "new_value")
    assert result == 4
    assert redis.lrange(mylist, 0, -1) == ["value1", "value2", "new_value", "value3"]


def test_linsert_before_nonexistent_value(redis: Redis):
    mylist = "mylist3"
    values = ["value1", "value2", "value3"]

    redis.rpush(mylist, *values)

    result = redis.linsert(mylist, "BEFORE", "value4", "new_value")
    assert result == -1
    assert redis.lrange(mylist, 0, -1) == ["value1", "value2", "value3"]


def test_linsert_after_nonexistent_value(redis: Redis):
    mylist = "mylist4"
    values = ["value1", "value2", "value3"]

    redis.rpush(mylist, *values)

    result = redis.linsert(mylist, "AFTER", "value4", "new_value")
    assert result == -1
    assert redis.lrange(mylist, 0, -1) == ["value1", "value2", "value3"]
