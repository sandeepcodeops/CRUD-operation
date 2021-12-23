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
    data_csv = pd.read_csv(file_path, index_col=False, delimiter=',')
    data = data_csv.where((pd.notnull(data_csv)), None)
    return data

#
# def creating_database(data_frame):
#     """
#     This function represents the creating the MySQL table
#     Input:
#         :param data_frame: dataframe as a input
#     Return:
#         :return: MySQL table
#     """
    conn = mysql.connector.connect(host='localhost', database='uk_police', user='sandeep', passwd='1234')
    cursor = conn.cursor()
    cursor.execute("select database();")
    record = cursor.fetchone()
    logging.info("You're connected to database:{} ".format(record))
    cursor.execute('DROP TABLE IF EXISTS mytable;')
    logging.info('Creating table....')
    create_table = """
    CREATE TABLE museum(objectID INT PRIMARY KEY , 
isHighlight VARCHAR(255) DEFAULT 'Null',
accessionNumber VARCHAR(255) DEFAULT 'Null',
accessionYear INT DEFAULT 0,
isPublicDomain VARCHAR(255) DEFAULT 'Null', 
primaryImage VARCHAR(255) DEFAULT 'Null',
primaryImageSmall VARCHAR(255) DEFAULT 'Null',
department VARCHAR(255) DEFAULT 'Null',
objectName VARCHAR(255) DEFAULT 'Null',
title VARCHAR(255) DEFAULT 'Null',
culture VARCHAR(255) DEFAULT 'Null',
artistRole VARCHAR(255) DEFAULT 'Null',
artistPrefix VARCHAR(255) DEFAULT 'Null',
artistDisplayName VARCHAR(255) DEFAULT 'Null',
artistDisplayBio VARCHAR(255) DEFAULT 'Null',
artistAlphaSort VARCHAR(255) DEFAULT 'Null',
artistNationality VARCHAR(255) DEFAULT 'Null',
artistBeginDate INT DEFAULT 0,
artistEndDate INT DEFAULT 0,
artistWikidata_URL VARCHAR(255) DEFAULT 'Null',
artistULAN_URL VARCHAR(255) DEFAULT 'Null',
objectDate VARCHAR(255) DEFAULT 'Null',
objectBeginDate VARCHAR(255) DEFAULT 'Null',
objectEndDate VARCHAR(255) DEFAULT 'Null', 
medium VARCHAR(255) DEFAULT 'Null',
dimensions VARCHAR(255) DEFAULT 'Null',
creditLine VARCHAR(255) DEFAULT 'Null',
geographyType VARCHAR(255) DEFAULT 'Null',
city VARCHAR(255) DEFAULT 'Null',
state VARCHAR(255) DEFAULT 'Null',
county VARCHAR(255) DEFAULT 'Null',
country VARCHAR(255) DEFAULT 'Null',
metadataDate VARCHAR(255) DEFAULT 'Null',
repository VARCHAR(255) DEFAULT 'Null',
objectURL VARCHAR(255) DEFAULT 'Null',
objectWikidata_URL VARCHAR(255) DEFAULT 'Null',
isTimelineWork VARCHAR(255) DEFAULT 'Null',
GalleryNumber INT DEFAULT 0,
constituents_constituentID INT DEFAULT 0,
constituents_role VARCHAR(255) DEFAULT 'Null',
constituents_name VARCHAR(255) DEFAULT 'Null',
constituents_constituentULAN_URL VARCHAR(255) DEFAULT 'Null',
constituents_constituentWikidata_URL VARCHAR(255) DEFAULT 'Null', measurements_elementName VARCHAR(255) DEFAULT 'Null',
measurements_elementDescription VARCHAR(255) DEFAULT 'Null', elementMeasurements_Diameter VARCHAR(255) DEFAULT 'Null',
tags_term VARCHAR(255) DEFAULT 'Null',
tags_AAT_URL VARCHAR(255) DEFAULT 'Null',
tags_Wikidata_URL VARCHAR(255) DEFAULT 'Null',
elementMeasurements_Depth FLOAT DEFAULT 0,
elementMeasurements_Height FLOAT DEFAULT 0,
measurements_elementMeasurements_Width FLOAT DEFAULT 0,
measurements_elementMeasurements_Weight FLOAT DEFAULT 0)
    """
    cursor.execute(create_table)
    logging.info("Table is created....")
    for i, row in data.iterrows():
        sql = """
        INSERT INTO uk_police.museum VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,
              %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
        """
        cursor.execute(sql, tuple(row))
        logging.info("Record inserted")
        conn.commit()


create_df('Mmuseum.csv')
# logging.debug(creating_database(datafarme))
