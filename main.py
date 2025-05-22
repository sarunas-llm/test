from datetime import datetime, timezone
from fastapi import FastAPI


async def get_current_time() -> dict[str, str]:
    """Return the current UTC time in ISO format."""
    return {"time": datetime.now(tz=timezone.utc).isoformat()}


def create_app() -> FastAPI:
    app = FastAPI()

    app.add_api_route("/time", get_current_time, methods=["GET"])

    return app


app = create_app()


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
