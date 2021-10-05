FROM continuumio/anaconda3:4.4.0
COPY . /usr/app/smt
EXPOSE 8000
WORKDIR /usr/app/smt
RUN pip install -r requirements.txt
CMD python frontend_flasgger.py