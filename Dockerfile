# Base image
FROM --platform=linux/amd64 ubuntu:22.04

# Labels and Credits
LABEL \
    name="bnmc" \
    description="bnmc is a automated pipeline of recon process, useful for information gathering during web application penetration testing."

# Environment Variables
ENV DEBIAN_FRONTEND="noninteractive" \
    DATABASE="postgres"
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV GOROOT="/usr/local/go"
ENV GOPATH=$HOME/go
ENV PATH="${PATH}:${GOROOT}/bin:${GOPATH}/bin"

# Install Python
RUN apt update -y && \
    apt update -y && \
    apt install -y \
    python3.10 \
    python3-dev \
    python3-pip

# Install essential packages
RUN apt install -y  --no-install-recommends \
    build-essential \
    cmake \
    geoip-bin \
    geoip-database \
    gcc \
    git \
    libpq-dev \
    libpango-1.0-0 \
    libpangoft2-1.0-0 \
    libpcap-dev \
    netcat \
    nmap \
    x11-utils \
    xvfb \
    wget \
    curl \
    python3-netaddr \
    software-properties-common

RUN add-apt-repository ppa:mozillateam/ppa

# Download and install go 1.20
RUN wget https://golang.org/dl/go1.21.4.linux-amd64.tar.gz
RUN tar -xvf go1.21.4.linux-amd64.tar.gz
RUN rm go1.21.4.linux-amd64.tar.gz
RUN mv go /usr/local

# Download geckodriver
RUN wget https://github.com/mozilla/geckodriver/releases/download/v0.32.0/geckodriver-v0.32.0-linux64.tar.gz
RUN tar -xvf geckodriver-v0.32.0-linux64.tar.gz
RUN rm geckodriver-v0.32.0-linux64.tar.gz
RUN mv geckodriver /usr/bin

# Make directory for app
WORKDIR /usr/src/app

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Copy requirements
COPY ./requirements.txt /tmp/requirements-dev.txt
RUN pip3 install --upgrade setuptools pip && \
    pip3 install -r /tmp/requirements-dev.txt

# Copy source code
COPY . /usr/src/app/
