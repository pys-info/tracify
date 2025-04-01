import json
from io import BytesIO
from urllib.parse import parse_qs

from django.http import RawPostDataException
from django.http.multipartparser import MultiPartParser


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
    Process the request and convert request body into a dictionary.

    Args:
        request: The incoming request.

    Returns:
        dict: Request body as a dictionary.
    """

    # Cache the request body to prevent multiple reads
    if not hasattr(request, '_body_cache'):
        try:
            request._body_cache = request.body  # Store body on first access
        except RawPostDataException:
            request._body_cache = b''  # Handle cases where body is already read

    body = {}

    if request.content_type == "application/x-www-form-urlencoded":
        body = {key: value[0] for key, value in parse_qs(request._body_cache.decode()).items()}

    elif request.content_type == "multipart/form-data":
        if request.method == "POST":
            body.update(request.POST.dict())
            prepare_file_list(request.FILES, body)  # Assuming this function exists
        else:
            parser = MultiPartParser(
                request.META,
                BytesIO(request._body_cache),
                request.upload_handlers,
                request.encoding,
            )
            query_dict, multi_value_dict = parser.parse()
            body.update(query_dict.dict())
            prepare_file_list(multi_value_dict, body)

    elif request.content_type == "application/json":
        try:
            body = json.loads(request._body_cache.decode())
        except json.JSONDecodeError:
            body = {}

    return body
