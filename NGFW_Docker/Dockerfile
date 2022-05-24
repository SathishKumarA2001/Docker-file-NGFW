FROM ubuntu

RUN apt-get -y update && apt-get -y upgrade
RUN apt-get install python3 pip -y
RUN pip install requests 
RUN apt-get -y install apache2
RUN apt-get -y install net-tools apt-utils
ENV DEBIAN_FRONTEND=noninteractive
WORKDIR /root/

VOLUME ["/var/www/","/etc/apache2", "/root/"]

#COPY ./NGFW-with-VPN-Filteration /root/server/
#COPY ./script /root/
#COPY ./html /var/www/html
CMD /root/script/entry.sh

EXPOSE 9999
