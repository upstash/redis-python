from pytest import mark, raises

from upstash_redis import AsyncRedis


@mark.asyncio
async def test(async_redis: AsyncRedis) -> None:
    assert await async_redis.exists("string", "hash") == 2


@mark.asyncio
async def test_without_keys(async_redis: AsyncRedis) -> None:
    with raises(Exception) as exception:
        await async_redis.exists()

    assert str(exception.value) == "At least one key must be checked."
