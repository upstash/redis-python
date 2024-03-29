from pytest import mark

from tests.execute_on_http import execute_on_http
from upstash_redis.asyncio import Redis


@mark.asyncio
async def test(async_redis: Redis) -> None:
    assert await async_redis.setbit("setbit", offset=4, value=1) == 0

    assert await execute_on_http("GETBIT", "setbit", "4") == 1
