import json
from fastapi import Request, FastAPI

from fastapi.middleware.cors import CORSMiddleware
import chatting
app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/generate")
async def read_root(request: Request):
        payload = await request.json()
        print(payload['message'])

        res = chatting.generate(payload['message'])
        print('This is result')
        print(res)
        return {
            'result': res
        }
