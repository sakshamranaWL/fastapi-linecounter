from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.responses import JSONResponse

app = FastAPI()

@app.post("/count-lines/")
async def count_lines(file: UploadFile = File(...)):
    if not file.filename.endswith(".txt"):
        raise HTTPException(status_code=400, detail="Only file with .txt extension are allowed")
    
    content = await file.read()
    lines = content.decode("utf-8").splitlines()
    return JSONResponse(content={"line_count": len(lines)})
