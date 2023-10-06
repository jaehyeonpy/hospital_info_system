ARG BASE_IMAGE
FROM ${BASE_IMAGE}

COPY hospital_info_applyer hospital_info_system/hospital_info_applyer
COPY hospital_info_system hospital_info_system/hospital_info_system
COPY requirements.txt hospital_info_system/requirements.txt
COPY manage.py hospital_info_system/manage.py
RUN cd hospital_info_system && pip install -r requirements.txt