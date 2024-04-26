from django.test import SimpleTestCase
from django.urls import reverse, resolve
from habits.views import HabitCreateAPIView, HabitListAPIView, PublicHabitListAPIView, \
    HabitRetrieveAPIView, HabitUpdateAPIView, HabitDestroyAPIView


class TestUrls(SimpleTestCase):
    def test_habit_create_url_resolves(self):
        url = reverse('habits:habit_create')
        self.assertEqual(resolve(url).func.view_class, HabitCreateAPIView)

    def test_habit_list_url_resolves(self):
        url = reverse('habits:habit_list')
        self.assertEqual(resolve(url).func.view_class, HabitListAPIView)

    def test_public_habit_list_url_resolves(self):
        url = reverse('habits:public_habit_list')
        self.assertEqual(resolve(url).func.view_class, PublicHabitListAPIView)

    def test_habit_retrieve_url_resolves(self):
        url = reverse('habits:habit', args=[1])  # Предполагая, что для теста у вас есть привычка с id=1
        self.assertEqual(resolve(url).func.view_class, HabitRetrieveAPIView)

    def test_habit_update_url_resolves(self):
        url = reverse('habits:habit_update', args=[1])  # Предполагая, что для теста у вас есть привычка с id=1
        self.assertEqual(resolve(url).func.view_class, HabitUpdateAPIView)

    def test_habit_delete_url_resolves(self):
        url = reverse('habits:habit_delete', args=[1])  # Предполагая, что для теста у вас есть привычка с id=1
        self.assertEqual(resolve(url).func.view_class, HabitDestroyAPIView)
