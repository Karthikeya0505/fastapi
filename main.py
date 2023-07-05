from fastapi import FastAPI

app = FastAPI()
@app.get('/{name}')

async def hello(name):
    return f'welcome {name}'