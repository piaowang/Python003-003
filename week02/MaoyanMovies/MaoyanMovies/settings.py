# -*- coding: utf-8 -*-

# Scrapy settings for MaoyanMovies project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'MaoyanMovies'

SPIDER_MODULES = ['MaoyanMovies.spiders']
NEWSPIDER_MODULE = 'MaoyanMovies.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'MaoyanMovies (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = True



# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 5
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16


PROXIES =[]

# Disable cookies (enabled by default)


COOKIES_ENABLED = True
cookie = '_lxsdk_cuid=172a8697a46c8-07863daf44f946-87f133f-1fa400-172a8697a46c8; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22172a8697e063bb-097bafa65e2e58-87f133f-2073600-172a8697e07460%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E8%87%AA%E7%84%B6%E6%90%9C%E7%B4%A2%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC%22%2C%22%24latest_referrer%22%3A%22https%3A%2F%2Fwww.google.com%2F%22%7D%2C%22%24device_id%22%3A%22172a8697e063bb-097bafa65e2e58-87f133f-2073600-172a8697e07460%22%7D; uuid_n_v=v1; uuid=07975540E22F11EABDF7A52DEC86ABCD34B57FAC3EDE4CDCABF378DBF5F0C83F; _csrf=26f7ea61031d83843e1fe596d71bd2e030224cdd7c1a8252680e36988e32f740; mojo-uuid=8dfd7a9865de74edd7cd5f95c3b05da5; _lxsdk=07975540E22F11EABDF7A52DEC86ABCD34B57FAC3EDE4CDCABF378DBF5F0C83F; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1597850227,1597850252,1597932875; mojo-session-id={"id":"1e5a367323fc454b7877e90d10d0ac53","time":1598686449857}; mojo-trace-id=1; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1598686450; __mta=150811913.1597850228100.1598673134579.1598686451134.21; _lxsdk_s=174392351e8-8f9-5c7-d40%7C%7C2'

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:

DEFAULT_REQUEST_HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
    'Host': 'maoyan.com',
    'Sec-Fetch-Dest': 'document',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
    'Cookie': '_lxsdk_cuid=172a8697a46c8-07863daf44f946-87f133f-1fa400-172a8697a46c8; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22172a8697e063bb-097bafa65e2e58-87f133f-2073600-172a8697e07460%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E8%87%AA%E7%84%B6%E6%90%9C%E7%B4%A2%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC%22%2C%22%24latest_referrer%22%3A%22https%3A%2F%2Fwww.google.com%2F%22%7D%2C%22%24device_id%22%3A%22172a8697e063bb-097bafa65e2e58-87f133f-2073600-172a8697e07460%22%7D; uuid_n_v=v1; uuid=07975540E22F11EABDF7A52DEC86ABCD34B57FAC3EDE4CDCABF378DBF5F0C83F; _csrf=26f7ea61031d83843e1fe596d71bd2e030224cdd7c1a8252680e36988e32f740; mojo-uuid=8dfd7a9865de74edd7cd5f95c3b05da5; _lxsdk=07975540E22F11EABDF7A52DEC86ABCD34B57FAC3EDE4CDCABF378DBF5F0C83F; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1597850227,1597850252,1597932875; mojo-session-id={"id":"1e5a367323fc454b7877e90d10d0ac53","time":1598686449857}; mojo-trace-id=1; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1598686450; __mta=150811913.1597850228100.1598673134579.1598686451134.21; _lxsdk_s=174392351e8-8f9-5c7-d40%7C%7C2',
    'Cache-Control': 'max-age=0'
    }

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'MaoyanMovies.middlewares.MaoyanmoviesSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
   #'MaoyanMovies.middlewares.ProxyMiddleware': 300,
   'MaoyanMovies.middlewares.MaoyanmoviesDownloaderMiddleware': 543,
   'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware': None,
   'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None
}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html



ITEM_PIPELINES = {
    'MaoyanMovies.pipelines.MaoyanmoviesPipeline': 300,
}



# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
