from asyncio.windows_events import NULL
import os
from urllib import response


import uvicorn
from fastapi import FastAPI , Request,  Response 
import requests

url = "https://api.hatchways.io/assessment/blog/posts?tag=tech"


app = FastAPI(title="Backend Assessment")

@app.get('/api/get_Posts')
def get_Posts(request:Request ):
    Posts = requests.get(url)
    posts = Posts.json()
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
def post(  tags , sortBy , direction , response:Response  ) :
    Posts = requests.get(url)
    posts = Posts.json()
    if direction == "ASC" or direction == "asc":
        if sortBy == "id":
            post_find = [post for post in posts if  tags.lower() in post["tags"].json()]
            post_find.sort(key=lambda  x: x["id"] , reverse=True)

            if not post_find:
                response.status_code=404
                return "Not Posts Found"
            else:return post_find if len(post_find) >1 else post_find[0] 
        
        elif sortBy =="likes":
            post_find = [post for post in posts if  tags.lower() in post[2]]
            post_find.sort(key=lambda  x: x["likes"] , reverse=True)

            if not post_find:
                response.status_code=404
                return "Not Posts Found"
            else:return post_find if len(post_find) >1 else post_find[0]
        
        elif sortBy =="reads":
            post_find = [post for post in posts if  tags.lower() in post[2]]
            post_find.sort(key=lambda  x: x["reads"] , reverse=True)

            if not post_find:
                response.status_code=404
                return "Not Posts Found"
            else:return post_find if len(post_find) >1 else post_find[0]

        elif sortBy =="popularity":
            post_find = [post for post in posts if  tags.lower() in post[2]]
            post_find.sort(key=lambda  x: x["popularity"] , reverse=True)

            if not post_find:
                response.status_code=404
                return "Not Posts Found"
            else:return post_find if len(post_find) >1 else post_find[0]
            # return post_find_sort

    elif direction == "DESC" or direction == "desc":
            if sortBy == "id":
                post_find = [post for post in posts if  tags.lower() in post[2]]
                post_find.sort(key=lambda  x: x["id"] , reverse=True)

                if not post_find:
                    response.status_code=404
                    return "Not Posts Found"
                else:return post_find if len(post_find) >1 else post_find[0] 

            elif sortBy =="likes":
            
                post_find = [post for post in posts if  tags.lower() in post[2]]
                post_find.sort(key=lambda  x: x["likes"] , reverse=True)

                if not post_find:
                    response.status_code=404
                    return "Not Posts Found"
                else:return post_find if len(post_find) >1 else post_find[0]
        
            elif sortBy =="reads":
                post_find = [post for post in posts if  tags.lower() in post[2]]
                post_find.sort(key=lambda  x: x["reads"] , reverse=True)

                if not post_find:
                    response.status_code=404
                    return "Not Posts Found"
                else:return post_find if len(post_find) >1 else post_find[0]

            elif sortBy =="popularity":
                post_find = [post for post in posts if  tags.lower() in post[2]]
                post_find.sort(key=lambda  x: x["popularity"] , reverse=True)

                if not post_find:
                    response.status_code=404
                    return "Not Posts Found"
                else:return post_find if len(post_find) >1 else post_find[0]
                # return post_find_sort

            elif sortBy==" " or sortBy==NULL:
                return {"error":"direction paramter not valid"}
            else :
                return {"error":"direction paramter not valid"}
    
        


    #return {"request": request, "tag": tags}

    if __name__ == "__main__":
        uvicorn.run(app, host="0.0.0.0", port=8000)