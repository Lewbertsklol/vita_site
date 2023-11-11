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


def write_worksheet(month: str, day_number: int, event_number: int, value: str) -> bool:
    service_file = open("service_file.json", "w")
    json.dump(json_dict, service_file)
    service_file.close()
    client: pygsheets.client.Client = pygsheets.authorize(
        service_file=service_file.name
    )
    os.remove("service_file.json")
    sheet: pygsheets.Spreadsheet = client.open("Окошки")
    worksheet: pygsheets.Worksheet = sheet.worksheet('title', month)
    data_range: pygsheets.DataRange = worksheet.range('B2:H37', 'matrix')
    (x, y) = find_event_inside_matrix(data_range, day_number, event_number)
    cell = (x + 2, y + 2)
    if not worksheet.cell(cell).value:
        worksheet.update_value(addr=cell, val=f"'{value}")
        return True
    return False


def find_event_inside_matrix(matrix, day_number: str, event_number: int):
    num_of_rows = len(matrix)
    for row in range(0, num_of_rows, 6):
        for col in range(0, 7):
            if day_number == matrix[row][col]:
                x = row + 1 + event_number
                y = col
                return (x, y)
    return None
