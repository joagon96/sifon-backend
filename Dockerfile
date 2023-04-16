FROM python:3.7
WORKDIR /vgn-sifon-backend
COPY . .
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["run.py"]