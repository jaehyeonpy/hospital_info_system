from django.db import models 


# the longest data length in the fixture is 91 characters,
# so, the max_length value is set to 95, with an additional 4 characters that I added arbitrarily.
# additionally, note that this application does not assume any extension of its functionality,
# and charfield is converted to varchar in mysql,
# which means it is acceptable even if more characters are added arbitrarily. 
#
# For the fields doctor.major, doctor.school, and hospital.director, it is okay to temporarily set them as null
# before assigning values to major, school, and director, respectively.
#
# The fields hospital.phone, hospital.url, hospital.eup_myeon_dong_name, and hospital.established_at can also be set as null
# based on the provided fixture data.
#
# you can find more details about the fixture data here:
# https://www.data.go.kr/data/15001698/openapi.do#/layer-api-guide


MAX_LENGTH = 95


class Major(models.Model):
    id = models.PositiveSmallIntegerField(primary_key=True)
    name = models.CharField(max_length=MAX_LENGTH)
    
class School(models.Model):
    id = models.PositiveSmallIntegerField(primary_key=True)
    name = models.CharField(max_length=MAX_LENGTH)

class Doctor(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=MAX_LENGTH)
    major = models.ForeignKey(
        Major, 
        on_delete=models.DO_NOTHING,
        null=True
    )
    school = models.ForeignKey(
        School, 
        on_delete=models.DO_NOTHING,
        null=True
    )

class Hospital(models.Model): 
    hospital_id = models.CharField(
        max_length=MAX_LENGTH, 
        primary_key=True
    )
    hospital_name = models.CharField(max_length=MAX_LENGTH)
    class_code = models.PositiveSmallIntegerField()
    class_code_name = models.CharField(max_length=MAX_LENGTH)
    phone = models.CharField(
        max_length=MAX_LENGTH, 
        null=True
    )
    url = models.CharField(
        max_length=MAX_LENGTH, 
        null=True
    )


    # the following adheres to the administrative division system of south korea.

    sigungu_name = models.CharField(max_length=MAX_LENGTH)
    sido_name = models.CharField(max_length=MAX_LENGTH)
    eup_myeon_dong_name = models.CharField(
        max_length=MAX_LENGTH,
        null=True
    )
    full_address = models.CharField(max_length=MAX_LENGTH)
    sigungu_num = models.IntegerField()
    sido_num = models.IntegerField()
    post_num = models.IntegerField()
    

    general_doctor_count = models.IntegerField()
    intern_count = models.IntegerField()
    resident_count = models.IntegerField()
    fellow_doctor_count = models.IntegerField()
    established_at = models.DateField(null=True)
    director = models.ForeignKey(
        Doctor, 
        on_delete=models.CASCADE,
        null=True
    )