from fastapi import Header,HTTPException, status

DEMO_API_KEY = "student-secret-key"

def verify_api_key(x_api_key:str |None=Header(default=None)) -> str:
    if x_api_key!= DEMO_API_KEY:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or missing API key",
        )
    return x_api_key