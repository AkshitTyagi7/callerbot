import json
from fastapi import Request, FastAPI
import detector
from fastapi.middleware.cors import CORSMiddleware
import chatgpt
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

        res = detector.guess(payload['message'])
        print('This is result')
        print(res)
        return {
            'result': res
        }
@app.post("/chatgpt")
async def read_root(request: Request):
        payload = await request.json()
        # print(payload['message'])

        res = chatgpt.createresponse(payload['message'])
        print('This is result')
        print(res)
        return {
            'result': res
        }