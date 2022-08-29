"""
/***********************************************************************
* Copyright (c) 2022 Isak Ruas                                        *
* Distributed under the MIT software license, see the accompanying    *
* https://github.com/isakruas/rtpcore/blob/master/LICENSE             *
***********************************************************************/
------------------------------------------------------------------------
Details: Ecutils module applications
Reference video: https://youtu.be/HQJnrWMufZg
Playlist: https://youtube.com/playlist?list=PL_AicbRG9Iu_OaQwn_sRsRaRnBmRkQt-L
--
----------------------------------------------------------------------
"""
import click
from importlib import import_module
from rtp.server import server
import asyncio
import typing


@click.command()
@click.argument('app')
@click.option(
    '--host',
    type=str,
    default='127.0.0.1',
    help='Bind socket to this host.',
    show_default=True
)
@click.option(
    '--port',
    type=int,
    default=8000,
    help='Bind socket to this port.',
    show_default=True
)
def main(
        app: str,
        host: str,
        port: int
) -> None:
    """
    Inicia o servidor RTP de um aplicativo (CLI)
    :param app: Aplicativo asgi
    :param host: Endereço ipv4
    :param port: Porta do endereço ipv4
    :return: server(app, host, port)
    """
    run(
        app,
        host=host,
        port=port
    )


def run(
        app: typing.Union[typing.Callable, str],
        *,
        host: str = '127.0.0.1',
        port: int = 8000
) -> None:
    """
    Inicia o servidor RTP de um aplicativo
    :param app: Aplicativo asgi
    :param host: Endereço ipv4
    :param port: Porta do endereço ipv4
    :return: server(app, host, port)
    """
    module_str, _, attrs_str = app.partition(':')

    # importar o aplicativo asgi
    app = import_module(module_str)

    for attr_str in attrs_str.split('.'):
        app = getattr(app, attr_str)

    # executar o observador do aplicativo
    asyncio.run(server(app, host, port))


if __name__ == '__main__':
    main()
