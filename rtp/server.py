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
import asyncio
from rtp.handler import handler


async def server(
        app,
        host,
        port
) -> None:
    """
    Inicia o servidor RTP de um aplicativo (CLI)
    :param app: Aplicativo asgi
    :param host: Endereço ipv4
    :param port: Porta do endereço ipv4
    :return: asyncio.start_server(app, reader, writer)
    """
    start = await asyncio.start_server(lambda reader, writer: handler(app, reader, writer), host, port)
    addrs = ', '.join(str(sock.getsockname()) for sock in start.sockets)
    print(f'Serving on {addrs}')
    async with start:
        await start.serve_forever()
