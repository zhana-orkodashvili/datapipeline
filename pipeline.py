import pandas as pd
import requests
from sqlalchemy import create_engine
import logging.config

from logging_config import logging_config

logging.config.dictConfig(logging_config)
logger = logging.getLogger(__name__)

def transform_data(df):
    df.drop(columns=['explorer'], inplace=True)
    df.fillna({'maxSupply': 0}, inplace=True)
    logger.info('Data transformation completed successfully.')


def load_crypto_data():
    url = 'https://api.coincap.io/v2/assets'

    header = {'Content-Type': 'application/json',
              'Accept-Encoding': 'deflate'}

    logger.info('Loading secret crypto data...')
    try:
        response = requests.get(url, headers=header)
        response.raise_for_status()

        data = response.json()

        df = pd.json_normalize(data, 'data')

        logger.info('Crypto data has been loaded')
        logger.info('Starting data processing')

        transform_data(df)

        engine = create_engine('postgresql://postgres:postgres@localhost:5432/cryptoapi')

        table_name = 'CryptoData'

        logger.info('Writing data to PostgreSQL database...')
        df.to_sql(table_name, engine, if_exists='replace', index=False)
        logger.info('Data has been successfully written to PostgreSQL.')

    except Exception as e:
        logger.exception("Error occurred while loading crypto data: %s", str(e))


load_crypto_data()

