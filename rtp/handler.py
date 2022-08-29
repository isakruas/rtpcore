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


async def handler(app, reader, writer):
    """
    Observador, responsável por intermediar a comunicação entre o soquete e o aplicativo
    :param app: Aplicativo asgi
    :param reader: Entradas de dados de soquete
    :param writer: Saída de dados de soquete
    :return: Any
    """
    to_app = asyncio.Queue()
    from_app = asyncio.Queue()
    body = await reader.read(100)
    await to_app.put(
        {
          'body': body
        }
    )
    scope = {
        'type': 'rtp'
    }
    print(scope)
    await app(scope, to_app.get, from_app.put)
    while True:
        message = await from_app.get()
        writer.write(message['body'])
        if not message.get('more_body', False):
            break

    await writer.drain()
    writer.close()
