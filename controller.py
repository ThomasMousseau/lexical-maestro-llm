from fastapi import FastAPI
import asyncio
import subprocess
import uvicorn
import pickle
from privateGPT import getAnswer 

app = FastAPI() #root should be /api/

@app.get('/question/{prompt}')
async def get_data(prompt: str):
    #convert space into %20 to get the complete prompt
    try:
        return getAnswer(prompt), 200
    except Exception as e:
        return str(e), 500

@app.get('/health')
async def health():
    return 'OK', 200
    

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)