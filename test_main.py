from urllib import response
from fastapi.testclient import TestClient
import json


from main import app , get_Posts

client = TestClient(app)

def test_ping():
    response = client.get('/api/ping')
    assert response.status_code == 200
    assert response.json()=={"success": True }

def test_post():
    data ={"tags":"health" , "sortBy":"id" , "direction":"asc"}
    response = client.get('/api/posts?tags=health&sortBy=id&direction=asc' )
    assert response.status_code == 200
    assert response.json()==[ {
    "author": "Jon Abbott",
    "authorId": 4,
    "id": 95,
    "likes": 985,
    "popularity": 0.42,
    "reads": 55875,
    "tags": [
      "politics",
      "tech",
      "health",
      "history"
    ]
  },
  {
    "author": "Lainey Ritter",
    "authorId": 1,
    "id": 76,
    "likes": 122,
    "popularity": 0.01,
    "reads": 75771,
    "tags": [
      "tech",
      "health",
      "politics"
    ]
  },
  {
    "author": "Adalyn Blevins",
    "authorId": 11,
    "id": 37,
    "likes": 107,
    "popularity": 0.55,
    "reads": 35946,
    "tags": [
      "tech",
      "health",
      "history"
    ]
  },
  {
    "author": "Rylee Paul",
    "authorId": 9,
    "id": 1,
    "likes": 960,
    "popularity": 0.13,
    "reads": 50361,
    "tags": [
      "tech",
      "health"
    ]
  }
    ]

def test_post_tags():
    response= client.get('/api/posts?sortBy=id&direction=desc')
    assert response.status_code == 400
    assert response.json()=={"error": "tags parameter is required"}

def test_post_tags():
    response= client.get('/api/posts?tags=%20blaaaa&sortBy=id&direction=desc')
    assert response.status_code == 400
    assert response.json()=="Not Posts Found"

def test_post_sortBy():
    response= client.get('/api/posts?tags=health&sortBy=%20&direction=desc')
    assert response.status_code == 400
    assert response.json()=={"error": "sortBy parameter is invalid"}

def test_post_direction():
    response= client.get('/api/posts?sortBy=id&direction=%20')
    assert response.status_code == 400
    assert response.json()=={"error": "tags parameter is required"}