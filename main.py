from fastapi import FastAPI,status,Response

app = FastAPI()
@app.get("/info/{id}",status_code=200)
def get_info(id:int,response:Response):
    if id == 1:
        response.status_code = 418
        return {'error':'I am teapot'}
    elif id == 2:
        response.status_code = 451
        return {'error':'Unavailable For Legal Reasons'}
    else:
        response.status_code = 200
        return {'id':id}
