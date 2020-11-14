# -*- coding: utf-8 -*-

# Scrapy settings for spiders project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'spiders'

SPIDER_MODULES = ['spiders.spiders']
NEWSPIDER_MODULE = 'spiders.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'spiders (+http://www.yourdomain.com)'

# Obey robots.txt rules
#ROBOTSTXT_OBEY = True
LOG_LEVEL="WARNING"

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 5
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
COOKIES_ENABLED = True
cookie = ' __ckguid=jqB6Sox38GhPGhoyrxsiy2; device_id=20321486161594741290576028e4d02297c3d0dd498b1473a874191962; _ga=GA1.2.1202547864.1594741291; __jsluid_s=f62ae7361f1c2a1416b9db2390f7acdf; zdm_qd=%7B%22referrer%22%3A%22https%3A%2F%2Fu.geekbang.org%2Flesson%2F43%3Farticle%3D273014%26utm_source%3Dwebgeektime%26utm_medium%3Dpc%26utm_term%3Dpc_interstitial_246%22%7D; _gid=GA1.2.779156206.1604927222; wt3_sid=%3B999768690672041; smzdm_ec=06; smzdm_ea=200; homepage_sug=h; r_sort_type=score; _zdmA.uid=ZDMA.BEzRbfV1D.1604933418.2419200; footer_floating_layer=0; ad_date=9; bannerCounter=%5B%7B%22number%22%3A0%2C%22surplus%22%3A1%7D%2C%7B%22number%22%3A0%2C%22surplus%22%3A1%7D%2C%7B%22number%22%3A0%2C%22surplus%22%3A1%7D%2C%7B%22number%22%3A0%2C%22surplus%22%3A1%7D%2C%7B%22number%22%3A0%2C%22surplus%22%3A1%7D%2C%7B%22number%22%3A0%2C%22surplus%22%3A1%7D%5D; ad_json_feed=%7B%22J_feed_ad1%22%3A%7B%22number%22%3A0%2C%22surplus%22%3A1%7D%2C%22J_feed_ad4%22%3A%7B%22number%22%3A0%2C%22surplus%22%3A1%7D%7D; Hm_lvt_9b7ac3d38f30fe89ff0b8a0546904e58=1603889422,1604927220,1604932657,1604933431; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%221734dfcf4be564-0c7f1797a6ac61-87f133f-2073600-1734dfcf4bf55a%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E5%BC%95%E8%8D%90%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC%22%2C%22%24latest_referrer%22%3A%22https%3A%2F%2Fu.geekbang.org%2Flesson%2F43%3Farticle%3D273014%26utm_source%3Dwebgeektime%26utm_medium%3Dpc%26utm_term%3Dpc_interstitial_246%22%2C%22%24latest_landing_page%22%3A%22https%3A%2F%2Fwww.smzdm.com%2Ffenlei%2Fqipaoshui%2F%22%7D%2C%22%24device_id%22%3A%221734dfcf4be564-0c7f1797a6ac61-87f133f-2073600-1734dfcf4bf55a%22%7D; Hm_lpvt_9b7ac3d38f30fe89ff0b8a0546904e58=1605012818; wt3_eid=%3B999768690672041%7C2160493259200725137%232160501281900685890'
# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
    'Host': 'www.smzdm.com',
    'Referer':' https://www.smzdm.com/fenlei/zhinengshouji/',
    'Sec-Fetch-Dest': 'document',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36',
    'Cookie': '__ckguid=jqB6Sox38GhPGhoyrxsiy2; device_id=20321486161594741290576028e4d02297c3d0dd498b1473a874191962; _ga=GA1.2.1202547864.1594741291; __jsluid_s=f62ae7361f1c2a1416b9db2390f7acdf; zdm_qd=%7B%22referrer%22%3A%22https%3A%2F%2Fu.geekbang.org%2Flesson%2F43%3Farticle%3D273014%26utm_source%3Dwebgeektime%26utm_medium%3Dpc%26utm_term%3Dpc_interstitial_246%22%7D; _gid=GA1.2.779156206.1604927222; wt3_sid=%3B999768690672041; smzdm_ec=06; smzdm_ea=200; homepage_sug=h; r_sort_type=score; _zdmA.uid=ZDMA.BEzRbfV1D.1604933418.2419200; footer_floating_layer=0; ad_date=9; bannerCounter=%5B%7B%22number%22%3A0%2C%22surplus%22%3A1%7D%2C%7B%22number%22%3A0%2C%22surplus%22%3A1%7D%2C%7B%22number%22%3A0%2C%22surplus%22%3A1%7D%2C%7B%22number%22%3A0%2C%22surplus%22%3A1%7D%2C%7B%22number%22%3A0%2C%22surplus%22%3A1%7D%2C%7B%22number%22%3A0%2C%22surplus%22%3A1%7D%5D; ad_json_feed=%7B%22J_feed_ad1%22%3A%7B%22number%22%3A0%2C%22surplus%22%3A1%7D%2C%22J_feed_ad4%22%3A%7B%22number%22%3A0%2C%22surplus%22%3A1%7D%7D; Hm_lvt_9b7ac3d38f30fe89ff0b8a0546904e58=1603889422,1604927220,1604932657,1604933431; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%221734dfcf4be564-0c7f1797a6ac61-87f133f-2073600-1734dfcf4bf55a%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E5%BC%95%E8%8D%90%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC%22%2C%22%24latest_referrer%22%3A%22https%3A%2F%2Fu.geekbang.org%2Flesson%2F43%3Farticle%3D273014%26utm_source%3Dwebgeektime%26utm_medium%3Dpc%26utm_term%3Dpc_interstitial_246%22%2C%22%24latest_landing_page%22%3A%22https%3A%2F%2Fwww.smzdm.com%2Ffenlei%2Fqipaoshui%2F%22%7D%2C%22%24device_id%22%3A%221734dfcf4be564-0c7f1797a6ac61-87f133f-2073600-1734dfcf4bf55a%22%7D; Hm_lpvt_9b7ac3d38f30fe89ff0b8a0546904e58=1605012818; wt3_eid=%3B999768690672041%7C2160493259200725137%232160501281900685890',
    'Cache-Control': 'max-age=0'
    }
# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'spiders.middlewares.SpidersSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'spiders.middlewares.SpidersDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'spiders.pipelines.SpidersPipeline': 300,
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
