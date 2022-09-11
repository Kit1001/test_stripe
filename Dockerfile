FROM ubuntu

WORKDIR /root/test_stripe

COPY . .

EXPOSE 80/tcp

ENV DJANGO_PRODUCTION=1

RUN apt-get update
RUN apt-get install python3-dev pip nginx -y
RUN pip install -r requirements.txt
RUN apt-get install gunicorn -y
RUN python3 manage.py migrate
RUN python3 manage.py loaddata data
RUN python3 manage.py collectstatic
RUN rm /etc/nginx/nginx.conf
RUN cp ./nginx.conf /etc/nginx/nginx.conf
RUN chmod +x ./start.sh

CMD ["./start.sh"]