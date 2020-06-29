import sys
from loguru import logger

from util import load_db_details
from read import read_table
import pandas as pd
from write import write_df_to_file


def init_logger():
    logger.add("etl-demo.info",
               rotation="1 MB",
               retention="10 days",
               level="INFO"
               )
    logger.add("etl-demo.err",
               rotation="1 MB",
               retention="10 days",
               level="ERROR"
               )


def main():
    env = sys.argv[1]
    a_database = sys.argv[2]
    a_table = sys.argv[3]
    init_logger()
    db_details = load_db_details(env)[a_database]
    logger.info(f'reading data for {a_table}')
    data, column_names = read_table(db_details, a_table)
    df = pd.DataFrame(data, columns=column_names)
    write_df_to_file('/tmp', table_name=a_table, df=df)


if __name__ == '__main__':
    main()
