import pygsheets
import json
import os
from vita_app.entities import Month
from vita_app.service_file import json_dict


def read_worksheet() -> list[Month]:
    calendar: list[Month] = []
    service_file = open("service_file.json", "w")
    json.dump(json_dict, service_file)
    service_file.close()
    client: pygsheets.client.Client = pygsheets.authorize(
        service_file=service_file.name
    )
    os.remove("service_file.json")
    sheet: pygsheets.Spreadsheet = client.open("Окошки")
    for worksheet in sheet.worksheets():
        data_range: pygsheets.DataRange = worksheet.range(
            'B2:H37', 'matrix')
        month = Month.from_matrix(data_range, worksheet.title)
        calendar.append(month)
    return calendar


def write_worksheet(month: Month, month_number: int, day_number: int, event_number: int, value: str) -> bool:
    service_file = open("service_file.json", "w")
    json.dump(json_dict, service_file)
    service_file.close()
    client: pygsheets.client.Client = pygsheets.authorize(
        service_file=service_file.name
    )
    os.remove("service_file.json")
    sheet: pygsheets.Spreadsheet = client.open("Окошки")
    worksheet: pygsheets.Worksheet = sheet.worksheet('index', month_number)
    (x, y) = month.find_event_inside_matrix(day_number, event_number)
    cell = (x + 2, y + 2)
    if not worksheet.cell(cell).value:
        worksheet.update_value(addr=cell, val=value)
        return True
    return False
