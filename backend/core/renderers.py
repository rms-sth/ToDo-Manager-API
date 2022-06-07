from rest_framework.renderers import JSONRenderer
from rest_framework.utils.serializer_helpers import ReturnList, ReturnDict


class CustomJSONRenderer(JSONRenderer):
    def render(self, data, accepted_media_type=None, renderer_context=None):

        response_dict = {"status": "success", "message": "Successful", "data": data}

        if type(data) in (ReturnList, list):
            print("this is list response")
            response_dict["data"] = data
            response_dict["message"] = "Successful"
            response_dict["status"] = "success"

        elif type(data) in (ReturnDict, dict):
            print("this is dict type response")
            # data
            if data.get("data") is not None:
                response_dict["data"] = data.get("data")
            else:
                response_dict["data"] = data
            # status
            if data.get("status"):
                response_dict["status"] = data.get("status")
            # message
            if data.get("message"):
                response_dict["message"] = data.get("message")

        response = response_dict
        return super(CustomJSONRenderer, self).render(
            response, accepted_media_type, renderer_context
        )
