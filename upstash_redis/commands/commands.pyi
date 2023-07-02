

from upstash_redis.schema.commands.parameters import (
    BitFieldOffset,
    GeoMember,
    FloatMinMax,
)

from typing import Any, Iterable, Optional, Set, Tuple, Union, List, Literal, Dict

class Commands:
    def bitcount(
        self, key: str, start: Union[int, None] = None, end: Union[int, None] = None
    ) -> int: 
        ...

    def bitfield(self, key: str) -> "BitFieldCommands":
        ...

    def bitfield_ro(self, key: str) -> "BitFieldRO":
        ...

    def bitop(
        self, operation: Literal["AND", "OR", "XOR", "NOT"], destkey: str, *srckeys: str
    ) -> int:
        ...

    def bitpos(
        self,
        key: str,
        bit: Literal[0, 1],
        start: Union[int, None] = None,
        end: Union[int, None] = None,
    ) -> int:
        ...

    def getbit(self, key: str, offset: int) -> int:
        ...

    def setbit(self, key: str, offset: int, value: Literal[0, 1]) -> int:
        ...

    def ping(self, message: Union[str, None] = None) -> str:
        ...

    def echo(self, message: str) -> str:
        ...
    
    def copy(
        self, source: str, destination: str, replace: bool = False
    ) -> Union[Literal[1, 0], bool]:
        ...

    def delete(self, *keys: str) -> int:
        ...

    def exists(self, *keys: str) -> int:
        ...

    def expire(self, key: str, seconds: int) -> Union[Literal[1, 0], bool]:
        ...

    def expireat(
        self, key: str, unix_time_seconds: int
    ) -> Union[Literal[1, 0], bool]:
       ...

    def keys(self, pattern: str) -> List[str]:
        ...

    def persist(self, key: str) -> Union[Literal[1, 0], bool]:
        ...

    def pexpire(self, key: str, milliseconds: int) -> Union[Literal[1, 0], bool]:
        ...

    def pexpireat(
        self, key: str, unix_time_milliseconds: int
    ) -> Union[Literal[1, 0], bool]:
        ...

    def pttl(self, key: str) -> int:
        ...

    def randomkey(self) -> Union[str, None]:
        ...

    def rename(self, key: str, newkey: str) -> str:
        ...

    def renamenx(self, key: str, newkey: str) -> Union[Literal[1, 0], bool]:
        ...

    def scan(
        self,
        cursor: int,
        match_pattern: Union[str, None] = None,
        count: Union[int, None] = None,
        scan_type: Union[str, None] = None,
    ) -> Union[List[Union[str, List[str]]], List[Union[int, List[str]]]]:
        ...
    
    def touch(self, *keys: str) -> int:
        ...

    def ttl(self, key: str) -> int:
        ...

    def type(self, key: str) -> Union[str, None]:
        ...

    def unlink(self, *keys: str) -> int:
        ...

    def geoadd(
        self,
        key: str,
        *members: GeoMember,
        nx: bool = False,
        xx: bool = False,
        ch: bool = False,
    ) -> int:
        ...

    def geodist(
        self,
        key: str,
        member1: str,
        member2: str,
        unit: Literal["m", "km", "ft", "mi", "M", "KM", "FT", "MI"] = "M",
    ) -> Union[str, float, None]:
        ...

    def geohash(self, key: str, *members: str) -> List[Union[str, None]]:
        ...

    def geopos(
        self, key: str, *members: str
    ) -> Union[List[Union[List[str], None]], List[Union[Dict[str, float], None]]]:
        ...

    def georadius(
        self,
        key: str,
        longitude: float,
        latitude: float,
        radius: float,
        unit: Literal["m", "km", "ft", "mi", "M", "KM", "FT", "MI"],
        withdist: bool = False,
        withhash: bool = False,
        withcoord: bool = False,
        count: Union[int, None] = None,
        count_any: bool = False,
        sort: Union[Literal["ASC", "DESC"], None] = None,
        store: Union[str, None] = None,
        storedist: Union[str, None] = None,
    ) -> Union[List[Union[str, List[Union[str, List[str]]]]], List[Dict[str, Union[str, float, int]]], int]:
        ...

    def georadius_ro(
        self,
        key: str,
        longitude: float,
        latitude: float,
        radius: float,
        unit: Literal["m", "km", "ft", "mi", "M", "KM", "FT", "MI"],
        withdist: bool = False,
        withhash: bool = False,
        withcoord: bool = False,
        count: Union[int, None] = None,
        count_any: bool = False,
        sort: Union[Literal["ASC", "DESC"], None] = None,
    ) -> Union[List[Union[str, List[Union[str, List[str]]]]], List[Dict[str, Union[str, float, int]]]]:
        ...

    def georadiusbymember(
        self,
        key: str,
        member: str,
        radius: float,
        unit: Literal["m", "km", "ft", "mi", "M", "KM", "FT", "MI"],
        withdist: bool = False,
        withhash: bool = False,
        withcoord: bool = False,
        count: Union[int, None] = None,
        count_any: bool = False,
        sort: Union[Literal["ASC", "DESC"], None] = None,
        store: Union[str, None] = None,
        storedist: Union[str, None] = None,
    ) -> Union[List[Union[str, List[Union[str, List[str]]]]], List[Dict[str, Union[str, float, int]]], int]:
        ...

    def georadiusbymember_ro(
        self,
        key: str,
        member: str,
        radius: float,
        unit: Literal["m", "km", "ft", "mi", "M", "KM", "FT", "MI"],
        withdist: bool = False,
        withhash: bool = False,
        withcoord: bool = False,
        count: Union[int, None] = None,
        count_any: bool = False,
        sort: Union[Literal["ASC", "DESC"], None] = None,
    ) -> Union[List[Union[str, List[Union[str, List[str]]]]], List[Dict[str, Union[str, float, int]]]]:
        ...

    def geosearch(
        self,
        key: str,
        unit: Literal["m", "km", "ft", "mi", "M", "KM", "FT", "MI"],
        frommember: Union[str, None] = None,
        fromlonlat_longitude: Union[float, None] = None,
        fromlonlat_latitude: Union[float, None] = None,
        byradius: Union[float, None] = None,
        bybox_width: Union[float, None] = None,
        bybox_height: Union[float, None] = None,
        sort: Union[Literal["ASC", "DESC"], None] = None,
        count: Union[int, None] = None,
        count_any: bool = False,
        withdist: bool = False,
        withhash: bool = False,
        withcoord: bool = False,
    ) -> Union[List[Union[str, List[Union[str, List[str]]]]], List[Dict[str, Union[str, float, int]]]]:
        ...

    def geosearchstore(
        self,
        destination: str,
        source: str,
        unit: Literal["m", "km", "ft", "mi", "M", "KM", "FT", "MI"],
        frommember: Union[str, None] = None,
        fromlonlat_longitude: Union[float, None] = None,
        fromlonlat_latitude: Union[float, None] = None,
        byradius: Union[float, None] = None,
        bybox_width: Union[float, None] = None,
        bybox_height: Union[float, None] = None,
        sort: Union[Literal["ASC", "DESC"], None] = None,
        count: Union[int, None] = None,
        count_any: bool = False,
        storedist: bool = False,
    ) -> int:
        ...

    def hdel(self, key: str, *fields: str) -> int:
        ...

    def hexists(self, key: str, field: str) -> Union[Literal[1, 0], bool]:
        ...

    def hget(self, key: str, field: str) -> Union[str, None]:
        ...

    def hgetall(self, key: str) -> Union[List[str], Dict[str, str]]:
        ...

    def hincrby(self, key: str, field: str, increment: int) -> int:
        ...

    def hincrbyfloat(
        self, key: str, field: str, increment: float
    ) -> Union[str, float]:
        ...

    def hkeys(self, key: str) -> List[str]:
        ...

    def hlen(self, key: str) -> int:
        ...

    def hmget(self, key: str, *fields: str) -> List[Union[str, None]]:
        ...

    def hmset(self, key: str, field_value_pairs: Dict) -> str:
        ...

    def hrandfield(
        self, key: str, count: Union[int, None] = None, withvalues: bool = False
    ):
        ...

    def hscan(
        self,
        name: str,
        cursor: int,
        match_pattern: Union[str, None] = None,
        count: Union[int, None] = None,
    ) -> Tuple[int, Dict[str, str]]:
        ...

    def hset(self, name: str, key: Optional[str] = None, val: Optional[str] = None, field_value_pairs: Optional[Dict] = None) -> int:
        ...

    def hsetnx(
        self, key: str, field: str, value: Any
    ) -> Union[Literal[1, 0], bool]:
        ...

    def hstrlen(self, key: str, field: str) -> int:
        ...

    def hvals(self, key: str) -> List[str]:
        ...

    def pfadd(self, key: str, *elements: Any) -> Union[Literal[1, 0], bool]:
        ...

    def pfcount(self, *keys: str) -> int:
        ...

    def pfmerge(self, destkey: str, *sourcekeys: str) -> str:
        ...

    def lindex(self, key: str, index: int) -> Union[str, None]:
        ...

    def linsert(
        self, key: str, position: Literal["BEFORE", "AFTER", "before", "after"], pivot: Any, element: Any
    ) -> int:
       ...

    def llen(self, key: str) -> int:
        ...

    def lmove(
        self,
        source: str,
        destination: str,
        source_position: Literal["LEFT", "RIGHT"] = "LEFT",
        destination_position: Literal["LEFT", "RIGHT"] = "RIGHT",
    ) -> Union[str, None]:
        ...

    def lpop(
        self, key: str, count: Union[int, None] = None
    ) -> Union[(Union[str, None]), List[str]]:
        ...

    def lpos(
        self,
        key: str,
        element: Any,
        rank: Union[int, None] = None,
        count: Union[int, None] = None,
        maxlen: Union[int, None] = None,
    ) -> Union[(Union[int, None]), List[int]]:
        ...

    def lpush(self, key: str, *elements: Any) -> int:
        ...

    def lpushx(self, key: str, *elements: Any) -> int:
        ...

    def lrange(self, key: str, start: int, stop: int) -> List[str]:
        ...

    def lrem(self, key: str, count: int, element: Any) -> int:
        ...

    def lset(self, key: str, index: int, element: Any) -> str:
        ...

    def ltrim(self, key: str, start: int, stop: int) -> str:
        ...

    def rpop(
        self, key: str, count: Union[int, None] = None
    ) -> Union[(Union[str, None]), List[str]]:
        ...

    def rpoplpush(self, source: str, destination: str) -> Union[str, None]:
        ...

    def rpush(self, key: str, *elements: Any) -> int:
        ...

    def rpushx(self, key: str, *elements: Any) -> int:
        ...

    def publish(self, channel: str, message: str) -> int:
        ...

    def eval(
        self,
        script: str,
        keys: Union[List[str], None] = None,
        args: Union[List, None] = None,
    ) -> Any:
        ...

    def evalsha(
        self,
        sha1: str,
        keys: Union[List[str], None] = None,
        args: Union[List, None] = None,
    ) -> Any:
        ...

    def dbsize(self) -> int:
        ...

    def flushall(self, mode: Union[Literal["ASYNC", "SYNC"], None] = None) -> Union[str, bool]:
        ...

    def flushdb(self, mode: Union[Literal["ASYNC", "SYNC"], None] = None) -> Union[str, bool]:
        ...

    def time(self) -> Union[List[str], Dict[str, int]]:
        ...

    def sadd(self, key: str, *members: Any) -> int:
        ...

    def scard(self, key: str) -> int:
        ...

    def sdiff(self, *keys: str) -> Set[str]:
        ...

    def sdiffstore(self, destination: str, *keys: str) -> int:
        ...

    def sinter(self, *keys: str) -> Set[str]:
        ...

    def sinterstore(self, destination: str, *keys: str) -> int:
        ...

    def sismember(self, key: str, member: Any) -> Union[Literal[1, 0], bool]:
        ...

    def smismember(self, key: str, *members: Any) -> Union[List[Literal[1, 0]], List[bool]]:
        ...
        
    def smembers(self, key: str) -> Set[str]:
        ...

    def smove(
        self, source: str, destination: str, member: Any
    ) -> Union[Literal[1, 0], bool]:
        ...

    def spop(
        self, key: str, count: Union[int, None] = None
    ) -> Union[(Union[str, None]), List[str]]:
        ...

    def srandmember(
        self, key: str, count: Union[int, None] = None
    ) -> Union[(Union[str, None]), List[str]]:
        ...

    def srem(self, key: str, *members: Any) -> int:
        ...

    def sscan(
        self,
        key: str,
        cursor: int = 0,
        match_pattern: Union[str, None] = None,
        count: Union[int, None] = None,
    ) -> Tuple[int, List[str]]:
        ...

    def sunion(self, *keys: str) -> Set[str]:
        ...

    def sunionstore(self, destination: str, *keys: str) -> int:
        ...

    def zadd(
        self,
        key: str,
        score_member_pairs: Dict,
        nx: bool = False,
        xx: bool = False,
        gt: bool = False,
        lt: bool = False,
        ch: bool = False,
        incr: bool = False,
    ) -> Union[int, (Union[str, None, float])]:
        ...
    
    def zcard(self, key: str) -> int:
        ...

    def zcount(
        self, key: str, min_score: FloatMinMax, max_score: FloatMinMax
    ) -> int:
        ...

    def zdiff(
        self, keys: List[str], withscores: bool = False
    ) -> Union[List[str], List[Tuple[str, float]]]:
        ...

    def zdiffstore(self, destination: str, keys: List[str]) -> int:
        ...

    def zincrby(
        self, key: str, increment: float, member: str
    ) -> Union[str, float]:
        ...

    def zinter(
        self,
        keys: List[str],
        weights: Union[List[float], List[int], None] = None,
        aggregate: Union[Literal["SUM", "MIN", "MAX"], None] = None,
        withscores: bool = False,
    ) -> Union[List[str], List[Tuple[str, float]]]:
        ...

    def zinterstore(
        self,
        destination: str,
        keys: List[str],
        weights: Union[List[float], List[int], None] = None,
        aggregate: Union[Literal["SUM", "MIN", "MAX"], None] = None,
    ) -> int:
        ...

    def zlexcount(self, key: str, min_score: str, max_score: str) -> int:
        ...

    def zmscore(
        self, key: str, members: List[str]
    ) -> Union[List[Union[str, None]], List[Union[float, None]]]:
        ...

    def zpopmax(
        self, key: str, count: Union[int, None] = None
    ) -> Union[List[str], List[Tuple[str, float]]]:
        ...

    def zpopmin(
        self, key: str, count: Union[int, None] = None
    ) -> Union[List[str], List[Tuple[str, float]]]:
        ...

    def zrandmember(
        self, key: str, count: Union[int, None] = None, withscores: bool = False
    ) -> Union[(Union[str, None]), (Union[List[str], List[Tuple[str, float]]])]:
        ...

    def zrange(
        self,
        key: str,
        start: FloatMinMax,
        stop: FloatMinMax,
        range_method: Union[Literal["BYSCORE", "BYLEX"], None] = None,
        rev: bool = False,
        limit_offset: Union[int, None] = None,
        limit_count: Union[int, None] = None,
        withscores: bool = False,
    ) -> Union[List[str], List[Tuple[str, float]]]:
        ...

    def zrangebylex(
        self,
        key: str,
        min_score: str,
        max_score: str,
        limit_offset: Union[int, None] = None,
        limit_count: Union[int, None] = None,
    ) -> List[Union[str, None]]:
        ...

    def zrangebyscore(
        self,
        key: str,
        min_score: FloatMinMax,
        max_score: FloatMinMax,
        withscores: bool = False,
        limit_offset: Union[int, None] = None,
        limit_count: Union[int, None] = None,
    ) -> Union[List[str], List[Tuple[str, float]]]:
        ...

    def zrangestore(
        self,
        dst: str,
        src: str,
        start: FloatMinMax,
        stop: FloatMinMax,
        range_method: Union[Literal["BYSCORE", "BYLEX"], None] = None,
        rev: bool = False,
        limit_offset: Union[int, None] = None,
        limit_count: Union[int, None] = None,
    ) -> int:
        ...

    def zrank(self, key: str, member: str) -> Union[int, None]:
        ...

    def zrem(self, key: str, *members: str) -> int:
        ...

    def zremrangebylex(self, key: str, min_score: str, max_score: str) -> int:
        ...

    def zremrangebyrank(self, key: str, start: int, stop: int) -> int:
        ...

    def zremrangebyscore(
        self, key: str, min_score: FloatMinMax, max_score: FloatMinMax
    ) -> int:
        ...

    def zrevrange(
        self, key: str, start: int, stop: int, withscores: bool = False
    ) -> Union[List[str], List[Tuple[str, float]]]:
        ...

    def zrevrangebylex(
        self,
        key: str,
        max_score: str,
        min_score: str,
        limit_offset: Union[int, None] = None,
        limit_count: Union[int, None] = None,
    ) -> List[str]:
        ...

    def zrevrangebyscore(
        self,
        key: str,
        max_score: FloatMinMax,
        min_score: FloatMinMax,
        withscores: bool = False,
        limit_offset: Union[int, None] = None,
        limit_count: Union[int, None] = None,
    ) -> Union[List[str], List[Tuple[str, float]]]:
        ...

    def zrevrank(self, key: str, member: str) -> Union[int, None]:
        ...

    def zscan(
        self,
        key: str,
        cursor: int,
        match_pattern: Union[str, None] = None,
        count: Union[int, None] = None,
    ) -> Tuple[int, List[Tuple[str, float]]]:
        ...

    def zscore(self, key: str, member: str) -> Union[str, None, float]:
        ...

    def zunion(
        self,
        keys: List[str],
        weights: Union[List[float], List[int], None] = None,
        aggregate: Union[Literal["SUM", "MIN", "MAX"], None] = None,
        withscores: bool = False,
    ) -> Union[List[str], List[Tuple[str, float]]]:
        ...

    def zunionstore(
        self,
        destination: str,
        keys: List[str],
        weights: Union[List[float], List[int], None] = None,
        aggregate: Union[Literal["SUM", "MIN", "MAX"], None] = None,
    ) -> int:
        ...

    def append(self, key: str, value: Any) -> int:
        ...

    def decr(self, key: str) -> int:
        ...

    def decrby(self, key: str, decrement: int) -> int:
        ...

    def get(self, key: str) -> Union[str, None]:
        ...

    def getdel(self, key: str) -> Union[str, None]:
        ...

    def getex(
        self,
        key: str,
        ex: Union[int, None] = None,
        px: Union[int, None] = None,
        exat: Union[int, None] = None,
        pxat: Union[int, None] = None,
        persist: Union[bool, None] = None,
    ) -> Union[str, None]:
        ...

    def getrange(self, key: str, start: int, end: int) -> str:
        ...

    def getset(self, key: str, value: Any) -> Union[str, None]:
        ...

    def incr(self, key: str) -> int:
        ...

    def incrby(self, key: str, increment: int) -> int:
        ...

    def incrbyfloat(self, key: str, increment: float) -> Union[str, float]:
        ...

    def mget(self, *keys: str) -> List[Union[str, None]]:
        ...

    def mset(self, key_value_pairs: Dict) -> Literal["OK"]:
        ...

    def msetnx(self, key_value_pairs: Dict) -> Literal[1, 0]:
        ...

    def psetex(self, key: str, milliseconds: int, value: Any) -> str:
        ...

    def set(
        self,
        key: str,
        value: Any,
        nx: bool = False,
        xx: bool = False,
        get: bool = False,
        ex: Union[int, None] = None,
        px: Union[int, None] = None,
        exat: Union[int, None] = None,
        pxat: Union[int, None] = None,
        keepttl: bool = False,
    ) -> Union[str, None]:
        ...

    def setex(self, key: str, seconds: int, value: Any) -> str:
        ...

    def setnx(self, key: str, value: Any) -> Literal[1, 0]:
        ...
    
    def setrange(self, key: str, offset: int, value: Any) -> int:
        ...

    def strlen(self, key: str) -> int:
        ...

    def substr(self, key: str, start: int, end: int) -> str:
        ...

    def pubsub(self) -> "PubSub":
        ...

    def script(self) -> "Script":
        ...

