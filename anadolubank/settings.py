BOT_NAME = 'anadolubank'
SPIDER_MODULES = ['anadolubank.spiders']
NEWSPIDER_MODULE = 'anadolubank.spiders'
ROBOTSTXT_OBEY = True
LOG_LEVEL = 'WARNING'
ITEM_PIPELINES = {
   'anadolubank.pipelines.DatabasePipeline': 300,
}
