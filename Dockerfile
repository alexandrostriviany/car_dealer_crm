FROM python:3.8

RUN pip3 install pipenv

ENV PROJECT_DIR /usr/src/car_dealer_crm
ENV DEALER_CENTER_CRM_DB_NAME dealerCenterCrm.db
ENV DEALER_CENTER_TABLE_NAME dealerCenter
ENV CAR_TABLE_NAME car

WORKDIR ${PROJECT_DIR}

COPY Pipfile .
COPY Pipfile.lock .
COPY . .

RUN pipenv install --deploy --ignore-pipfile

EXPOSE 5000

CMD ["pipenv", "run", "python", "app.py"]