FROM python:3.7.3
LABEL maintainer="Robert Knight <dataknight@zohomail.com>"
WORKDIR /app
RUN apt-get update && apt-get install -y python3-pip
COPY requirements.txt .
RUN pip3 install -r requirements.txt && \
    pip3 install jupyter
EXPOSE 8888
VOLUME /app
CMD ["jupyter", "notebook", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--allow-root"]