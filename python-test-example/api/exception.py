# -*- encoding: utf-8 -*-
import traceback


class HTTPError(Exception):
    """Base class for http error"""

    def __init__(self, title: str, description: str, code: int) -> None:
        self.title = title
        self.description = description
        self.code = code

    def to_dict(self) -> dict:
        error = {
            'message': self.title,
            'derail': self.description,
            'code': self.code
        }
        return {'Error': error}


class BadRequest(HTTPError):
    """400 Bad Request"""

    def __init__(self, title='Bad Request', description=''):
        super().__init__(title, description, code=400)


class Forbidden(HTTPError):
    """403 Forbidden"""

    def __init__(self, title='Forbidden', description=''):
        super().__init__(title, description, code=403)


class NotFound(HTTPError):
    """404 Not Found"""

    def __init__(self, title='Not Found', description=''):
        super().__init__(title, description, code=404)


class InternalServerError(HTTPError):
    """500 Internal Server Error"""

    def __init__(self, title='Internal Server Error', description=''):
        super().__init__(title, description, code=500)


def error_handler(error):
    """
    error handler for session
    :param error: Exception object
    :raises: BadRequest | InternalServerError
    """
    if not error:
        return
    try:
        traceback.print_exc()
        raise error
    except (ValueError, KeyError):
        raise BadRequest()
    except Exception:
        raise InternalServerError()
