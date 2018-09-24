from yattag import Doc


def modeler(d):
    n = d['name']
    m = '{{' + d['vmodel'] + '}}'
    return n + m


def textbox_field(data):
    textbox_doc, textbox_tag, textbox_text = Doc(
        defaults={data['name']: ''}, errors={data['name']: ''}
    ).tagtext()
    rdnl = 'readonly' if data['readonly'] == 'y' else 'test'
    with textbox_tag('div', klass="form-group"):
        with textbox_tag('label', ('for', data['id']), ('style', 'color:red')):
            textbox_text(modeler(data))
        textbox_doc.input(('v-model', data['vmodel']), (rdnl, ''), name=data['name'], type='text',
                          placeholder=data['placeholder'],
                          id=data['id'],
                          klass='form-control', style='color:blue;font-family: sans-serif;')
    return textbox_doc.getvalue()


def email_field(data):
    email_doc, email_tag, email_text = Doc(
        defaults={data['name']: ''}, errors={data['name']: ''}
    ).tagtext()
    with email_tag('div', klass="form-group"):
        with email_tag('label', ('for', data['id'])):
            email_text(modeler(data))
        email_doc.input(('v-model', data['vmodel']), name=data['name'], type='email', placeholder=data['placeholder'],
                        id=data['id'],
                        klass='form-control')
    return email_doc.getvalue()


def textarea_field(data):
    textarea_doc, textarea_tag, textarea_text = Doc(
        defaults={}, errors={}
    ).tagtext()
    with textarea_tag('div', klass="form-group"):
        with textarea_tag('label', ('for', data['id'])):
            textarea_text(modeler(data))
        with textarea_doc.textarea(('v-model', data['vmodel']), name=data['name'], rows=data['rows'],
                                   placeholder=data['placeholder'], id=data['id'],
                                   klass='form-control'):
            pass
    return textarea_doc.getvalue()


def password_field(data):
    password_doc, password_tag, password_text = Doc(
        defaults={data['name']: ''}, errors={data['name']: 'Compulsury'}
    ).tagtext()
    with password_tag('div', klass="form-group"):
        with password_tag('label', ('for', data['id'])):
            password_text(modeler(data))
        password_doc.input(('v-model', data['vmodel']), name=data['name'], type='password',
                           placeholder=data['placeholder'], id=data['id'],
                           klass='form-control')
    return password_doc.getvalue()


def select_field(data):
    select_doc, select_tag, select_text, select_line = Doc().ttl()
    with select_tag('div', klass="form-group"):
        select_line('label', data['name'])
        with select_doc.select(('v-model', data['vmodel']), name=data['name'], klass="custom-select"):
            for val, desc in zip(data['values'], data['label']):
                with select_doc.option(value=val):
                    select_text(desc)
    return select_doc.getvalue()


def radio_field(data):
    radio_doc, radio_tag, radio_text, radio_line = Doc().ttl()
    with radio_tag('div', klass="form-group"):
        radio_line('label', data['name'])
        for rad in range(data['radioLength']):
            radio_doc.input(('v-model', data['vmodel']), name=data['name'], type='radio', value=data['values'][rad])
            radio_text(data['label'][rad])
        print(radio_doc.getvalue())
        input()
    return radio_doc.getvalue()


def checkbox_field(data):
    checkbox_doc, checkbox_tag, checkbox_text, checkbox_line = Doc().ttl()
    with checkbox_tag('div', klass="form-group"):
        checkbox_line('label', data['name'])
        for check in range(data['checkLength']):
            checkbox_doc.input(('v-model', data['vmodel']), name=data['name'], type='checkbox',
                               value=data['values'][check])
            checkbox_text(data['label'][check])
    return checkbox_doc.getvalue()


def date_field(data):
    date_doc, date_tag, date_text = Doc(
        defaults={data['name']: ''}, errors={data['name']: ''}
    ).tagtext()
    rdnl = 'readonly' if data['readonly'] == 'y' else 'test'
    with date_tag('div', klass="form-group"):
        with date_tag('label', ('for', data['id'])):
            date_text(modeler(data))
        date_doc.input(('v-model', data['vmodel']), (rdnl, ''), name=data['name'], type='date',
                       id=data['id'], klass='form-control')
    return date_doc.getvalue()


def time_field(data):
    time_doc, time_tag, time_text = Doc(
        defaults={data['name']: ''}, errors={data['name']: ''}
    ).tagtext()
    rdnl = 'readonly' if data['readonly'] == 'y' else 'test'
    with time_tag('div', klass="form-group"):
        with time_tag('label', ('for', data['id'])):
            time_text(modeler(data))
        time_doc.input(('v-model', data['vmodel']), (rdnl, ''), name=data['name'], type='time',
                       id=data['id'], klass='form-control')
    return time_doc.getvalue()


