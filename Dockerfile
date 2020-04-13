FROM python:3.7

WORKDIR /app

RUN pip install pandas numpy pathlib scikit-learn flask gunicorn

ADD ./src ./src
ADD ./models ./models
ADD main.py main.py

EXPOSE 5001

CMD [ "gunicorn", "--bind", "0.0.0.0:5001", "main:app" ]