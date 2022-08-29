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
import rtp


async def application(scope, receive, send):
    print('application(scope, receive, send)')
    print(scope, receive, send)
    event = await receive()
    event.update({'more_body': True})
    await send(
        event
    )
    await send(
        {
            'body': '\na aplicação retornou dados'.encode('utf-8'),
        }
    )


if __name__ == '__main__':
    rtp.run(f'{__name__}:application')