def month_field(data):
    month_doc, month_tag, month_text = Doc(
        defaults={data['name']: ''}, errors={data['name']: ''}
    ).tagtext()
    rdnl = 'readonly' if data['readonly'] == 'y' else 'test'
    with month_tag('div', klass="form-group"):
        with month_tag('label', ('for', data['id'])):
            month_text(modeler(data))
        month_doc.input(('v-model', data['vmodel']), (rdnl, ''), name=data['name'], type='month',
                        id=data['id'], klass='form-control')
    return month_doc.getvalue()


def week_field(data):
    week_doc, week_tag, week_text = Doc(
        defaults={data['name']: ''}, errors={data['name']: ''}
    ).tagtext()
    rdnl = 'readonly' if data['readonly'] == 'y' else 'test'
    with week_tag('div', klass="form-group"):
        with week_tag('label', ('for', data['id'])):
            week_text(modeler(data))
        week_doc.input(('v-model', data['vmodel']), (rdnl, ''), name=data['name'], type='week',
                       id=data['id'], klass='form-control')
    return week_doc.getvalue()


def datetime_field(data):
    datetime_doc, datetime_tag, datetime_text = Doc(
        defaults={data['name']: ''}, errors={data['name']: ''}
    ).tagtext()
    rdnl = 'readonly' if data['readonly'] == 'y' else 'test'
    with datetime_tag('div', klass="form-group"):
        with datetime_tag('label', ('for', data['id'])):
            datetime_text(modeler(data))
        datetime_doc.input(('v-model', data['vmodel']), (rdnl, ''), name=data['name'], type='datetime-local',
                           id=data['id'], klass='form-control')
    return datetime_doc.getvalue()


def number_field(data):
    number_doc, number_tag, number_text = Doc(
        defaults={data['name']: ''}, errors={data['name']: ''}
    ).tagtext()
    rdnl = 'readonly' if data['readonly'] == 'y' else 'test'
    with number_tag('div', klass="form-group"):
        with number_tag('label', ('for', data['id'])):
            number_text(modeler(data))
        number_doc.input(('v-model', data['vmodel']), (rdnl, ''), name=data['name'], type='number',
                         id=data['id'], klass='form-control')
    return number_doc.getvalue()


def range_field(data):
    number_doc, number_tag, number_text = Doc(
        defaults={data['name']: ''}, errors={data['name']: ''}
    ).tagtext()
    rdnl = 'readonly' if data['readonly'] == 'y' else 'test'
    with number_tag('div', klass="form-group"):
        with number_tag('label', ('for', data['id'])):
            number_text(modeler(data))
        number_doc.input(('v-model', data['vmodel']), (rdnl, ''), name=data['name'], type='range', min=data['min'],
                         max=data['max'], id=data['id'], klass='form-control')
    return number_doc.getvalue()


def color_field(data):
    color_doc, color_tag, color_text = Doc(
        defaults={data['name']: ''}, errors={data['name']: ''}
    ).tagtext()
    rdnl = 'readonly' if data['readonly'] == 'y' else 'test'
    with color_tag('div', klass="form-group"):
        with color_tag('label', ('for', data['id'])):
            color_text(modeler(data))
        color_doc.input(('v-model', data['vmodel']), (rdnl, ''), name=data['name'], type='color',
                        id=data['id'], klass='form-control')
    return color_doc.getvalue()


def search_field(data):
    search_doc, search_tag, search_text = Doc(
        defaults={data['name']: ''}, errors={data['name']: ''}
    ).tagtext()
    rdnl = 'readonly' if data['readonly'] == 'y' else 'test'
    with search_tag('div', klass="form-group"):
        with search_tag('label', ('for', data['id'])):
            search_text(modeler(data))
        search_doc.input(('v-model', data['vmodel']), (rdnl, ''), name=data['name'], type='search',
                         id=data['id'], klass='form-control')
    return search_doc.getvalue()


def file_field(data):
    file_doc, file_tag, file_text = Doc(
        defaults={data['name']: ''}, errors={data['name']: ''}
    ).tagtext()
    rdnl = 'readonly' if data['readonly'] == 'y' else 'test'
    with file_tag('div', klass="form-group"):
        with file_tag('label', ('for', data['id'])):
            file_text(modeler(data))
        file_doc.input(('v-model', data['vmodel']), (rdnl, ''), name=data['name'], type='file',
                       id=data['id'], klass='form-control')
    return file_doc.getvalue()


def button(data):
    button_doc = Doc()
    button_doc.stag('input', type='button', value=data["value"], id=data['id'], klass="btn btn-primary btn-lg")
    return button_doc.getvalue()
