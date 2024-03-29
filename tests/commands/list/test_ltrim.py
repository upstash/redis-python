import pytest

from upstash_redis import Redis


@pytest.fixture(autouse=True)
def flush_mylist(redis: Redis):
    mylist = "mylist"

    redis.delete(mylist)


def test_ltrim_with_positive_indices(redis: Redis):
    mylist = "mylist"
    values = ["value1", "value2", "value3", "value4", "value5"]

    redis.rpush(mylist, *values)

    redis.ltrim(mylist, 1, 3)

    expected_list = ["value2", "value3", "value4"]
    assert redis.lrange(mylist, 0, -1) == expected_list


def test_ltrim_with_negative_indices(redis: Redis):
    mylist = "mylist"
    values = ["value1", "value2", "value3", "value4", "value5"]

    redis.rpush(mylist, *values)

    redis.ltrim(mylist, -3, -2)

    expected_list = ["value3", "value4"]
    assert redis.lrange(mylist, 0, -1) == expected_list
