# django-verbosecache

`django-verbosecache` is a dummy cache backend for Django, but verbose.  It
will just print which methods of the backend are called, and the provided
arguments.

## Set up

Copy the `verbose_cache.py` file in the root of your Django project (for
example), and ajust your settings:

    CACHES = {
        'default': {
            'BACKEND': 'verbose_cache.VerboseCache',
        }
    }

## Example output

    [CACHE] get called with:
    (<verbose_cache.VerboseCache object at 0x000000010441d1a0>,
     'views.decorators.cache.cache_header..6666cd76f96956469e7be39d750cc7d9.en-us.notmobile',
     None)
    {}
    Output: None
