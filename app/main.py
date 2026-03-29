#app/main.py
from dotenv import load_dotenv
load_dotenv()
from app.mcp_server import mcp
import os

giton_url = os.getenv("giton_url")

if __name__ == "__main__":
    if not giton_url:
        print("Error: 'giton_url' is not set in the environment variables. Exiting...")
        exit(1)
    mcp.run(transport="sse", host="0.0.0.0", port=8000)