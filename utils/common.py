from rest_framework.response import Response


def create_response(data=None, error=None, status=None):
    if 200 <= status < 400:
        success = True
    else:
        success = False

    response = {
        "data": data,
        "error": error,
        "success": success
    }
    return Response(data=response, status=status)
