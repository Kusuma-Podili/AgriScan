"""
AgriScan Platform Entry Point.
Direct executable script that launches the FastAPI decision platform and web dashboard.
"""
import os
import sys

# Add backend directory to module search path
backend_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "backend")
if backend_dir not in sys.path:
    sys.path.insert(0, backend_dir)

import uvicorn
from app.main import app  # noqa: E402


def main() -> None:
    port = int(os.environ.get("PORT", 8000))
    host = os.environ.get("HOST", "0.0.0.0")
    print(f"AgriScan Precision Agriculture Platform starting on http://{host}:{port}")
    uvicorn.run(app, host=host, port=port)


if __name__ == "__main__":
    main()
