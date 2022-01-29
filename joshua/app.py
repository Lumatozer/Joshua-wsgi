from joshua.request import Request
from joshua.response import Http404,FileResponse,Response
from joshua.router import Router,Path

class App:
    def __init__(self):
        self.router = Router()
        self.static_dir = None  # this sotres paths to all static filez
        self.static_path = None  # specifies prefix of the url of all requests with static file requests

        def set_static(self, static_path, static_dir):
            # this function makes the required settinz for our static file requests
            self.static_dir = static_dir
            self.static_path = static_path

        def serve_static(self, request: Request):
            new_path = request.path[len(self.static_path)::]  # this gets the actual files path name
            return FileResponse(request, os.path.join(self.static_dir, new_path))

    def set_routes(self, routes: list):
        # this function takes the list of the paths and then adds them to the apps router list
        for path in routes:
            self.router.add_route(path)

    def __call__(self, environ, start_response):
        try:
            request = Request(environ, start_response)
            # this checks whether we are pointing to a file or dir :)
            if self.static_path !=None and  request.path.startswith(self.static_path):
                response = self.serve_static(request)
                return response.make_response()
            else:
                func = self.router.get_route(request.path)
                if func is not None:
                    response: Response = func(request)
                    return response.make_response()
                else:
                    print(f'route Not found : {request.path}')
        except Exception as e:

            print(e)

        response =  Http404(request)
        return response.make_response()