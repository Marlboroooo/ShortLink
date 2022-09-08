from typing import NamedTuple
import validators

from exceptions import UrlError


class IntroductoryURL(NamedTuple):
    url: str


def get_url() -> IntroductoryURL:
    try:
        url = _validation_url()
        if not url:
            raise UrlError
        return IntroductoryURL(url=url)
    except:
        raise UrlError


def _validation_url():
    try:
        link = input('Your URL-address: ')
        validation = validators.url(link)
        if validation:
            return link
    except:
        raise UrlError
