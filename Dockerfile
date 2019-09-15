FROM python:3.7-slim
WORKDIR /api
ADD . /api
RUN pip install -r requirements.txt
EXPOSE 5000
ENTRYPOINT ["python"]
CMD ["controller.py"]