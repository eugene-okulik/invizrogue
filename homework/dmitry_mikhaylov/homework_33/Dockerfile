FROM jenkins/jenkins:lts-jdk17

USER root
COPY requirements.txt /
RUN apt-get update && apt-get install -y python3 python3-pip python3-venv \
    && python3 -m venv /venv
RUN /venv/bin/pip install -r requirements.txt && /venv/bin/playwright install-deps && /venv/bin/playwright install

USER jenkins