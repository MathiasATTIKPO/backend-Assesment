from asyncio.windows_events import NULL
import os
from typing import Optional
from urllib import response

import uvicorn
from fastapi import FastAPI , Request,  Response 

import requests
import httpx 

url = "https://api.hatchways.io/assessment/blog/posts?tag=tech"


app = FastAPI(title="Backend Assessment")


#route 1 
@app.get('/api/ping' )
def ping( response:Response ):
        response.status_code = 200
        return{"success": True }

# route to  to get all posts
@app.get('/api/get_Posts')
def get_Posts(request:Request ):
    Posts = requests.get(url)
    posts = Posts.json()
    return posts

# route 2 to get posts with tags , sortBy , direction
@app.get('/api/posts')
def post( response:Response ,  tags :Optional[str] = None   , sortBy :Optional[str] = None , direction :Optional[str] = None  ) :
    cmd1 = httpx.get(url)
    posts = (cmd1.json().get('posts'))
    tag = tags
    print(tag)
    #print(posts)
    
    if tag is not None :
        if direction == "ASC" or direction == "asc" or direction == "desc" or direction == "DESC":
                if sortBy == "id":
                    post_find = [post for post in posts if  tags.lower() in post["tags"]]
                    post_find.sort(key=lambda  x: x["id"] , reverse=True)

                    if not post_find:
                        response.status_code=400
                        return "Not Posts Found"
                    else:
                        return post_find if len(post_find) >1 else post_find[0] 
                
                elif sortBy =="likes":
                    post_find = [post for post in posts if  tags.lower() in post["tags"]]
                    post_find.sort(key=lambda  x: x["id"] , reverse=True)

                    if not post_find:
                        response.status_code=400
                        return "Not Posts Found"
                    else:
                        return post_find if len(post_find) >1 else post_find[0] 
        
                elif sortBy =="reads":
                    post_find = [post for post in posts if  tags.lower() in post["tags"]]
                    post_find.sort(key=lambda  x: x["id"] , reverse=True)

                    if not post_find:
                        response.status_code=400
                        return "Not Posts Found"
                    else:
                        return post_find if len(post_find) >1 else post_find[0] 

                elif sortBy =="popularity":
                    post_find = [post for post in posts if  tags.lower() in post["tags"]]
                    post_find.sort(key=lambda  x: x["id"] , reverse=True)

                    if not post_find:
                        response.status_code=400
                        return "Not Posts Found"
                    else:
                        return post_find if len(post_find) >1 else post_find[0] 

                elif sortBy==" " or sortBy==NULL:
                    response.status_code=400
                    return {"error":"sortBy parameter is invalid"}
                else :
                    response.status_code=400
                    return {"error":"sortBy parameter is invalid"}
         
        elif direction==" " or direction==NULL :
            response.status_code=400
            return {"error":"direction parameter is invalid"}

        else:
            response.status_code=400
            return {"error":"direction parameter is invalid"}
    
    elif tag is None :
        response.status_code=400
        return {"error":"tags parameter is required"}


if __name__ == "__main__":
     uvicorn.run(app, host="0.0.0.0", port=8000)