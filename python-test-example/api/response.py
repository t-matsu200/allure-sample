# -*- encoding: utf-8 -*-
from typing import Any

from fastapi.responses import JSONResponse

try:
    import orjson
except ImportError:
    orjson = None


class ApiJSONResponse(JSONResponse):
    media_type = 'application/json'

    def render(self, content: Any) -> bytes:
        if orjson is None:
            return super().render(content)
        return orjson.dumps(
            content,
            option=orjson.OPT_INDENT_2 | orjson.OPT_SERIALIZE_NUMPY
        )
