from django.test import TestCase
from django.urls import reverse

class PortfolioTests(TestCase):

    def test_home_page_status_code(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_about_page_status_code(self):
        response = self.client.get(reverse('about'))
        self.assertEqual(response.status_code, 200)

    def test_projects_page_status_code(self):
        response = self.client.get(reverse('projects'))
        self.assertEqual(response.status_code, 200)

    def test_home_page_template(self):
        response = self.client.get(reverse('home'))
        self.assertTemplateUsed(response, 'portfolio/home.html')

    def test_about_page_template(self):
        response = self.client.get(reverse('about'))
        self.assertTemplateUsed(response, 'portfolio/about.html')

    def test_projects_page_template(self):
        response = self.client.get(reverse('projects'))
        self.assertTemplateUsed(response, 'portfolio/projects.html')