FROM ubuntu

RUN apt-get update
RUN apt-get -y install python3
RUN apt -y install python3-pip
RUN pip3 install numpy

COPY my_csv_reader_PK.py .
COPY wine.data .

CMD ["python3","-u","my_csv_reader_PK.py"]
