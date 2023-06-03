# -*- encoding: utf-8 -*-
import time
from typing import Awaitable, Callable

from fastapi import Request, Response


async def timer(
        request: Request,
        call_next: Callable[[Request], Awaitable[Response]]
) -> Response:
    start_time = time.time()
    response = await call_next(request)
    elapsed = time.time() - start_time
    response.headers['X-Response-Time'] = str(elapsed)
    return response
