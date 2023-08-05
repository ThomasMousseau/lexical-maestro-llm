from fastapi import FastAPI
import asyncio
import subprocess
import uvicorn
import pickle
from privateGPT import getAnswer 

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
    await process.wait()
    stdout, stderr = await process.communicate()
    return stdout, stderr

@app.get('/question/{prompt}')
async def get_data(prompt: str):
    #convert space into %20 to get the complete prompt
    try:
        setup_script = ['python', 'setupPrivateGPT.py']
        completed_process = subprocess.run(setup_script, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

        with open("output.pkl", "rb") as f:
            result = pickle.load(f)

        arguments = [completed_process, prompt]
        command = ['python', 'privateGPT.py', arguments]
        stdout, stderr = await run_subprocess(command)
        stdout = stdout.decode('utf-8')
        
        gpt_script = 'privateGPT.py', prompt
        stdout, stderr = await run_subprocess(['python'] + list(gpt_script))
        return stdout.decode('utf-8')
        #, 200 if stderr == b'' else 500
    except Exception as e:
        return str(e), 500


@app.get('/questionv2/{prompt}')
async def get_data(prompt: str):
    #convert space into %20 to get the complete prompt
    try:
        return getAnswer(prompt), 200
    except Exception as e:
        return str(e), 500

if __name__ == '__main__':
    uvicorn.run(app)