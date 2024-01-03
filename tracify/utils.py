from urllib.parse import parse_qs
from django.http.multipartparser import MultiPartParser
from io import BytesIO
import json


def prepare_file_list(file_dict, body):
    for key in file_dict:
        for file in file_dict.getlist(key):
            if body.get(key):
                file_list = body.get(key)
                file_list.append(file.name)
                body.update({key: file_list})
            else:
                body.update({key: [file.name]})


def get_body_data(request):
    """
    Process the request and convert request body in dictionary.

    Args:
        request: The incoming request.

    Returns:
        body: request body in dictionary format

    """

    if request.content_type == "application/x-www-form-urlencoded":
        body = {key: value[0] for key, value in parse_qs(request.body.decode()).items()}
        return body

    elif request.content_type == "multipart/form-data":
        body = {}
        if request.method == "POST":
            body.update(request.POST.dict())
            prepare_file_list(request.FILES, body)
            return body
        else:
            parser = MultiPartParser(request.META, BytesIO(request.body), request.upload_handlers, request.encoding)
            query_dict, multi_value_dict = parser.parse()

            body.update(query_dict.dict())
            prepare_file_list(multi_value_dict, body)
            return body

    elif request.content_type == "application/json":
        body = json.loads(request.body.decode())
        return body
