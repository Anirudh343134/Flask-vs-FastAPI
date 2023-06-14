FROM python:3.7

RUN pip3 install fastapi uvicorn
RUN pip3 install jinja2
RUN pip3 install python-multipart

COPY . .

CMD ["uvicorn", "main:app", "--host", "0.0.0.0"]