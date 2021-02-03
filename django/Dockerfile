FROM python:3.7-buster

#change working directory
WORKDIR /usr/src/django

# set env variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# copy requirements
COPY ./requirements.txt /usr/src/django/requirements.txt

# netcdf4 libraries
RUN apt-get update && apt-get install -y libhdf5-serial-dev netcdf-bin libnetcdf-dev tree
# install required packages
RUN pip install -r requirements.txt

# copy entrypoint.sh
COPY ./entrypoint.sh /usr/src/django/entrypoint.sh

# copy project
COPY . /usr/src/django/

# run entrypoint.sh
ENTRYPOINT ["/usr/src/django/entrypoint.sh"]

# for security reasons the user that will run
# our software will be user and not root
# RUN adduser --disabled-login --gecos "" user
# USER user