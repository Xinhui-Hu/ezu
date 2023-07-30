# from django.test import TestCase
# from .models import Semester, Section, Course, Instructor, Student, Registration, Period, Year
# from django.contrib.auth import get_user_model
# from django.urls import reverse
#
# # Create your tests here.
#
#
# class CourseTests(TestCase):
#
#     @classmethod
#     def setUpTestData(cls):
#         cls.user = get_user_model().objects.create_user(
#             username="tester”", password="{iSchoolUI}"
#         )
#
#         cls.period = Period.objects.create(
#             period_sequence="9",
#             period_name="TestPeriod",
#         )
#
#         cls.year = Year.objects.create(
#             year="2999",
#         )
#
#         cls.course = Course.objects.create(
#             course_number="TEST599",
#             course_name="Test App Course Name",
#         )
#
#         cls.semester = Semester.objects.create(
#             year=cls.year,
#             period=cls.period,
#         )
#
#         cls.instructor = Instructor.objects.create(
#             first_name="Good First Name",
#             last_name="Good Last Name",
#             disambiguator="Good Disambiguator",
#         )
#
#         cls.student = Student.objects.create(
#             first_name="Good First Name",
#             last_name="Good Last Name",
#             disambiguator="Good Disambiguator",
#         )
#
#         cls.section = Section.objects.create(
#             section_name="Good Section Name",
#             semester=cls.semester,
#             course=cls.course,
#             instructor=cls.instructor,
#
#         )
#
#         cls.registration = Registration.objects.create(
#             student=cls.student,
#             section=cls.section,
#
#         )
#
#     def test_model_content(self):
#
#         self.assertEqual(self.course.course_number, "TEST599")
#         self.assertEqual(self.course.course_name, "Test App Course Name")
#         self.assertEqual(self.period.period_sequence, "9")
#         self.assertEqual(self.period.period_name, "TestPeriod")
#         self.assertEqual(self.instructor.first_name, "Good First Name")
#         self.assertEqual(self.instructor.last_name, "Good Last Name")
#         self.assertEqual(self.instructor.disambiguator, "Good Disambiguator")
#         self.assertEqual(self.student.first_name, "Good First Name")
#         self.assertEqual(self.student.last_name, "Good Last Name")
#         self.assertEqual(self.student.disambiguator, "Good Disambiguator")
#         self.assertEqual(self.section.section_name, "Good Section Name")
#         self.assertEqual(self.year.year, "2999")
#
#     def test_url_exists_at_correct_location_listview(self):  # new
#         response = self.client.get("/instructor/")
#         response = self.client.get("/semester/")
#         response = self.client.get("/section/")
#         response = self.client.get("/student/")
#         response = self.client.get("/course/")
#         response = self.client.get("/registration/")
#         self.assertEqual(response.status_code, 200)
#
#     def test_url_exists_at_correct_location_detailview(self):  # new
#         response = self.client.get("/semester/1/")
#         self.assertEqual(response.status_code, 200)
#         response = self.client.get("/instructor/1/")
#         self.assertEqual(response.status_code, 200)
#         response = self.client.get("/section/1/")
#         self.assertEqual(response.status_code, 200)
#         response = self.client.get("/student/1/")
#         self.assertEqual(response.status_code, 200)
#         response = self.client.get("/course/1/")
#         self.assertEqual(response.status_code, 200)
#         response = self.client.get("/registration/1/")
#         self.assertEqual(response.status_code, 200)
#
#     def test_instructor_listview(self):  # new
#         response = self.client.get(reverse("courseinfo_instructor_list_urlpattern"))
#         self.assertEqual(response.status_code, 200)
#         self.assertTemplateUsed(response, "courseinfo/instructor_list.html")
#
#     def test_section_listview(self):  # new
#         response = self.client.get(reverse("courseinfo_section_list_urlpattern"))
#         self.assertEqual(response.status_code, 200)
#         self.assertTemplateUsed(response, "courseinfo/section_list.html")
#
#     def test_student_listview(self):  # new
#         response = self.client.get(reverse("courseinfo_student_list_urlpattern"))
#         self.assertEqual(response.status_code, 200)
#         self.assertTemplateUsed(response, "courseinfo/student_list.html")
#
#     def test_semester_listview(self):  # new
#         response = self.client.get(reverse("courseinfo_semester_list_urlpattern"))
#         self.assertEqual(response.status_code, 200)
#         self.assertTemplateUsed(response, "courseinfo/semester_list.html")
#
#     def test_registration_listview(self):  # new
#         response = self.client.get(reverse("courseinfo_registration_list_urlpattern"))
#         self.assertTemplateUsed(response, "courseinfo/registration_list.html")
#
#     def test_instructor_detailview(self):  # new
#         response = self.client.get(reverse("courseinfo_instructor_detail_urlpattern",
#                                            kwargs={"pk": self.instructor.pk}))
#         no_response = self.client.get("/post/100000/")
#         self.assertEqual(response.status_code, 200)
#         self.assertEqual(no_response.status_code, 404)
#         self.assertContains(response, "Good Disambiguator")
#         self.assertTemplateUsed(response, "courseinfo/instructor_detail.html")
#
#     def test_section_detailview(self):  # new
#         response = self.client.get(reverse("courseinfo_section_detail_urlpattern",
#                                            kwargs={"pk": self.section.pk}))
#         no_response = self.client.get("/post/100000/")
#         self.assertEqual(response.status_code, 200)
#         self.assertEqual(no_response.status_code, 404)
#         self.assertContains(response, "Good Section Name")
#         self.assertTemplateUsed(response, "courseinfo/section_detail.html")
#
#     def test_student_detailview(self):  # new
#         response = self.client.get(reverse("courseinfo_student_detail_urlpattern",
#                                            kwargs={"pk": self.student.pk}))
#         no_response = self.client.get("/post/100000/")
#         self.assertEqual(response.status_code, 200)
#         self.assertEqual(no_response.status_code, 404)
#         self.assertContains(response, "Good First Name")
#         self.assertTemplateUsed(response, "courseinfo/student_detail.html")
#
#     def test_semester_detailview(self):  # new
#         response = self.client.get(reverse("courseinfo_semester_detail_urlpattern",
#                                            kwargs={"pk": self.semester.pk}))
#         no_response = self.client.get("/post/100000/")
#         self.assertEqual(response.status_code, 200)
#         self.assertEqual(no_response.status_code, 404)
#         self.assertContains(response, "TestPeriod")
#         self.assertTemplateUsed(response, "courseinfo/semester_detail.html")
#
#     def test_course_detailview(self):  # new
#         response = self.client.get(reverse("courseinfo_course_detail_urlpattern",
#                                            kwargs={"pk": self.course.pk}))
#         no_response = self.client.get("/post/100000/")
#         self.assertEqual(response.status_code, 200)
#         self.assertEqual(no_response.status_code, 404)
#         self.assertContains(response, "Test App Course Name")
#         self.assertTemplateUsed(response, "courseinfo/course_detail.html")
#
#     def test_registration_detailview(self):  # new
#         response = self.client.get(reverse("courseinfo_registration_detail_urlpattern",
#                                            kwargs={"pk": self.registration.pk}))
#         no_response = self.client.get("/post/100000/")
#         self.assertEqual(response.status_code, 200)
#         self.assertEqual(no_response.status_code, 404)
#         self.assertContains(response, "Good Section Name")
#         self.assertTemplateUsed(response, "courseinfo/registration_detail.html")
#
#     def test_instructor_create_view(self):  # new
#         response = self.client.post(reverse('courseinfo_instructor_create_urlpattern'), {
#             'first_name': 'New First Name',
#             'disambiguator': "New Disambiguator",
#         })
#
#         self.assertEqual(response.status_code, 200)
#         self.assertContains(response, 'New First Name')
#         self.assertContains(response, 'New Disambiguator')
#
#     def test_course_create_view(self):  # new
#         response = self.client.post(reverse('courseinfo_course_create_urlpattern'), {
#             'course_name': 'New Course Name',
#         })
#
#         self.assertEqual(response.status_code, 200)
#         self.assertContains(response, 'New Course Name')
#
#     def test_section_create_view(self):  # new
#         response = self.client.post(reverse('courseinfo_section_create_urlpattern'), {
#             'section_name': 'New Section Name',
#         })
#
#         self.assertEqual(response.status_code, 200)
#         self.assertContains(response, 'New Section Name')
#
#     def test_semester_create_view(self):  # new
#         response = self.client.post(reverse('courseinfo_semester_create_urlpattern'), {
#             'year': "1999"
#         })
#
#         self.assertEqual(response.status_code, 200)
#
#     def test_student_create_view(self):  # new
#         response = self.client.post(reverse('courseinfo_student_create_urlpattern'), {
#             'first_name': 'New First Name',
#             'disambiguator': "New Disambiguator",
#         })
#
#         self.assertEqual(response.status_code, 200)
#         self.assertContains(response, 'New First Name')
#         self.assertContains(response, 'New Disambiguator')
#
#     def test_registration_create_view(self):  # new
#         response = self.client.post(reverse('courseinfo_registration_create_urlpattern'), {
#             'section_name': 'New Section Name',
#         })
#
#         self.assertEqual(response.status_code, 200)
#         # self.assertContains(response, 'New Section Name')
#
#     def test_instructor_update_view(self):  # new
#         response = self.client.post(reverse('courseinfo_instructor_update_urlpattern', args='1'), {
#             'first_name': 'Updated First Name',
#             'last_name': 'Updated Last Name',
#         })
#
#         self.assertEqual(response.status_code, 302)
#
#     def test_student_update_view(self):  # new
#         response = self.client.post(reverse('courseinfo_student_update_urlpattern', args='1'), {
#             'first_name': 'Updated First Name',
#             'last_name': 'Updated Last Name',
#         })
#
#         self.assertEqual(response.status_code, 302)
#
#     def test_instructor_delete_view(self):  # new
#         response = self.client.get(
#             reverse('courseinfo_instructor_delete_urlpattern', args='1'))
#
#         self.assertEqual(response.status_code, 200)
#
#     def test_student_delete_view(self):  # new
#         response = self.client.get(
#             reverse('courseinfo_student_delete_urlpattern', args='1'))
#
#         self.assertEqual(response.status_code, 200)
#
#     def test_section_delete_view(self):  # new
#         response = self.client.get(
#             reverse('courseinfo_section_delete_urlpattern', args='1'))
#
#         self.assertEqual(response.status_code, 200)
#
#     def test_semester_delete_view(self):  # new
#         response = self.client.get(
#             reverse('courseinfo_semester_delete_urlpattern', args='1'))
#
#         self.assertEqual(response.status_code, 200)
#
#     def test_course_delete_view(self):  # new
#         response = self.client.get(
#             reverse('courseinfo_course_delete_urlpattern', args='1'))
#
#         self.assertEqual(response.status_code, 200)
#
#     def test_registration_delete_view(self):  # new
#         response = self.client.get(
#             reverse('courseinfo_registration_delete_urlpattern', args='1'))
#
#         self.assertEqual(response.status_code, 200)
