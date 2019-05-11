Step 1:
	Create the directory where you want to have all the relecent files.
	in this case, ~/class4-homework/

Step 2:
	Create or use existing Python script.
	In our example is the my_csv_reader_PK.py

Step 3:
	Create a Dockerfile by typing the following: "nano Dockerfile"
	In the Dockerfile, write the the commands to create the image.
	
"
#what OS to use.
FROM ubuntu

#run update, install python3, pithon3-pip and numpy.
RUN apt-get update
RUN apt-get -y install python3
RUN apt -y install python3-pip
RUN pip3 install numpy



#include the python3 script and the data to process.
COPY my_csv_reader_PK.py .
COPY wine.data .

#execute the python script.
CMD ["python3","-u","my_csv_reader_PK.py"]
"

Step 4:
	Build the image by running the following command:
	sudo docker build -t class4-hmrk-container .

Step 5:
	Run the image to create the container with the following command:
	sudo docker run class4-hmrk-container
