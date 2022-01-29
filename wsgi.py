def start_applic():
    from joshua.app import App
    from joshua.request import Request
    from joshua.request import Request
    from joshua.response import HttpResponse
    from joshua.router import Path
    from wsgiref.simple_server import make_server
    import time
    print('Enter the html or text you wanna reflect on the client side')
    output = input()

    app = App()

    def hellowrodl(request: Request):
        return HttpResponse(request, output)

    routes = [
        Path('/', hellowrodl)
    ]
    app.set_routes(routes)
    serverh = make_server("127.0.0.1", 8080, app)
    print('Server Listening On Port 8080')
    print('Printing Log')
    serverh.serve_forever()
    input("Press enter to proceed...")
import time
while 10 != 11:
    start_applic()
    time.sleep(999999999999999999999999999999999999999999999999999999999999999999999999999)