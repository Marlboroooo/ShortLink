from get_url import get_url
from get_short_link import get_short_url
from short_link_formatter import formatter_links
from exceptions import UrlError, ApiServiceError


def main():
    try:
        full_url = get_url()
    except UrlError:
        print('Invalid URL-address')
        exit(1)
    try:
        short_url = get_short_url(full_url)
    except ApiServiceError:
        print('URL-address could not be shortened')
        exit(1)
    print(formatter_links(short_url))


if __name__ == '__main__':
    main()
