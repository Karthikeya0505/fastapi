from fastapi import FastAPI
from enum import Enum
app = FastAPI()

class AvailableItems(str,Enum):
    indian = 'indian'
    english = 'english'
    italian = 'italian'

food_items = {
    'indian' : ['samosa','pani puri'],
    'english' : ['pizza','maccoroni'],
    'italian' : ['ravioli']
}
@app.get('/get_items/{cuisine}')

async def get_items(cuisine: AvailableItems):
    return food_items.get(cuisine)


coupon = {
    1:'10%',
    2:'20%'
}

@app.get('/get_coupon/{code}')

async def coupon(code: int):
    return {'discounted amount': coupon.get(code)}