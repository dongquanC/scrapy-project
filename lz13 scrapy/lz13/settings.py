BOT_NAME = 'lz13'

SPIDER_MODULES = ['lz13.spiders']
NEWSPIDER_MODULE = 'lz13.spiders'

ROBOTSTXT_OBEY = False


DEFAULT_REQUEST_HEADERS = {
   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
   'Accept-Language': 'en',
   'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
}

ITEM_PIPELINES = {
    'lz13.pipelines.Lz13Pipeline': 300,
}
