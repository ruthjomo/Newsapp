import os

class Config:

    HEADLINES_API_URL="https://newsapi.org/v2/top-headlines?country=us&apiKey={}"
    SOURCE_API_URL='https://newsapi.org/v2/sources?apiKey={}'
    SEARCH_SOURCES='https://newsapi.org/v2/everything?q={1f0ed6430e9046308995a25d5117dc57}&apiKey={1f0ed6430e9046308995a25d5117dc57}'
    NEWS_API_KEY = os.environ.get('NEWS_API_KEY')


class ProdConfig(Config):
    pass


class DevConfig(Config):
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}