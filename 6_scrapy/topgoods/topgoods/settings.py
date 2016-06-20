# -*- coding: utf-8 -*-

# Scrapy settings for topgoods project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'topgoods'

SPIDER_MODULES = ['topgoods.spiders']
NEWSPIDER_MODULE = 'topgoods.spiders'
# 打开下载中间件
#DOWNLOADER_MIDDLEWARES = {
#        'scrapy.downloadermiddleware.httpproxy.HttpProxyMiddleware':301,
 #   }
# 打开图片下载管道
ITEM_PIPELINES = {'scrapy.pipelines.images.ImagesPipeline': 1}
# 把items中的图片链接字段配置在这里
IMAGES_URLS_FIELD = 'file_urls'
# 设置图片保存路径
IMAGES_STORE = r'.'

LOG_FILE = "scrapy.log"
