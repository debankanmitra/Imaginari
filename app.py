from api.routes import app
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

# origins = [
#     "http://localhost.tiangolo.com",
#     "https://localhost.tiangolo.com",
#     "http://localhost:3000",
#     "http://localhost:8080",
#     "http://localhost:5173"
# ]


# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["http://localhost:5173"],
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# When a Python file is run directly as a script, the special variable __name__ is set to "__main__" within that script. 
# This allows you to determine whether the script is being run as the main program or if it is being imported as a module
# into another program.

# By placing this code inside the if __name__ == "__main__": block, it ensures that the FastAPI application 
# is only run when the script is executed directly

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000,reload=True)