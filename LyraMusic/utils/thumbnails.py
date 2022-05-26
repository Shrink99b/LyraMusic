#
# Copyright (C) 2022-2023 by NitricXd@Github, < https://github.com/NitricXd >.
#
# This file is part of < https://github.com/NitricXd/LyraMusic > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/NitricXd/LyraMusic/blob/master/LICENSE >
#
# All rights reserved.
#

import os
import aiohttp
import aiofiles

from config import MUSIC_BOT_NAME, YOUTUBE_IMG_URL

async def gen_thumb(videoid):
    if os.path.isfile(f"cache/techz{videoid}.png"): 
        return f"cache/techz{videoid}.png"

    url = f"https://techzbotsapi.herokuapp.com/thumb?videoid={videoid}&botname={MUSIC_BOT_NAME}"
    
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as resp:
                if resp.status == 200:
                    f = await aiofiles.open(f"cache/techz{videoid}.png", mode="wb" ) 
                    await f.write(await resp.read()) 
                    await f.close()

        return f"cache/techz{videoid}.png"
    except Exception:
        return YOUTUBE_IMG_URL
