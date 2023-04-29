import configparser
import pathlib

from quotes.quotes.settings import env

file_config = pathlib.Path(__file__).parent.joinpath('config.ini')
config = configparser.ConfigParser()
config.read(file_config)

username = env("MONGO_DB_USER")
password = env("MONGO_DB_PASSWORD")
db_name = env("MONGO_DB_NAME")
domain = env("MONGO_DB_DOMAIN")

url = f'mongodb+srv://{username}:{password}@{domain}/{db_name}?retryWrites=true&w=majority'
