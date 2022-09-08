import json
from json.decoder import JSONDecodeError
import urllib.request
from urllib.error import URLError
from typing import NamedTuple

from get_url import IntroductoryURL
import config
from exceptions import ApiServiceError


class ShortUrl(NamedTuple):
    shortlink: str


def get_short_url(get_url: IntroductoryURL) -> ShortUrl:
    api_response = _get_api_response(url=get_url.url)
    short_url = _parse_api_response(api_response)
    return short_url


def _get_api_response(url: str) -> str:
    api_url = config.API_URL.format(url=url)
    try:
        return urllib.request.urlopen(api_url).read()
    except URLError:
        raise ApiServiceError


def _parse_api_response(api_response: str) -> ShortUrl:
    try:
        api_dict = json.loads(api_response)
    except JSONDecodeError:
        raise ApiServiceError
    try:
        return ShortUrl(
            shortlink=_parse_shortlink(api_dict)
        )
    except:
        raise ApiServiceError


def _parse_shortlink(api_dict: dict) -> str:
    return str(api_dict['url']['shortLink'])


