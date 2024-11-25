import os
from fastapi import FastAPI, HTTPException, APIRouter, Depends, Request
from typing import Optional
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

# Initialize FastAPI app
app = FastAPI()

# Retrieve API Key from environment variables for secure access
SECRET_API_KEY = os.getenv("LAB4_API_KEY")

# Middleware function to check the API Key for authorization
def check_api_key(request: Request):
    key_from_request = request.headers.get("DI-KEY")
    if key_from_request != SECRET_API_KEY:
        raise HTTPException(status_code=401, detail="Unauthorized: Invalid API Key")
    return key_from_request

# In-memory simulation of a database for storing activities
activity_database = [
    {"activity_id": 1, "name": "Complete Lab 4", "details": "Finish the assigned lab work", "is_done": False}
]

# Pydantic model for validating activity input
class Activity(BaseModel):
    name: str
    details: Optional[str] = ""
    is_done: bool = False

# Router for API version 1
v1_router = APIRouter()

@v1_router.get("/activities/{activity_id}")
def get_activity_v1(activity_id: int, api_key: str = Depends(check_api_key)):
    activity = next((a for a in activity_database if a["activity_id"] == activity_id), None)
    if not activity:
        raise HTTPException(status_code=404, detail=f"Activity with ID {activity_id} not found.")
    return activity

@v1_router.post("/activities/")
def create_activity_v1(activity: Activity, api_key: str = Depends(check_api_key)):
    new_activity_id = len(activity_database) + 1
    new_activity = activity.dict()
    new_activity["activity_id"] = new_activity_id
    activity_database.append(new_activity)
    return JSONResponse(status_code=201, content={"message": "Activity successfully created.", "activity": new_activity})

@v1_router.patch("/activities/{activity_id}")
def update_activity_v1(activity_id: int, activity: Activity, api_key: str = Depends(check_api_key)):
    activity_to_update = next((a for a in activity_database if a["activity_id"] == activity_id), None)
    if not activity_to_update:
        raise HTTPException(status_code=404, detail=f"Activity with ID {activity_id} not found.")
    activity_to_update.update(activity.dict())
    return JSONResponse(status_code=200, content={"message": "Activity updated successfully."})

@v1_router.delete("/activities/{activity_id}")
def delete_activity_v1(activity_id: int, api_key: str = Depends(check_api_key)):
    activity_to_delete = next((a for a in activity_database if a["activity_id"] == activity_id), None)
    if not activity_to_delete:
        raise HTTPException(status_code=404, detail=f"Activity with ID {activity_id} not found.")
    activity_database.remove(activity_to_delete)
    return JSONResponse(status_code=204, content={"message": "Activity deleted successfully."})

# Router for API version 2
v2_router = APIRouter()

@v2_router.get("/activities/{activity_id}")
def get_activity_v2(activity_id: int, api_key: str = Depends(check_api_key)):
    activity = next((a for a in activity_database if a["activity_id"] == activity_id), None)
    if not activity:
        raise HTTPException(status_code=404, detail=f"Activity with ID {activity_id} not found.")
    return activity

@v2_router.post("/activities/")
def create_activity_v2(activity: Activity, api_key: str = Depends(check_api_key)):
    new_activity_id = len(activity_database) + 1
    new_activity = activity.dict()
    new_activity["activity_id"] = new_activity_id
    activity_database.append(new_activity)
    return JSONResponse(status_code=201, content={"message": "Activity created in v2.", "activity": new_activity})

@v2_router.patch("/activities/{activity_id}")
def update_activity_v2(activity_id: int, activity: Activity, api_key: str = Depends(check_api_key)):
    activity_to_update = next((a for a in activity_database if a["activity_id"] == activity_id), None)
    if not activity_to_update:
        raise HTTPException(status_code=404, detail=f"Activity with ID {activity_id} not found.")
    activity_to_update.update(activity.dict())
    return JSONResponse(status_code=200, content={"message": "Activity updated in v2."})

@v2_router.delete("/activities/{activity_id}")
def delete_activity_v2(activity_id: int, api_key: str = Depends(check_api_key)):
    activity_to_delete = next((a for a in activity_database if a["activity_id"] == activity_id), None)
    if not activity_to_delete:
        raise HTTPException(status_code=404, detail=f"Activity with ID {activity_id} not found.")
    activity_database.remove(activity_to_delete)
    return JSONResponse(status_code=204, content={"message": "Activity deleted in v2."})

# Include the versioned routers for API access
app.include_router(v1_router, prefix="/apiv1")
app.include_router(v2_router, prefix="/apiv2")

# Root endpoint to check the server
@app.get("/")
def home():
    return {"message": "API is running. Use /apiv1 or /apiv2 for activity management."}

# Health endpoint to check the status of the API
@app.get("/health")
def health():
    return {"status": "API is up and running"}
