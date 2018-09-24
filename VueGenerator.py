from _datetime import datetime

vue = '<script src="https://cdn.jsdelivr.net/npm/vue@2.5.17/dist/vue.js"></script>'
bootstrap = '<link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Roboto:300,400,500,700|Material+Icons"><link rel="stylesheet" href="https://unpkg.com/bootstrap-material-design@4.1.1/dist/css/bootstrap-material-design.min.css" integrity="sha384-wXznGJNEXNG1NFsbm0ugrLFMQPWswR3lds2VeinahP8N0zJw9VWSopbjv2x7WCvX" crossorigin="anonymous">'
script = "<script>var app = new Vue({  el: '#app',  data: {    message: 'Hello Vue!'  }})</script>"
data = {}


def makedict_k(**kwargs):
    return kwargs


def makedict(*args):
    return args


# str and array
def data_injector(model, *args):
    global data
    if len(args) > 0:
        if model and args[0]:
            data[model] = []
    elif model:
        data[model] = ''
    print(data)
    data['message'] = datetime.now().strftime("%d %a %Y %I:%M %p")
    tt = makedict(data)
    t = "<script>var app = new Vue({  el: '#app',  data: " + str(tt)[1:-1] + "   })</script>"
    print(t)
    return t


def combine_content(html):
    middle = bootstrap + vue + html
    return middle + data_injector(False)

# data_injector()
