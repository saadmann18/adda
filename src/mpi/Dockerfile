FROM continuumio/anaconda3
WORKDIR /usr/app/
EXPOSE 5000
ENV FLASK_APP=flasgger_imp.py
COPY . /usr/app/
RUN pip install -r requirements.txt
ENTRYPOINT [ "flask" ]
CMD ["run", "--host", "0.0.0.0"]

#compile:
#docker build . -t deploy_flask_api
#run:
#docker run -p 5000:5000 -t -i deploy_flask_api:latest
#check website
#http://0.0.0.0:5000/apidocs/