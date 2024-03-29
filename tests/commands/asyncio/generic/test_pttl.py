from pytest import mark

from tests.execute_on_http import execute_on_http
from upstash_redis.asyncio import Redis


@mark.asyncio
async def test(async_redis: Redis) -> None:
    await execute_on_http("EXPIRE", "string_for_ttl", "500")

    # < 1000 would rather indicate seconds.
    assert await async_redis.pttl("string_for_ttl") > 1000
