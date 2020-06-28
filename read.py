from util import get_connection
from loguru import logger


def get_column_names(cursor, db_type):
    if db_type == 'mysql':
        column_names = cursor.column_names
    elif db_type == 'postgres':
        column_names = []
        for column_name in cursor.description:
            column_names.append(column_name)
    return column_names


def read_table(db_details, table_name, limit=0):
    logger.info(db_details)
    connection = get_connection(db_type=db_details['DB_TYPE'],
                                db_host=db_details['DB_HOST'],
                                db_name=db_details['DB_NAME'],
                                db_user=db_details['DB_USER'],
                                db_pass=db_details['DB_PASS']
                                )
    cursor = connection.cursor()
    if limit == 0:
        query = f'SELECT * FROM {table_name}'
    else:
        query = f'SELECT * FROM {table_name} LIMIT {limit}'
    cursor.execute(query)
    data = cursor.fetchall()
    column_names = get_column_names(cursor, db_details['DB_TYPE'])

    connection.close()

    return data, column_names
