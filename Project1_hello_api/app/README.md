# Project 1 - Hello API

go to project folder 

    cd Project1_hello_api 

## Run
```bash
uvicorn app.main:app --reload
```

Open
    
    API: http://127.0.0.1:8000
    Docs: http://127.0.0.1:8000/docs

### Meaning of this command
* uvicorn → server runner
* app.main → file path app/main.py
* app → FastAPI object inside that file
* --reload → auto-restart on code change

###  Test endpoint 1
GET /

Response:
``` json
{
  "message": "Welcome to Project 1: Hello API",
  "docs": "/docs"
}
```

### Test endpoint 2

GET /hello/{name}

Example:

/hello/Saib

Response:
``` json
{
  "success": true,
  "reply": "Hello, Saib! Your API is working."
}
``` 

