from fastapi import FastAPI , File, UploadFile
from fastapi.responses import HTMLResponse
from pydantic import BaseModel

# app


class FileRequest(BaseModel):
    file : bytes = File()

app = FastAPI()

# * the file can be large so we need to put the function async

@app.get("/")
async def main():
    content = """
<body>
<form action="/uploadfile/" enctype="multipart/form-data" method="post">
<input name="files" type="file" multiple>
<input type="submit">
</form>
<form action="/uploadfiles/" enctype="multipart/form-data" method="post">
<input name="files" type="file" multiple>
<input type="submit">
</form>
</body>
    """
    return HTMLResponse(content=content)

# convert the file to bytes
@app.post('/file')
async def file(request : FileRequest):
    return {
        "file" : request
    }

@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile):
    return {"filename": file.filename , "content_type" : file.content_type}


# multiple file
@app.post("/uploadfiles/")
async def create_upload_files(files: list[UploadFile]):
    return {"filenames": [file.filename for file in files]}