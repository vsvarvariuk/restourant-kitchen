from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse


class TestCookAdmin(TestCase):
    def setUp(self):
        self.client = Client()
        self.user_admin = get_user_model().objects.create_superuser(
            username="admin",
            password="admin12345"
        )
        self.client.force_login(self.user_admin)
        self.author = get_user_model().objects.create_user(
            username="author",
            password="author12345",
            years_of_experience=1
        )

    def test_cook_list_years_of_experience(self):
        url = reverse("admin:service_cook_changelist")
        res = self.client.get(url)
        self.assertContains(res, self.author.years_of_experience)

    def test_cook_detail_years_of_experience(self):
        url = reverse("admin:service_cook_change", args=[self.author.id])
        res = self.client.get(url)
        self.assertContains(res, self.author.years_of_experience)

    def test_cook_create_years_of_experience(self):
        url = reverse("admin:service_cook_add")
        res = self.client.get(url)
        self.assertContains(res, self.author.years_of_experience)
