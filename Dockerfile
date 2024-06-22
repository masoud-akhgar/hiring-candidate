FROM python:3.11.3

ADD requirements.txt /
RUN pip install -r /requirements.txt

ADD BankClassifier.py /
ADD readme.txt /

ENV PYTHONUNBUFFERED=1
ENTRYPOINT [ "python", "./BankClassifier.py" ]
