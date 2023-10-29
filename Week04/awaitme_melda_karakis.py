import asyncio

def awaitme(fn):
    async def wrapper(*args, **kwargs):
        return await fn(*args, **kwargs)
    return wrapper
