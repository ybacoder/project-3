# FastAPI Deployment
# https://fastapi.tiangolo.com/deployment/
FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7

COPY ./app /app

# Install production dependencies
RUN pip install "fastapi==0.54.1" "aiofiles==0.5.0" "uvicorn==0.11.5" "pandas==1.0.3" "scikit-learn==0.22.2.post1" "ipykernel==5.2.1" "imbalanced-learn==0.6.2" "gunicorn==20.0.4" "jinja2==3.0.0a1" "python-multipart==0.0.5" "httptools==0.1.1" "uvloop==0.14.0"