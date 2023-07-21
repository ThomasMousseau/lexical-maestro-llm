from fastapi import FastAPI
import asyncio
import subprocess
import uvicorn

app = FastAPI()

@app.get('/data')
async def get_data():
    data = await fetch_data()
    return {'data': data}

async def fetch_data():
    await asyncio.sleep(1)
    return 'Async data'

async def run_subprocess(cmd):
    process = await asyncio.create_subprocess_exec(*cmd,
                                                   stdout=asyncio.subprocess.PIPE,
                                                   stderr=asyncio.subprocess.PIPE)
    stdout, stderr = await process.communicate()
    return stdout, stderr


@app.get('/question/{prompt}')
async def get_data(prompt: str):
    try:
        gpt_script = 'privateGPT-Answer.py', prompt
        stdout, stderr = await run_subprocess(['python'] + list(gpt_script))
        return stdout.decode('utf-8'), 200 if stderr == b'' else 500
    except Exception as e:
        return str(e), 500

if __name__ == '__main__':
    uvicorn.run(app)
