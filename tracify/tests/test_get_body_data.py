from django.core.files.uploadedfile import InMemoryUploadedFile
from django.http import QueryDict
from django.test import RequestFactory, TestCase
from django.utils.datastructures import MultiValueDict
from requests_toolbelt.multipart.encoder import MultipartEncoder

from tracify.utils import get_body_data


class GetBodyDataTestCase(TestCase):
    def test_form_urlencoded_content_type(self):
        request = RequestFactory()
        request = request.post(
            "",
            data=b"name=John&age=30",
            content_type="application/x-www-form-urlencoded",
        )

        result = get_body_data(request)

        self.assertEqual(result, {"name": "John", "age": "30"})

    def test_multipart_form_data_content_type(self):
        request = RequestFactory()
        request.method = "POST"
        request.content_type = "multipart/form-data"

        data_dict = {"name": "John", "age": "30"}
        query_dict = QueryDict("", mutable=True)
        for key, values in data_dict.items():
            query_dict.appendlist(key, values)
        request.POST = query_dict

        file_1 = InMemoryUploadedFile(
            file=open("sample.jpg", "rb"),
            field_name="file",
            name="sample.jpg",
            content_type="image/png",
            size=1024,
            charset="utf-8",
        )

        file_2 = InMemoryUploadedFile(
            file=open("sample.jpg", "rb"),
            field_name="file1",
            name="sample.jpg",
            content_type="image/png",
            size=512,
            charset="utf-8",
        )

        request.FILES = MultiValueDict({"file": [file_1], "file1": [file_2]})

        result = get_body_data(request)

        expected_result = {
            "name": "John",
            "age": "30",
            "file": ["sample.jpg"],
            "file1": ["sample.jpg"],
        }

        self.assertEqual(result, expected_result)

    def test_multipart_form_data_content_type_else_part(self):
        with open("sample.jpg", "rb") as file:
            file_data = file.read()

        dynamic_data = {
            "name": "John",
            "file1_data": ("sample.jpg", file_data, "application/octet-stream"),
        }
        multipart_data = MultipartEncoder(fields=dynamic_data)

        request_factory = RequestFactory()
        request = request_factory.put(
            "", data=multipart_data.to_string(), content_type="multipart/form-data"
        )
        request.META.update({"CONTENT_TYPE": multipart_data.content_type})

        result = get_body_data(request)
        expected_result = {"name": "John", "file1_data": ["sample.jpg"]}

        self.assertEqual(result, expected_result)

    def test_application_json_content_type(self):
        request = RequestFactory()
        request = request.post(
            "", data=b'{"name": "John", "age": 30}', content_type="application/json"
        )

        result = get_body_data(request)

        self.assertEqual(result, {"name": "John", "age": 30})


class MockFile:
    def __init__(self, name):
        self.name = name
