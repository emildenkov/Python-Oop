from unittest import TestCase, main
from project.student import Student


class TestStudent(TestCase):

    def setUp(self):
        self.student = Student("Test1", {})
        self.student_with_courses = Student("Test2", {"basics": ["for", "while"]})

    def test_correct_init_without_courses(self):
        self.assertEqual("Test1", self.student.name)
        self.assertEqual({}, self.student.courses)

    def test_correct_init_with_courses(self):
        self.assertEqual("Test2", self.student_with_courses.name)
        self.assertEqual({"basics": ["for", "while"]}, self.student_with_courses.courses)

    def test_enroll_without_third_param_appending_notes_to_course(self):
        result = self.student_with_courses.enroll("basics", ["if statements"])

        self.assertEqual("Course already added. Notes have been updated.", result)
        self.assertEqual(["for", "while", "if statements"], self.student_with_courses.courses["basics"])

    def test_enroll_new_course_with_third_param_Y_appending_course_and_notes(self):
        result = self.student.enroll("basics", ["for", "while"], "Y")

        self.assertEqual("Course and course notes have been added.", result)
        self.assertEqual({"basics": ["for", "while"]}, self.student.courses)

    def test_enroll_new_course_with_third_param_none_appending_course_and_notes(self):
        result = self.student.enroll("basics", ["for", "while"], "")

        self.assertEqual("Course and course notes have been added.", result)
        self.assertEqual({"basics": ["for", "while"]}, self.student.courses)

    def test_enroll_new_course_with_different_third_param_appending_course_and_notes(self):
        result = self.student.enroll("basics", ["for", "while"], "uoh")

        self.assertEqual("Course has been added.", result)
        self.assertEqual({"basics": []}, self.student.courses)

    def test_add_notes_appends_notes_to_list_in_dict_and_returns_str(self):
        result = self.student_with_courses.add_notes("basics", "nested loops")

        self.assertEqual("Notes have been updated", result)
        self.assertEqual(["for", "while", "nested loops"], self.student_with_courses.courses["basics"])

    def test_add_notes_when_course_in_not_found_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.student_with_courses.add_notes("advanced", "matrix")

        self.assertEqual("Cannot add notes. Course not found.", str(ex.exception))

    def test_leave_course_pops_course_and_returns_proper_str(self):
        result = self.student_with_courses.leave_course("basics")

        self.assertEqual("Course has been removed", result)
        self.assertEqual({}, self.student_with_courses.courses)

    def test_leave_courses_when_no_course_found_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.student.leave_course("basics")

        self.assertEqual("Cannot remove course. Course not found.", str(ex.exception))


if __name__ == "__name__":
    main()
    