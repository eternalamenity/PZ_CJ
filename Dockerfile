from debian:latest

RUN apt-get update -y
RUN apt-get upgrade -y

#RUN apt-get install -y jupyter-notebook

RUN apt-get install -y python3-dev python3-pip

RUN pip3 install --upgrade pip
RUN pip3 install --upgrade setuptools

RUN pip3 install jupyter

RUN apt-get install -y sudo

RUN pip3 install matplotlib tensorflow sklearn

RUN useradd marcinek
RUN su marcinek

#RUN mkdir /var/jupyter
#RUN cd /var/jupyter

RUN mkdir /home/marcinek
RUN chmod 777 /home/marcinek
RUN mkdir /home/marcinek/.jupyter

RUN chown -R marcinek /home/marcinek

RUN cd /home/marcinek


EXPOSE 8888
CMD ["sudo", "-u", "marcinek", "jupyter", "notebook", "--port=8888", "--no-browser", "--ip=0.0.0.0", "--allow-root"]
