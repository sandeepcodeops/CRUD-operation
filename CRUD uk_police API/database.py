"""
This file represents the loading the data from CSV to MySQL database
"""
import pandas as pd
import mysql.connector
import logging

logging.basicConfig(filename='logging_statements.log', level=logging.DEBUG,
                    format='%(asctime)s:%(levelname)s:%(message)s')


def create_df(file_path):
    """
    This function represents the Dataframe creation from CSV file
    Input:
        :param file_path: CSV file as input
        :type file_path: file
    Return:
        :return: returns the Dataframe
    """
    data = pd.read_csv(file_path, index_col=False, delimiter=',')
    return data


def creating_database(data_frame):
    """
    This function represents the creating the MySQL table
    Input:
        :param data_frame: dataframe as a input
    Return:
        :return: MySQL table
    """
    conn = mysql.connector.connect(host='localhost', database='uk_police', user='sandeep', passwd='1234')
    cursor = conn.cursor()
    cursor.execute("select database();")
    record = cursor.fetchone()
    logging.info("You're connected to database:{} ".format(record))
    cursor.execute('DROP TABLE IF EXISTS search_data;')
    logging.info('Creating table....')
    cursor.execute("CREATE TABLE search_data(date DATE,stop_and_search varchar(1000))")
    logging.info("Table is created....")
    for i, row in data_frame.iterrows():
        sql = "INSERT INTO uk_police.search_data VALUES (%s,%s)"
        cursor.execute(sql, tuple(row))
        logging.info("Record inserted")
        conn.commit()


dataframe = create_df('D:\\Codeops\\Database Management\\file\\csv_output.csv')
logging.debug(creating_database(dataframe))
