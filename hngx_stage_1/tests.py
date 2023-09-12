from django.test import TestCase
from hngx_stage_1.models import Person

class PersonAPITestCase(TestCase):
  def setUp(self):
    Person.objects.create(name="Charles Swaleh")
    Person.objects.create(name="John Jameson")
    Person.objects.create(name="Michael Jordan")
    Person.objects.create(name="Samantha Nawal")
    Person.objects.create(name="Logan Reynolds")

  def test_database_is_populated(self):
    self.assertEqual(Person.objects.count(), 5)

  def test_fetching_all_users_from_the_db(self):
    r = self.client.get("/api/")
    data = r.json()
    self.assertEqual(len(data["persons"]), 5)

  def test_fetching_a_single_user(self):
    r = self.client.get("/api/charles swaleh")
    data = r.json()
    self.assertEqual(data["name"], "Charles Swaleh")

  def test_fetching_a_nonexistent_user(self):
    r = self.client.get("/api/Kirsten Stewart")
    self.assertTrue(r.status_code, 404)

  def test_adding_a_new_user_and_check_id(self):
    r = self.client.post("/api/", data={"name": "Samantha Nawal"}, content_type="application/x-www-form-urlencoded")
    data = r.json()
    self.assertTrue(data["id"], 6)

  def test_adding_a_new_user_and_check_name(self):
      r = self.client.post("/api/", data={"name": "Samantha Nawal"}, content_type="application/x-www-form-urlencoded")
      data = r.json()
      self.assertTrue(data["name"], "Samantha Nawal")

  def test_adding_a_new_user_and_check_status_code(self):
    r = self.client.post("/api/", data={"name": "Samantha Nawal"}, content_type="application/x-www-form-urlencoded")
    self.assertEqual(r.status_code, 201)

  def test_adding_a_new_user_and_check_db_objects(self):
    r = self.client.post("/api/", data={"name": "Samantha Nawal"}, content_type="application/x-www-form-urlencoded")
    self.assertTrue(Person.objects.count(), 6)

  def test_updating_a_user_name(self):
    r = self.client.patch("/api/1", data={"name": "Swaleh Charles"}, content_type="application/x-www-form-urlencoded")
    person = Person.objects.get(pk=1)
    self.assertTrue(person.name, "Swaleh Charles")
