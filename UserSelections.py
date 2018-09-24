import tagDefinations
import tagDescription
from finalizer import parsed_data
from greeter import display_menu, TAGCONST

choice = ''


def gettaginfo():
    display_menu()
    ip = int(input("Enter: "))
    return ip


parsed = ''
while True:
    choice = gettaginfo()
    if choice in ['Exit', 'exit', 99]:
        print('\033[92m')
        print(parsed)
        parsed_data(parsed)
        print('\033[0m')
        break
    else:
        print('\033[93m')
        for c in TAGCONST:
            if c['id'] == choice:
                data = getattr(tagDescription, c['tagDesc'])()
                tmp = getattr(tagDefinations, c['tagDef'])(data)
                parsed += tmp
