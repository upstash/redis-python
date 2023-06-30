from os import environ
from typing import Any, List, Type, Union

from aiohttp import ClientSession
from upstash_redis.commands.commands import BasicKeyCommands
from upstash_redis.config import REST_ENCODING, REST_RETRIES, REST_RETRY_INTERVAL, FORMAT_RETURN, ALLOW_TELEMETRY
from upstash_redis.http.execute import async_execute, sync_execute

from upstash_redis.schema.http import RESTEncoding, RESTResult
from upstash_redis.schema.telemetry import TelemetryData
from upstash_redis.utils.format import FormattedResponse

from asyncio import run


class Redis(FormattedResponse, BasicKeyCommands):
    
    def __init__(
        self,
        url: str,
        token: str,
        rest_encoding: RESTEncoding = REST_ENCODING,
        rest_retries: int = REST_RETRIES,
        rest_retry_interval: int = REST_RETRY_INTERVAL,  # Seconds.
        format_return: bool = FORMAT_RETURN,
        allow_telemetry: bool = ALLOW_TELEMETRY,
        telemetry_data: Union[TelemetryData, None] = None,
    ):
        """
        :param url: UPSTASH_REDIS_REST_URL in the console
        :param token: UPSTASH_REDIS_REST_TOKEN in the console
        :param rest_encoding: the encoding that can be used by the REST API to parse the response before sending it
        :param rest_retries: how many times an HTTP request will be retried if it fails
        :param rest_retry_interval: how many seconds will be waited between each retry
        :param format_return: whether the raw, RESP2 result or a formatted response will be returned
        :param allow_telemetry: whether anonymous telemetry can be collected
        """

        self.url = url
        self.token = token

        self.allow_telemetry = allow_telemetry

        self.format_return = format_return

        self.rest_encoding = rest_encoding
        self.rest_retries = rest_retries
        self.rest_retry_interval = rest_retry_interval

        self.telemetry_data = telemetry_data
        self.FORMATTERS = self.__class__.FORMATTERS



    @classmethod
    def from_env(
        cls,
        rest_encoding: RESTEncoding = REST_ENCODING,
        rest_retries: int = REST_RETRIES,
        rest_retry_interval: int = REST_RETRY_INTERVAL,
        format_return: bool = FORMAT_RETURN,
        allow_telemetry: bool = ALLOW_TELEMETRY,
        telemetry_data: Union[TelemetryData, None] = None,
    ):
        """
        Load the credentials from environment.

        :param rest_encoding: the encoding that can be used by the REST API to parse the response before sending it
        :param rest_retries: how many times an HTTP request will be retried if it fails
        :param rest_retry_interval: how many seconds will be waited between each retry
        :param format_return: whether the raw, RESP2 result or a formatted response will be returned
        :param allow_telemetry: whether anonymous telemetry can be collected
        """

        return cls(
            environ["UPSTASH_REDIS_REST_URL"],
            environ["UPSTASH_REDIS_REST_TOKEN"],
            rest_encoding,
            rest_retries,
            rest_retry_interval,
            format_return,
            allow_telemetry,
            telemetry_data,
        )

    def run(self, command: List) -> int:
        """
        Specify the http options and execute the command.
        """

        res = sync_execute(
                    url=self.url,
                    token=self.token,
                    encoding=self.rest_encoding,
                    retries=self.rest_retries,
                    retry_interval=self.rest_retry_interval,
                    command=command,
                    allow_telemetry=self.allow_telemetry,
                    telemetry_data=self.telemetry_data,
                )
                

        main_command = command[0]
        if len(command) > 1 and (main_command == "PUBSUB" or main_command == "SCRIPT"):
            main_command = f"{main_command} {command[1]}"

        if self.format_return and (main_command in self.FORMATTERS) :
            return self.FORMATTERS[main_command](res)

        return res
        

