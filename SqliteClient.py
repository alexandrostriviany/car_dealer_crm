import os
import sqlite3

DEALER_CENTER_CRM_DB_NAME = os.environ['DEALER_CENTER_CRM_DB_NAME'] #"dealerCenterCrm.db"


def __table_name_mapper(name):
    if name == 'id':
        return 'rowid'
    elif name == 'dealer_id':
        return 'dealerCenterId'
    elif name == 'car_name':
        return 'name'
    else:
        return name


def create_table():
    conn = sqlite3.connect(DEALER_CENTER_CRM_DB_NAME)
    c = conn.cursor()
    c.execute((f"""CREATE TABLE {os.environ['DEALER_CENTER_TABLE_NAME']} (
                name text
                )"""))
    conn.commit()
    c.execute((f"""CREATE TABLE {os.environ['CAR_TABLE_NAME']} (
                name text, 
                color text, 
                dealerCenterId integer
                )"""))
    conn.commit()
    conn.close()


def add_to_dc_db(table_name, *args):
    values = "', '".join(str(x) for x in list(args))
    conn = sqlite3.connect(DEALER_CENTER_CRM_DB_NAME)
    c = conn.cursor()
    c.execute(f"""INSERT INTO {table_name} VALUES ('{values.lower()}')""")
    conn.commit()
    rowid = c.lastrowid
    conn.close()
    return rowid


def get_all_from_dc_db(table_name):
    conn = sqlite3.connect(DEALER_CENTER_CRM_DB_NAME)
    c = conn.cursor()
    c.execute(f"SELECT rowid, * FROM '{table_name}'")
    conn.commit()
    dc_list = c.fetchall()
    conn.close()
    return dc_list


def get_filtered_from_dc_db(table_name, **kwargs):
    filter_key = ''
    for f, v in kwargs.items():
        if v is not None:
            filter_key += f"AND {__table_name_mapper(f)}='{str(v).lower()}'"
    conn = sqlite3.connect(DEALER_CENTER_CRM_DB_NAME)
    c = conn.cursor()
    c.execute(f"SELECT rowid, * FROM '{table_name}' WHERE {filter_key[4:].lstrip()}")
    conn.commit()
    dc_list = c.fetchall()
    conn.close()
    return dc_list


def delete_from_dc_db(table_name, **kwargs):
    filter_key = ''
    for f, v in kwargs.items():
        if isinstance(v, list):
            filter_key = f"""{__table_name_mapper(f)} IN ('{"', '".join(v)}')"""
        else:
            filter_key = f"{__table_name_mapper(f)}='{v}'"
    conn = sqlite3.connect(DEALER_CENTER_CRM_DB_NAME)
    c = conn.cursor()
    c.execute(f"DELETE FROM '{table_name.lower()}' WHERE {filter_key.lower()}")
    conn.commit()
    deleted_rows = c.rowcount
    conn.close()
    return deleted_rows
