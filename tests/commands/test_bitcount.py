from pytest import mark, raises
from tests.client import redis


@mark.asyncio
async def test_bitcount() -> None:
    async with redis:
        assert await redis.bitcount("string") == 17


@mark.asyncio
async def test_bitcount_with_interval() -> None:
    async with redis:
        assert await redis.bitcount("string", start=1, end=2) == 9

        with raises(Exception) as exception:
            await redis.bitcount("string", start=1)

        assert str(exception.value) == "Both \"start\" and \"end\" must be specified."

        with raises(Exception) as exception:
            await redis.bitcount("string", end=2)

        assert str(exception.value) == "Both \"start\" and \"end\" must be specified."