# It doesn't inherit from "Redis" mainly because of the methods signatures.
class BitFieldCommands:
    def __init__(self, client: Commands, key: str):
        ...

    def get(self, encoding: str, offset: BitFieldOffset) -> "BitFieldCommands":
        ...

    def set(self, encoding: str, offset: BitFieldOffset, value: int) -> "BitFieldCommands":
        ...

    def incrby(self, encoding: str, offset: BitFieldOffset, increment: int) -> "BitFieldCommands":
        ...

    def overflow(self, overflow: Literal["WRAP", "SAT", "FAIL"]) -> "BitFieldCommands":
        ...

    def execute(self) -> List:
        ...


class BitFieldRO:
    def __init__(self, client: Commands, key: str):
        ...

    def get(self, encoding: str, offset: BitFieldOffset) -> "BitFieldRO":
        ...

    def execute(self) -> List:
        ...


class PubSub:
    def __init__(self, client: Commands):
        ...

    def channels(self, pattern: Union[str, None] = None) -> List[str]:
        ...

    def numpat(self) -> int:
        ...

    def numsub(
        self, *channels: str
    ) -> Union[List[Union[str, int]], Dict[str, int]]:
        ...


class Script:
    def __init__(self, client: Commands):
        ...

    def exists(self, *sha1: str) -> Union[List[Literal[1, 0]], List[bool]]:
        ...

    def flush(self, mode: Literal["ASYNC", "SYNC"]) -> str:
        ...

    def load(self, script: str) -> str:
        ...


# TODO: make sure all the relevant sorted set commands return tuples