from fastapi import APIRouter, HTTPException
from src.backend.state.SceneState import SceneState

router = APIRouter()

@router.get("/api/scene")
async def get_scene():
    """Retrieve the current scene data."""
    try:
        scene_data = SceneState.get_scene_data()
        return {"status": "success", "scene_data": scene_data}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/api/scene/update")
async def update_scene(scene_update: dict):
    """Update the scene with new data."""
    try:
        SceneState.update_scene(scene_update)
        return {"status": "success", "message": "Scene updated successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))