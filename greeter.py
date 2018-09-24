import os

TAGCONST = [
    {"id": 1, "value": 'TextBox', "tagDef": "textbox_field", "tagDesc": "textbox_info"},
    {"id": 2, "value": 'Email', "tagDef": "email_field", "tagDesc": "email_info"},
    {"id": 3, "value": 'TextArea', "tagDef": "textarea_field", "tagDesc": "textarea_info"},
    {"id": 4, "value": 'Password', "tagDef": "password_field", "tagDesc": "password_info"},
    {"id": 5, "value": 'Select', "tagDef": "select_field", "tagDesc": "select_info"},
    {"id": 6, "value": 'Radio', "tagDef": "radio_field", "tagDesc": "radio_info"},
    {"id": 7, "value": 'Checkbox', "tagDef": "checkbox_field", "tagDesc": "check_info"},
    {"id": 8, "value": 'Date', "tagDef": "date_field", "tagDesc": "date_info"},
    {"id": 9, "value": 'Time', "tagDef": "time_field", "tagDesc": "time_info"},
    {"id": 10, "value": 'Month', "tagDef": "month_field", "tagDesc": "month_info"},
    {"id": 11, "value": 'Week', "tagDef": "week_field", "tagDesc": "week_info"},
    {"id": 12, "value": 'DateTime', "tagDef": "datetime_field", "tagDesc": "datetime_info"},
    {"id": 13, "value": 'Number', "tagDef": "number_field", "tagDesc": "number_info"},
    {"id": 14, "value": 'Range', "tagDef": "range_field", "tagDesc": "range_info"},
    {"id": 15, "value": 'Color', "tagDef": "color_field", "tagDesc": "color_info"},
    {"id": 16, "value": 'Search', "tagDef": "search_field", "tagDesc": "search_info"},
    {"id": 17, "value": 'File', "tagDef": "file_field", "tagDesc": "file_info"},
    {"id": 18, "value": 'Button', "tagDef": "button", "tagDesc": "button_info"}
]


def display_menu():
    os.system('clear')
    print('\033[94m')
    print("Select From Following.")
    print('\033[95m')
    for tag in TAGCONST:
        print(tag['id'], '.', tag['value'])
    print("\033[91m" + '99. Exit' + '\033[0m')
