from asyncio.windows_events import NULL
import os


import uvicorn
from fastapi import FastAPI , Request,  Response

app = FastAPI(title="Backend Assessment")


posts = [
    {"id": 1 , "author": "moi" , "authorId": 1  , "likes":20 , "popularity": 45, "reads": 100 , "tags" :["tech" , "santé"]} ,
    {"id":2 , "author": "toi","authorId": 2 , "likes":20 , "popularity": 45, "reads": 100 ,"tags" :["tech" , "football"]},
    {"id":3 , "author": "toi","authorId": 3  , "likes":20 , "popularity": 45, "reads": 100 , "tags" :["tech" , "basketball"]},
    {"id":4 , "author": "toi","authorId": 4  , "likes":20 , "popularity": 45, "reads": 100 , "tags" :["tech" , "automobile"]},
    {"id":5 , "author": "toi","authorId": 5  , "likes":20 , "popularity": 45, "reads": 100 , "tags" :["tech" , "Space"]}

]
    

@app.get('/api/get_posts')
def get_posts(request:Request ):
    return posts


@app.get('/api/ping', status_code=200)
def index(request:Request , response:Response):
    
    resp = response.status_code
    print(resp )
    if resp != 200:
        return{"success": True }
    else:
        return {"success": False}

@app.get('/api/posts')
def post(  tags , sortBy , response:Response  ) :

    if sortBy == "ASC" or sortBy == "asc":
        post_find = [post for post in posts if  tags.lower() in post["tags"]]
        post_find.sort(key=lambda  x: x["id"] , reverse=True)

        if not post_find:
            response.status_code=404
            return "Not Posts Found"
        else:return post_find if len(post_find) >1 else post_find[0]
       # return post_find_sort
    elif sortBy == "DESC" or sortBy == "desc":
        post_find = [post for post in posts if  tags.lower() in post["tags"]]
        post_find.sort(key=lambda  x: x["id"] , reverse=False)

        if not post_find:
            response.status_code=404
            return "Not Posts Found"
        else:return post_find if len(post_find) >1 else post_find[0]
        #return post_find_sort
    elif sortBy==" " or sortBy==NULL:
        return {"error":"SortBy paramter not valid"}
    else :
        return {"error":"SortBy paramter not valid"}
    
        


    #return {"request": request, "tag": tags}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)