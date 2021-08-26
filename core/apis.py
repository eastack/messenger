from core.environments import server


class HttpMethods:
    delete = f'{server()}/delete'
    post = f'{server()}/post'
