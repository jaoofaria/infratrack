from fastapi import FastAPI

app = FastAPI(title="InfraTrack API")

@app.get("/")
def read_root():
    return {"message": "InfraTrack backend running"}