FROM ubuntu

RUN apt-get -y update && apt-get -y upgrade
RUN apt-get install python3 pip -y
RUN pip install requests 
RUN apt-get -y install apache2
RUN apt-get -y install net-tools apt-utils
ENV DEBIAN_FRONTEND=noninteractive
WORKDIR /root
RUN rm /var/www/html -rf
VOLUME ["/var/www/","/etc/apache2", "/root/"]

COPY ./NGFW-code/ /root/
COPY ./script /root/script/
COPY ./html /var/www/html
CMD /root/script/entry.sh


EXPOSE 9999
