
import asyncio

from chapter18.flags_asyncio import get_flag


@asyncio.coroutine
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
        loop = asyncio.get_event_loop()
        loop.run_in_executor(
            None, save_flag, image, cc.lower() + '.gif'
            )
        status = HTTPStatus.OK
        msg = 'OK'
        
    if verbose and msg:
        print(cc, msg)
        
    return Result(status, cc)