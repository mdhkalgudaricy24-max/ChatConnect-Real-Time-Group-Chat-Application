import traceback

try:
    from app_real import app
except Exception:
    from fastapi import FastAPI
    from fastapi.responses import PlainTextResponse

    err = traceback.format_exc()
    app = FastAPI()

    @app.get("/{path:path}")
    def show_error(path: str):
        return PlainTextResponse(err[-3000:])
