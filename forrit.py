from bottle import route, run, template, static_file,error, os, request
import json

with open('bekkur.json','r', encoding='UTF-8')as f:

    bekkur = json.load(f)

@route('/')
def index():
    return template('verk_4',bekkur=bekkur)

@route('/nemandi/<kt>')
def nemandi(kt):
    found = False
    for nemandi in bekkur['nemendur']:
        if nemandi['kt']== kt:
            return template('verk_4_nemandi',nemandi=nemandi)
            found = True
    if found  == False:
        return error500()

@route('/static/<filename>')
def server_static(filename):
    return static_file(filename, root='./resources')


@error(404)
def error404(error):
    return '<h1>Þessi siða er ekki til</h1>' \
            '<a href="../">Til baka</a>'

@error(500)
def error500(error):
    return '<h1>Þessi siða er ekki til</h1>' \
           '<a href="../">Til baka</a>'



run(host="0.0.0.0", port=os.environ.get('PORT'))
