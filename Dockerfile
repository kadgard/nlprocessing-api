# Dockerfile - this is a comment. Delete me if you want.
FROM python:3.7-slim
WORKDIR /api
ADD . /api
RUN pip install flask
EXPOSE 5000
ENTRYPOINT ["python"]
CMD ["controller.py"]