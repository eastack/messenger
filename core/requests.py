from core.environments import session


def show_result(response):
    print(f'Status Code: {response.status_code}')
    print(f'Result: {response.text}')


class Requests:
    @staticmethod
    def delete(url):
        response = session().delete(url)
        show_result(response)
        return response
