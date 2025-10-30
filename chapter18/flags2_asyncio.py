import asyncio
import collections

import aiohttp
from aiohttp import web
import tqdm

from chapter17.flags2_sequential import main, HTTPStatus, Result, save_flag

DEFAULT_CONCUR_REQ = 5
MAX_CONCUR_REQ = 1000

class FetchError(Exception):
    def __init__(self, country_code):
        self.country_code = country_code

@asyncio.coroutine
def get_flag(base_url, cc):
    url = '{}/{cc}/{cc}.gif'.format(base_url, cc=cc.lower())
    resp = yield from aiohttp.request("GET", url)
    if resp.status == 200:
        image = yield from resp.read()
        return image
    elif resp.status == 404:
        raise web.HTTPNotFound()
    
    else:
        raise aiohttp.HtpProccessingError(
            code=resp.status, message=resp.reason,
            headers=resp.headers
        )        
        
        
def download_one(cc, base_url, semaphore, verbose):
    try:
        with (yield from semaphore):
            image = yield from get_flag(base_url, cc)
    except web.HTTPNotFound:
        status = HTTPStatus.NOT_FOUND
        msg = 'not found'
    except Exception as exc:
        raise FetchError(cc) from exc
    
    else:
        save_flag(image, cc.lower() + '.gif')
        status = HTTPStatus.OK
        msg = 'OK'
        
        
    if verbose and msg:
        print(cc, msg)
        
    return Result(status, cc)