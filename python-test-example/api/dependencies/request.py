# -*- encoding: utf-8 -*-
from typing import Optional

from fastapi import Depends, Request
from pydantic import BaseModel

from .auth import User, auth


class ClientData(BaseModel):
    user: User


class ServerData(BaseModel):
    host: Optional[str] = ''
    port: Optional[int] = 8080


class State(BaseModel):
    client: ClientData
    server: ServerData


def base_state(
        request: Request,
        user: User = Depends(auth)
) -> State:
    client_data = ClientData(user=user)
    host, port = request.url.hostname, request.url.port
    state = State(client=client_data, server=ServerData(host=host, port=port))
    return state
