import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn.config
import uvicorn.server
import signal
import sys

# List of allowed origins for CORS
origins = [
    '*',
]

# Create the FastAPI app instance
app = FastAPI()

# Include the saved_items router
# webapp.include_router(saved_items.router)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

# Define a new GET route that returns "Hello, World!"
@app.get("/")
async def read_root():
    return {"message": "Hello, World!"}

def serve():
    """Serve the web application."""
    uvicorn.run(app, host="0.0.0.0", port=8000)

if __name__ == "__main__":
    serve()
