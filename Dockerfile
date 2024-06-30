FROM python:3.10
 
WORKDIR /books-project
 
COPY . /books-project
RUN pip install --no-cache-dir --upgrade -r  /books-project/requirements.txt
RUN apt-get update && ACCEPT_EULA=Y apt-get install -y tesseract-ocr && apt clean
 
CMD ["uvicorn", "app.main:app", "--proxy-headers", "--host", "0.0.0.0", "--port", "8000"]