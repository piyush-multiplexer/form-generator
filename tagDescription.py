from VueGenerator import data_injector


def textbox_info():
    data = {'name': input('Enter Title: '), 'placeholder': input('Enter Placeholder: '), 'id': input('Enter Id: '),
            'vmodel': input('Enter v-model: '), 'readonly': input('Readonly (y/n)? ')}
    data_injector(data['vmodel'])
    return data


def email_info():
    data = {'name': input('Enter Title: '), 'placeholder': input('Enter Placeholder: '), 'id': input('Enter Id: '),
            'vmodel': input('Enter v-model: '), 'readonly': input('Readonly (y/n)? ')}
    data_injector(data['vmodel'])
    return data


def textarea_info():
    data = {'name': input('Enter Title: '), 'placeholder': input('Enter Placeholder: '),
            'rows': int(input('Enter no of Rows: ')), 'id': input('Enter Id: '), 'vmodel': input('Enter v-model: '),
            'readonly': input('Readonly (y/n)? ')}
    data_injector(data['vmodel'])
    return data


def password_info():
    data = {'name': input('Enter Title: '), 'placeholder': input('Enter Placeholder: '), 'id': input('Enter Id: '),
            'vmodel': input('Enter v-model: '), 'readonly': input('Readonly (y/n)? ')}
    data_injector(data['vmodel'])
    return data


def select_info():
    data = {'name': input('Enter Title: '), 'placeholder': input('Enter Placeholder: '), 'id': input('Enter Id: '),
            'vmodel': input('Enter v-model: '), 'optionsLength': int(input('Enter no.(length) of options')),
            'readonly': input('Readonly (y/n)? ')}
    val, lab = [], []
    for d in range(data['optionsLength']):
        val.append(input('Enter value'))
        lab.append(input('Enter label'))
    data['label'] = lab
    data['values'] = val
    data_injector(data['vmodel'])
    return data


def radio_info():
    data = {'name': input('Enter Title: '), 'id': input('Enter Id: '),
            'vmodel': input('Enter v-model: '), 'radioLength': int(input('Enter no.(length) of radio')),
            'readonly': input('Readonly (y/n)? ')}
    val, lab = [], []
    for d in range(data['radioLength']):
        val.append(input('Enter value'))
        lab.append(input('Enter label'))
    data['label'] = lab
    data['values'] = val
    data_injector(data['vmodel'])
    return data


def check_info():
    data = {'name': input('Enter Title: '), 'id': input('Enter Id: '),
            'vmodel': input('Enter v-model: '), 'checkLength': int(input('Enter no.(length) of checkbox')),
            'readonly': input('Readonly (y/n)? ')}
    val, lab = [], []
    for d in range(data['checkLength']):
        val.append(input('Enter value'))
        lab.append(input('Enter label'))
    data['label'] = lab
    data['values'] = val
    data_injector(data['vmodel'], True)
    return data


def date_info():
    data = {'name': input('Enter Title: '), 'id': input('Enter Id: '),
            'vmodel': input('Enter v-model: '), 'readonly': input('Readonly (y/n)? ')}
    data_injector(data['vmodel'])
    return data


def time_info():
    data = {'name': input('Enter Title: '), 'id': input('Enter Id: '),
            'vmodel': input('Enter v-model: '), 'readonly': input('Readonly (y/n)? ')}
    data_injector(data['vmodel'])
    return data


def month_info():
    data = {'name': input('Enter Title: '), 'id': input('Enter Id: '),
            'vmodel': input('Enter v-model: '), 'readonly': input('Readonly (y/n)? ')}
    data_injector(data['vmodel'])
    return data


def week_info():
    data = {'name': input('Enter Title: '), 'id': input('Enter Id: '),
            'vmodel': input('Enter v-model: '), 'readonly': input('Readonly (y/n)? ')}
    data_injector(data['vmodel'])
    return data


def datetime_info():
    data = {'name': input('Enter Title: '), 'id': input('Enter Id: '),
            'vmodel': input('Enter v-model: '), 'readonly': input('Readonly (y/n)? ')}
    data_injector(data['vmodel'])
    return data


def number_info():
    data = {'name': input('Enter Title: '), 'id': input('Enter Id: '),
            'vmodel': input('Enter v-model: '), 'readonly': input('Readonly (y/n)? ')}
    data_injector(data['vmodel'])
    return data


def range_info():
    data = {'name': input('Enter Title: '), 'id': input('Enter Id: '), 'max': int(input('Enter max value')),
            'min': int(input('Enter min value')), 'vmodel': input('Enter v-model: '),
            'readonly': input('Readonly (y/n)? ')}
    data_injector(data['vmodel'])
    return data


def color_info():
    data = {'name': input('Enter Title: '), 'id': input('Enter Id: '),
            'vmodel': input('Enter v-model: '), 'readonly': input('Readonly (y/n)? ')}
    data_injector(data['vmodel'])
    return data


def search_info():
    data = {'name': input('Enter Title: '), 'id': input('Enter Id: '),
            'vmodel': input('Enter v-model: '), 'readonly': input('Readonly (y/n)? ')}
    data_injector(data['vmodel'])
    return data


def file_info():
    accepts = {1: 'audio/*', 2: 'video/*', 3: 'image/*', 4: 'all'}
    data = {'name': input('Enter Title: '), 'id': input('Enter Id: '),
            'vmodel': input('Enter v-model: '), 'readonly': input('Readonly (y/n)? ')}
    print('type of file tobe accepted.')
    print(accepts)
    input('Select')
    data_injector(data['vmodel'])
    return data


def button_info():
    data = {'value': input('Enter Value: '), 'id': input('Enter Id: '), 'readonly': input('Readonly (y/n)? ')}
    data_injector(False)
    return data
