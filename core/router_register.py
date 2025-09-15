from fastapi import APIRouter

def include_routers(app):
    # Import and include your routers here
    from routers import service, auth, slider
    app.include_router(auth.router)
    app.include_router(slider.router)
    app.include_router(service.router)