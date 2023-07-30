FROM python:3.7
WORKDIR /vgn-sifon-backend
COPY . .
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
EXPOSE 5000
CMD ["run.py"]