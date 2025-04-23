FROM libretranslate/libretranslate:latest

ENV LT_LOAD_ONLY=en,de,th,fr,ko,ja,es,it

EXPOSE 5000

CMD ["libretranslate"]
#FROM python:3.10-slim

#WORKDIR /app

#COPY . /app

#RUN pip install flask requests gunicorn

#EXPOSE 8080

#CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:8080", "app:app"]
