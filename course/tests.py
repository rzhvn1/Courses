from django.test import TestCase
from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase
from .models import Category, Course, Branch, Contact
# Create your tests here.

class CategoryModelTest(TestCase):

    def setUp(self):
        self.category = Category.objects.create(name='Language', img_path='language/')

    def test_str_method(self):
        self.assertEqual(self.category.__str__(), self.category.name)


class CourseModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        branch = Branch.objects.create(latitude="12", longtitude='21', address='Neobis')
        contact = Contact.objects.create(type=3, value='english@example.com')
        category = Category.objects.create(name='Language', img_path='language/')
        course = Course.objects.create(name="English", description='Best', category=category, logo='enLogo/')
        cls.course = Course.objects.get(id=1)


    def test_name_label(self):
        field_label = self.course._meta.get_field('name').verbose_name
        self.assertEqual(field_label, 'name')

    def test_description_label(self):
        field_label = self.course._meta.get_field('description').verbose_name
        self.assertEqual(field_label, 'description')

    def test_logo_label(self):

        field_label = self.course._meta.get_field('logo').verbose_name
        self.assertEqual(field_label, 'logo')

    def test_name_max_length(self):
        max_length = self.course._meta.get_field('name').max_length
        self.assertEqual(max_length, 255)

    def test_str_method(self):
        self.assertEqual(self.course.__str__(), self.course.name)

    def test_is_instance_course(self):
        self.assertTrue(isinstance(self.course, Course))

    def test_is_instance_category(self):
        self.assertTrue(isinstance(self.course.category, Category))



class TestCourseView(APITestCase):

    def setUp(self):
        self.course_url = reverse('courses')

    def test_courses_get(self):
        self.response = self.client.get(self.course_url)
        self.assertEqual(self.response.status_code, status.HTTP_200_OK)

    def test_courses_post(self):
        data =         {
            "name":
                "Spanish"
            ,
            "description":
                "Course for beginners"
            ,
            "category":
                {
                    "name":"Language",
                    "img_path":"language/"
                }
            ,
            "logo":
                "SpainFlag"
            ,
            "contact": [
                {
                "type":3,
                "value":"spanish-course@example.com"
                }
            ]
            ,
            "branch": [
                {
                "latitude":"40.4637° N",
                "longtitude":"3.7492° W",
                "address":"Spain"
                }
            ]
        }
        self.response = self.client.post(self.course_url, data, format='json')
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

    #test courses post without category (NOTE: you can't create course withou category)
    def test_courses_post_without_category(self):
        data = {
            "name":
                "Spanish"
            ,
            "description":
                "Course for beginners"
            ,
            "logo":
                "SpainFlag"
            ,
            "contact": [
                {
                    "type": 3,
                    "value": "spanish-course@example.com"
                }
            ]
            ,
            "branch": [
                {
                    "latitude": "40.4637° N",
                    "longtitude": "3.7492° W",
                    "address": "Spain"
                }
            ]
        }
        self.response = self.client.post(self.course_url, data, format='json')
        self.assertNotEqual(self.response.status_code, status.HTTP_201_CREATED)

    #test courses post without branch (NOTE: you can't create course without branch)
    def test_courses_post_without_branch(self):
        data = {
            "name":
                "Spanish"
            ,
            "description":
                "Course for beginners"
            ,
            "category":
                {
                    "name": "Language",
                    "img_path": "language/"
                }
            ,
            "logo":
                "SpainFlag"
            ,
            "contact": [
                {
                    "type": 3,
                    "value": "spanish-course@example.com"
                }
            ]
        }
        self.response = self.client.post(self.course_url, data, format='json')
        self.assertNotEqual(self.response.status_code, status.HTTP_201_CREATED)

    # test courses post without contact (NOTE: you can't create course without contact)
    def test_courses_post_without_contact(self):
        data = {
            "name":
                "Spanish"
            ,
            "description":
                "Course for beginners"
            ,
            "category":
                {
                    "name": "Language",
                    "img_path": "language/"
                }
            ,
            "logo":
                "SpainFlag"
            ,
            "branch": [
                {
                    "latitude": "40.4637° N",
                    "longtitude": "3.7492° W",
                    "address": "Spain"
                }
            ]

        }
        self.response = self.client.post(self.course_url, data, format='json')
        self.assertNotEqual(self.response.status_code, status.HTTP_201_CREATED)

    def test_courses_post_without_category_and_branch(self):
        data = {
            "name":
                "Spanish"
            ,
            "description":
                "Course for beginners"
            ,
            "logo":
                "SpainFlag"
            ,
            "contact": [
                {
                    "type": 3,
                    "value": "spanish-course@example.com"
                }
            ]
        }
        self.response = self.client.post(self.course_url, data, format='json')
        self.assertNotEqual(self.response.status_code, status.HTTP_201_CREATED)

    def test_courses_post_without_category_and_contact(self):
        data = {
            "name":
                "Spanish"
            ,
            "description":
                "Course for beginners"
            ,
            "logo":
                "SpainFlag"
            ,
            "branch": [
                {
                    "latitude": "40.4637° N",
                    "longtitude": "3.7492° W",
                    "address": "Spain"
                }
            ]

        }
        self.response = self.client.post(self.course_url, data, format='json')
        self.assertNotEqual(self.response.status_code, status.HTTP_201_CREATED)

    def test_courses_post_without_branch_and_contact(self):
        data = {
            "name":
                "Spanish"
            ,
            "description":
                "Course for beginners"
            ,
            "category":
                {
                    "name": "Language",
                    "img_path": "language/"
                }
            ,
            "logo":
                "SpainFlag"
        }
        self.response = self.client.post(self.course_url, data, format='json')
        self.assertNotEqual(self.response.status_code, status.HTTP_201_CREATED)

    def test_courses_post_without_branch_contact_and_category(self):
        data = {
            "name":
                "Spanish"
            ,
            "description":
                "Course for beginners"
            ,
            "logo":
                "SpainFlag"
        }
        self.response = self.client.post(self.course_url, data, format='json')
        self.assertNotEqual(self.response.status_code, status.HTTP_201_CREATED)

class TestCourseDetailView(APITestCase):

    def create_course(self):
        course = Course.objects.create(name='English',
                                            description='Best',
                                            logo='englishLogo')
        return course

    def test_course_get(self):
        course_data = self.create_course()
        print(course_data.id)
        self.response = self.client.get(reverse('course', kwargs={'course_id':course_data.id}))
        self.assertEqual(self.response.status_code, status.HTTP_200_OK)

    def test_course_get_if_does_not_exist(self):
        self.response = self.client.get(reverse('course', kwargs={'course_id': 1}))
        self.assertEqual(self.response.status_code, status.HTTP_404_NOT_FOUND)

    def test_course_delete(self):
        course_data = self.create_course()
        self.response = self.client.delete(reverse('course', kwargs={'course_id':course_data.id}))
        self.assertEqual(self.response.status_code, status.HTTP_200_OK)

    def test_course_delete_if_does_not_exist(self):
        self.response = self.client.delete(reverse('course', kwargs={'course_id': 1}))
        self.assertEqual(self.response.status_code, status.HTTP_404_NOT_FOUND)








