from fastapi import FastAPI, HTTPException
from schemas import AnimeNewsCreate, AnimeNewsUpdate, AnimeNewsResponse
from storage_pkg.storage import (
    get_all_news,
    get_news_by_id,
    create_news,
    update_news,
    delete_news,
)

app = FastAPI(title="Anime News API")


@app.get("/")
def root():
    return {"message": "Anime News API is running"}


@app.get("/news", response_model=list[AnimeNewsResponse])
def read_all_news():
    return get_all_news()


@app.get("/news/{news_id}", response_model=AnimeNewsResponse)
def read_one_news(news_id: int):
    news = get_news_by_id(news_id)
    if not news:
        raise HTTPException(status_code=404, detail="News item not found")
    return news


@app.post("/news", response_model=AnimeNewsResponse)
def create_one_news(news: AnimeNewsCreate):
    return create_news(news.dict())


@app.put("/news/{news_id}", response_model=AnimeNewsResponse)
def update_one_news(news_id: int, news: AnimeNewsUpdate):
    updated_news = update_news(news_id, news.dict())
    if not updated_news:
        raise HTTPException(status_code=404, detail="News item not found")
    return updated_news


@app.delete("/news/{news_id}")
def delete_one_news(news_id: int):
    delete_result = delete_news(news_id)
    if not delete_result:
        raise HTTPException(status_code=404, detail="News item not found")
    return {"message": "News item deleted successfully"}    
