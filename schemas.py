from pydantic import BaseModel

class AnimeNewsBase(BaseModel):
    title: str
    link: str
    image_url: str

class AnimeNewsCreate(AnimeNewsBase):
    pass

class AnimeNewsUpdate(AnimeNewsBase):
    pass

class AnimeNewsResponse(AnimeNewsBase):
    id: int
