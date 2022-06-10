import os

import SqliteClient

DEALER_CENTER_CRM_DB_NAME = os.environ['DEALER_CENTER_CRM_DB_NAME'] #"dealerCenterCrm.db"
DEALER_CENTER_TABLE_NAME = os.environ['DEALER_CENTER_TABLE_NAME'] #"dealerCenter"
CAR_TABLE_NAME = os.environ['CAR_TABLE_NAME'] #"car"


def add_dealer_center(name):
    id = SqliteClient.add_to_dc_db(DEALER_CENTER_TABLE_NAME, name)
    return f"{name} Dealer Center was added. ID = {id}"


def delete_dealer_center_by_id(id):
    c= SqliteClient.delete_from_dc_db(DEALER_CENTER_TABLE_NAME, rowid=id)
    if c == 0:
        return f'Dealer Center №{id} not found. Please check it and try again', 404
    else:
        return f'Dealer Center №{id} was deleted', 200


def dealer_centers_list():
    all_dealers = SqliteClient.get_all_from_dc_db(DEALER_CENTER_TABLE_NAME)
    json_form = []
    for dealer in all_dealers:
        json_form.append({"id": dealer[0], "name": dealer[1]})
    return json_form


def dealer_center_list_filtered(**kwargs):
    all_dealers = SqliteClient.get_filtered_from_dc_db(DEALER_CENTER_TABLE_NAME, **kwargs)
    json_form = []
    for dealer in all_dealers:
        json_form.append({"id": dealer[0], "name": dealer[1]})
    return json_form


def car_list():
    all_dealers = SqliteClient.get_all_from_dc_db(CAR_TABLE_NAME)
    json_form = []
    for dealer in all_dealers:
        json_form.append({"id": dealer[0], "car_name": dealer[1], "color": dealer[2], "dealer_id": dealer[3]})
    return json_form


def car_list_filtered(**kwargs):
    all_dealers = SqliteClient.get_filtered_from_dc_db(CAR_TABLE_NAME, **kwargs)
    json_form = []
    for dealer in all_dealers:
        json_form.append({"id": dealer[0], "car_name": dealer[1], "color": dealer[2], "dealer_id": dealer[3]})
    return json_form


def car_list_by_name(name):
    all_dealers = SqliteClient.get_filtered_from_dc_db(CAR_TABLE_NAME, name=name)
    json_form = []
    for dealer in all_dealers:
        json_form.append({"id": dealer[0], "car_name": dealer[1], "color": dealer[2], "dealer_id": dealer[3]})
    return json_form


def delete_car_by_id(id):
    count = SqliteClient.delete_from_dc_db(CAR_TABLE_NAME, rowid=id)
    if count > 0:
        return f"{id} Car was deleted", 200
    else:
        return f"{id} Car was not found", 404


def add_car(name, color, dealer_center):
    if len(SqliteClient.get_filtered_from_dc_db(DEALER_CENTER_TABLE_NAME, rowid=dealer_center)) > 0:
        id = SqliteClient.add_to_dc_db(CAR_TABLE_NAME, name, color, dealer_center)
        return f"{color} {name} was added to Dealer Center №{str(dealer_center)} with ID={id}", 201
    else:
        return f"Dealer Center №{dealer_center} was not found. Please check it and try again", 404
