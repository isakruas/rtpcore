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


async def send():
    reader, writer = await asyncio.open_connection('127.0.0.1', 8000)
    writer.write('mensagem'.encode('utf-8'))
    response = bytes()
    while True:
        read = await reader.read(100)
        if not read:
            break
        response += read
    writer.close()
    return response

r = asyncio.run(send())
print(r.decode('utf-8'))

