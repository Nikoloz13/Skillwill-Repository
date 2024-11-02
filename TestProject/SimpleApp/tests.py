from django.test import TestCase
from .models import SimpleModel
from django.urls import reverse
from .forms import SimpleModelForm

class SimpleModelTests(TestCase):

    def setUp(self):
        self.obj = SimpleModel.objects.create(name="Test Model", description="A test model description")

    def test_model_save(self):
        obj = SimpleModel(name="Save Test", description="Testing save")
        obj.save()
        self.assertEqual(SimpleModel.objects.get(id=obj.id), obj)

    def test_model_retrieve(self):
        retrieved_obj = SimpleModel.objects.get(id=self.obj.id)
        self.assertEqual(retrieved_obj, self.obj)

    def test_model_update(self):
        self.obj.description = "Updated description"
        self.obj.save()
        updated_obj = SimpleModel.objects.get(id=self.obj.id)
        self.assertEqual(updated_obj.description, "Updated description")

    def test_model_delete(self):
        self.obj.delete()
        with self.assertRaises(SimpleModel.DoesNotExist):
            SimpleModel.objects.get(id=self.obj.id)


class ModelListViewTests(TestCase):

    def setUp(self):
        SimpleModel.objects.create(name="Model 1", description="Description 1")
        SimpleModel.objects.create(name="Model 2", description="Description 2")

    def test_view_status_code(self):
        response = self.client.get(reverse('model_list'))
        self.assertEqual(response.status_code, 200)

    def test_view_queryset(self):
        response = self.client.get(reverse('model_list'))
        self.assertEqual(len(response.context['objects']), 2)

    def test_view_template(self):
        response = self.client.get(reverse('model_list'))
        self.assertTemplateUsed(response, 'SimpleApp/model_list.html')


class SimpleModelFormTests(TestCase):

    def test_form_valid_data(self):
        form = SimpleModelForm(data={'name': 'Test Model', 'description': 'A description'})
        self.assertTrue(form.is_valid())

    def test_form_invalid_data(self):
        form = SimpleModelForm(data={'name': '', 'description': 'A description'})
        self.assertFalse(form.is_valid())

class ModelUpdateViewTests(TestCase):

    def setUp(self):
        self.obj = SimpleModel.objects.create(name="Test Model", description="A description")

    def test_update_view_status_code(self):
        response = self.client.get(reverse('model_update', args=[self.obj.id]))
        self.assertEqual(response.status_code, 200)

    def test_update_view_template(self):
        response = self.client.get(reverse('model_update', args=[self.obj.id]))
        self.assertTemplateUsed(response, 'SimpleApp/model_form.html')

    def test_update_object(self):
        self.client.post(reverse('model_update', args=[self.obj.id]), {'name': 'Updated Model', 'description': 'Updated description'})
        self.obj.refresh_from_db()
        self.assertEqual(self.obj.name, 'Updated Model')


class ModelDeleteViewTests(TestCase):

    def setUp(self):
        self.obj = SimpleModel.objects.create(name="Test Model", description="A description")

    def test_delete_view_status_code(self):
        response = self.client.post(reverse('model_delete', args=[self.obj.id]))
        self.assertEqual(response.status_code, 302)

    def test_delete_object(self):
        self.client.post(reverse('model_delete', args=[self.obj.id]))
        with self.assertRaises(SimpleModel.DoesNotExist):
            SimpleModel.objects.get(id=self.obj.id)
