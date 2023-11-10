FROM python:3.11
COPY . .
RUN pip install --no-cache-dir --prefer-binary django waitress whitenoise pygsheets aiogram
CMD [ "python", "index.py" ]
