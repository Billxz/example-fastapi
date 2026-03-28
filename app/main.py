from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
# from fastapi.params import Body

from random import randrange
from . import models
from .database import engine
from .routers import posts, users, auth, vote
from .config import settings

# pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
# Switched to argon2 because of bycrypt's limited byte of 72

models.Base.metadata.create_all(bind=engine)

# Testing CORS
# fetch('http://localhost:8000/')
#   .then(response => response.json())
#   .then(data => console.log(data))
#   .catch(error => console.error('Error:', error));

# origins = ["https://www.google.com", "https://www.youtube.com"]
origins = ["*"]
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

my_posts = [{"title": "title of post 1", "content": "content of post 1", "id": 1},
            {"title": "favourite food", "content": "I love fufu", "id": 2}]


def find_posts(id):
    for p in my_posts:
        if p["id"] == id:
            return p


def find_index_posts(id):
    for i, p in enumerate(my_posts):
        if p['id'] == id:
            return i


# importing the external files
app.include_router(posts.router)
app.include_router(users.router)
app.include_router(auth.router)
app.include_router(vote.router)


@app.get("/")
async def root():
    return {"message": "Hello world"}

    # @app.get("/posts")
    # def get_posts():
    #     return {"data": my_posts}
    # @app.post("/createposts")
    # def create_posts(payload: dict = Body(...)):
    #     print(payload)
    #     return {"new_post": f"title : {payload['title']} content: {payload['content']}"}
    # Retrieving posts


# @app.post("/posts", status_code=status.HTTP_201_CREATED)
# def create_posts(post: Post):
#     post_dict = post.model_dump()
#     post_dict['id'] = randrange(0, 100000)
#     my_posts.append(post_dict)
#     return {"Data": post_dict}


# import Response and status from fastapi to return a valid response
# for error


# @app.get("/posts/{id}", status_code=status.HTTP_302_FOUND)
# def get_post(id: int, response: Response):
#     post = find_posts(id)
#     if not post:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
#                             detail=f"post with id: {id} was not found")
#         # response.status_code = 404
#         # response.status_code = status.HTTP_404_NOT_FOUND
#         # return {'message': f"post with id: {id} was not found"}
#     return {"post details": post}

# Get one post


# @app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
# def delete_post(id: int):
#     index = find_index_posts(id)

#     if index == None:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
#                             detail=f"post with id: {id} does not exist")
#     my_posts.pop(index)
#     # return {"message": f"post with id: {id} was successfully deleted"}
#     return Response(status_code=status.HTTP_204_NO_CONTENT)


# @app.put("/posts/{id}")
# def update_Post(id: int, post: Post):
#     # we first perform an iteration
#     index = find_index_posts(id)
#     if index == None:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
#                             detail=f"post with id: {id} does not exist")
#     post_dict = post.model_dump()
#     post_dict['id'] = id
#     my_posts[index] = post_dict
#     return {"data": post_dict}

# Updating post
