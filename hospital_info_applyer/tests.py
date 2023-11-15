from rest_framework.test import APIClient, APITestCase


class HospitalInfoApplyerTest(APITestCase):
    fixtures = [
        'doctor.json',
        'major.json',
        'school.json',
        'part_of_hospital_info.jsonl'
    ]

    def setUp(self):
        self.client = APIClient()
        self.url = 'http://127.0.0.1:{port}/{model}/{resource}'
        self.port = 8000
        self.format = 'json'

    def test_get(self):
        one_major_get_response = self.client.get(
            path=self.url.format(
                port=self.port,
                model='major',
                resource='1/'
            )
        )
        one_school_get_response = self.client.get(
            path=self.url.format(
                port=self.port,
                model='school',
                resource='1/'
            )
        )
        one_doctor_get_response = self.client.get(
            path=self.url.format(
                port=self.port,
                model='doctor',
                resource='1/'
            )
        )
        one_hospital_get_response = self.client.get(
            path=self.url.format(
                port=self.port,
                model='hospital',
                resource='JDQ4MTYyMiM1MSMkMSMkMCMkODkkMzgxMzUxIzExIyQxIyQzIyQ3OSQyNjE4MzIjNDEjJDEjJDgjJDgz/'
            )
        )

        all_major_get_response = self.client.get(
            path=self.url.format(
                port=self.port,
                model='major',
                resource=''
            )
        )
        all_school_get_response = self.client.get(
            path=self.url.format(
                port=self.port,
                model='school',
                resource=''
            )
        )
        all_doctor_get_response = self.client.get(
            path=self.url.format(
                port=self.port,
                model='doctor',
                resource=''
            )
        )
        all_hospital_get_response = self.client.get(
            path=self.url.format(
                port=self.port,
                model='hospital',
                resource=''
            )
        )

        self.assertEqual(one_major_get_response.status_code, 200)
        self.assertEqual(one_school_get_response.status_code, 200)
        self.assertEqual(one_doctor_get_response.status_code, 200)
        self.assertEqual(one_hospital_get_response.status_code, 200)

        self.assertEqual(all_major_get_response.status_code, 200)
        self.assertEqual(all_school_get_response.status_code, 200)
        self.assertEqual(all_doctor_get_response.status_code, 200)
        self.assertEqual(all_hospital_get_response.status_code, 200)

    def test_delete(self):
        one_major_delete_response = self.client.delete(
            path=self.url.format(
                port=self.port,
                model='major',
                resource='2/'
            )
        )
        one_school_delete_response = self.client.delete(
            path=self.url.format(
                port=self.port,
                model='school',
                resource='2/'
            )
        )
        one_doctor_delete_response = self.client.delete(
            path=self.url.format(
                port=self.port,
                model='doctor',
                resource='2/'
            )
        )
        one_hospital_delete_response = self.client.delete(
            path=self.url.format(
                port=self.port,
                model='hospital',
                resource='JDQ4MTYyMiM1MSMkMSMkNCMkODkkMzgxMzUxIzExIyQxIyQzIyQ4OSQ0NjEwMDIjNDEjJDEjJDgjJDgz/'
            )
        )

        self.assertEqual(one_major_delete_response.status_code, 204)
        self.assertEqual(one_school_delete_response.status_code, 204)
        self.assertEqual(one_doctor_delete_response.status_code, 204)
        self.assertEqual(one_hospital_delete_response.status_code, 204)
        
    def test_patch(self):
        one_major_patch_response = self.client.patch(
            path=self.url.format(
                port=self.port,
                model='major',
                resource='3/'
            ),
            data={"major": "dental hygentist"},
            format=self.format
        )
        one_school_patch_response = self.client.patch(
            path=self.url.format(
                port=self.port,
                model='school',
                resource='3/'
            ),
            data={"school": "cau"},
            format=self.format
        )
        one_doctor_patch_response = self.client.patch(
            path=self.url.format(
                port=self.port,
                model='doctor',
                resource='3/'
            ),
            data={"name": "jeong", "major": 3, "school": 3},
            format=self.format
        )
        one_hospital_patch_response = self.client.patch(
            path=self.url.format(
                port=self.port,
                model='hospital',
                resource='JDQ4MTg4MSM1MSMkMSMkMCMkODkkMzgxMzUxIzExIyQxIyQzIyQ3OSQ0NjEwMDIjNjEjJDEjJDQjJDgz/'
            ),
            data={"fellow_doctor_count": 10000, "doctor": 3},
            format=self.format
        )

        self.assertEqual(one_major_patch_response.status_code, 200)
        self.assertEqual(one_school_patch_response.status_code, 200)
        self.assertEqual(one_doctor_patch_response.status_code, 200)
        self.assertEqual(one_hospital_patch_response.status_code, 200)

    def test_post(self):
        major_post_response = self.client.post(
            path=self.url.format(
                port=self.port,
                model='major',
                resource=''
            ),
            data={"id": "4", "name": "orthodontist"},
            format=self.format
        )
        school_post_response = self.client.post(
            path=self.url.format(
                port=self.port,
                model='school',
                resource=''
            ),
            data={"id": "4", "name": "sogang"},
            format=self.format
        )
        doctor_post_response = self.client.post(
            path=self.url.format(
                port=self.port,
                model='doctor',
                resource=''
            ),
            data={"id": "4", "name": "choi"},
            format=self.format
        )
        hospital_post_response = self.client.post(
            path=self.url.format(
                port=self.port,
                model='hospital',
                resource=''
            ),
            data={
                "hospital_id": "JDQ4MTg4MSM1MSMkMSMkMCMkODkkMzgxMzUxIzExIyQxIyQzIyQ2MiQyNjE4MzIjNjEjJDEjJDQjJDgz",
                "hospital_name": "\uac74\uad6d\ub300\ud559\uad50\ubcd1\uc6d0", 
                "class_code": 1, 
                "class_code_name": "\uc0c1\uae09\uc885\ud569", 
                "phone": "1588-1533", 
                "url": None, 
                "established_at": "1982-11-16", 
                "sigungu_name": "\uad11\uc9c4\uad6c", 
                "eup_myeon_dong_name": None, 
                "post_num": 5030, 
                "full_address": "\uc11c\uc6b8\ud2b9\ubcc4\uc2dc \uad11\uc9c4\uad6c \ub2a5\ub3d9\ub85c 120-1, (\ud654\uc591\ub3d9)", 
                "sido_name": "\uc11c\uc6b8", 
                "sigungu_num": 110023, 
                "sido_num": 110000, 
                "general_doctor_count": 0, 
                "intern_count": 0, 
                "resident_count": 0, 
                "fellow_doctor_count": 3
            },
            format=self.format
        )

        self.assertEqual(major_post_response.status_code, 201)
        self.assertEqual(school_post_response.status_code, 201)
        self.assertEqual(doctor_post_response.status_code, 201)
        self.assertEqual(hospital_post_response.status_code, 201)