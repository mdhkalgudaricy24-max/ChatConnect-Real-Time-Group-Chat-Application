import traceback
from fastapi import FastAPI
from fastapi.responses import PlainTextResponse

app = FastAPI()

try:
    import app_real
    app = app_real.app
except Exception:
    err = traceback.format_exc()

    @app.get("/{path:path}")
    def show_error(path: str):
        return PlainTextResponse(err[-3000:])
        
