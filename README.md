# datapipeline

This project is a Python-based pipeline for loading cryptocurrency data from the CoinCap API, transforming it, and storing it into a PostgreSQL database. It includes logging configurations and a Discord handler for logging events.

### Files

- **pipeline.py**: Contains the main functionality of the data pipeline, including data loading, transformation, and database storage.
- **logging_setup.py**: Basic logging infrastructure.
- **logging_config.py**: The file that configures the main logging settings such as log formatting, levels, and handlers.
- **logging_custom.py**: Defines custom logging handler and filter for Discord.