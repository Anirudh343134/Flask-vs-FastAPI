FROM ubuntu

RUN apt update 
RUN apt install python3-pip -y
RUN pip3 install Flask  

WORKDIR /Flask_Microservice_1

COPY . .

CMD ["python3", "-m", "flask", "--app", "main", "run", "--host=0.0.0.0"]