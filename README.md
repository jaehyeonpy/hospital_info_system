## Description

<img src='hosp-info-sys-desc.png'></img>

This project runs a WAS for registering information about hospital, doctor, major, school, and returning them corresponding to received HTTP request.

<br>

Note that the project does not supoort HTTPS.

Make sure to hide mysql_setting.yaml, secret_key.yaml to a safe place, modify settings.py to load these from the place.

<br>

The project is based on django rest framework.

The hospital information is from [this open api](https://www.data.go.kr/data/15001698/openapi.do#/layer-api-guide).


<br>

## Give it a try!

make the proejct containers by:

```
docker-compose up
```


<br>

wait about 30 seconds for mysql and the WAS to startup, run test or insert fixture to the WAS by:

```
(for test) cd hospital_info_system && python manage.py test hospital_info_applyer


(for inserting fixture to the WAS) 

cd hospital_info_system 

python manage.py loaddata hospital_info_applyer/fixtures/all_hospital_info.jsonl

nohup python manage.py runserver 0.0.0.0:8000 &
```

note that other fixtures are ready in hospital_info_applyer/fixtures, too.


<br>

the result are like the below, in the case of inserting fixture to the WAS:

```
curl -XGET http://127.0.0.1:8000/hospital/JDQ4MTYyMiM1MSMkMSMkMCMkODkkMzgxMzUxIzExIyQxIyQzIyQ3OSQyNjE4MzIjNDEjJDEjJDgjJDgz/ | jq    

  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100   589  100   589    0     0  30329      0 --:--:-- --:--:-- --:--:-- 31000
{
  "hospital_id": "JDQ4MTYyMiM1MSMkMSMkMCMkODkkMzgxMzUxIzExIyQxIyQzIyQ3OSQyNjE4MzIjNDEjJDEjJDgjJDgz",
  "hospital_name": "가톨릭대학교인천성모병원",
  "class_code": 1,
  "class_code_name": "상급종합",
  "phone": "032-1544-9004",
  "url": null,
  "sigungu_name": "인천부평구",
  "sido_name": "인천",
  "eup_myeon_dong_name": "부평동",
  "full_address": "인천광역시 부평구 동수로 56, (부평동)",
  "sigungu_num": 220003,
  "sido_num": 220000,
  "post_num": 21431,
  "general_doctor_count": 1,
  "intern_count": 0,
  "resident_count": 0,
  "fellow_doctor_count": 2,
  "established_at": "1981-08-06T00:00:00",
  "director": null
}
```

try other HTTP methods, other fixtures, too!


<br>

## License

MIT