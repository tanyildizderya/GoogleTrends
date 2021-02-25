import uvicorn
from google_trends import *
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def main_page():
    return {"Google Trends Query Search App"}

@app.get('/search/keyword')
async def interest_over_time():
    return search_json


@app.get('/keyword/region')
async def region_based():
    return region_json


@app.get('/related/queries')
async def related_queries():
    return related_query_json


@app.get('/related/topics')
async def related_topics():
    return related_topic_json

if __name__ == '__main__':
    uvicorn.run("fastAPI:app", host="127.0.0.1", port=3000)
