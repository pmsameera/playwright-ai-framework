class BaseAPI():

    def post(json_url, requestPayload):
        response = requests.post(json_url, json=requestPayload)
        return response.json()

    def get(json_url):
        response = requests.get(json_url)
        return response.json()

    def put(json_url, requestPayload):
        response = requests.put(json_url, json=requestPayload)
        return response.json()

    def delete(json_url):
        response = requests.delete(json_url)
        return response.json()