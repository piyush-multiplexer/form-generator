from yattag import Doc
from VueGenerator import combine_content


def parsed_data(otherData):
    doc, tag, text, line = Doc().ttl()

    with tag('div', id='app', klass='container'):
        line('h1', 'Generated Form -  {{message}}')
        with tag('form', action=""):
            doc.asis(otherData)

    print(doc.getvalue())

    f = open('index.html', "w")
    f.write(combine_content(doc.getvalue()))
