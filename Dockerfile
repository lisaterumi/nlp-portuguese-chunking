FROM python:3.6-slim

COPY . /app
WORKDIR /app

RUN pip install --upgrade pip

RUN pip install -U spacy

RUN python -m spacy download pt_core_news_md

CMD ["/bin/bash"]

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000
CMD python ./app.py