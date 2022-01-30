from joshua.app import App
from joshua.request import Request
from joshua.request import Request
from joshua.response import HttpResponse
from joshua.router import Path
from wsgiref.simple_server import make_server
import time
print("Enter/Paste your html or text content you wanna reflect on the client side.")
print('Type end to save it.')
contents = ''

while True:
    endingline = 'end'
    try:
        line = input()
    except EOFError:
        break
    if line == 'end':
        break
    else:
        contents= str(contents) + str(line)

output = contents
print('Enter the port on which you want the server to listen on.')
port = int(input())

app = App()


def uwu(request: Request):
    return HttpResponse(request, output)


routes = [
    Path('/', uwu)
]
app.set_routes(routes)
serverh = make_server("127.0.0.1", port, app)
print('Server Listening On Port ',port)
print('Printing Log')
serverh.serve_forever()
input("Press enter to proceed...")
