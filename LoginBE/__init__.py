import logging

import azure.functions as func
import http.client
import json
import requests
from CreateUserDAL import main


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.The function is LoginBE.')

    id = req.params.get('id')
    password = req.params.get('password')

    if not id or not password:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            id = req_body.get('id')
            password = req_body.get('password')

    if not all([id,password]):
        logging.info(f"{id},{password}")
        return func.HttpResponse('id or password is empty!',status_code=210)

    if id and password:
        url = 'http://localhost:7071/api/LoginDAL'
        headers = 'Content-Type:application/json'
        body ={'id':id,'password':password}
        # result=func.HttpRequest(method='POST',url=url,headers=headers,body=body)
        host = 'localhost:7071'
        conn=http.client.HTTPConnection(host)
        logging.info(f"body is {body}")
        bytes =json.dumps(body).encode()
        params={
            "req":{'id': id, 'password': password}
        }

        headers = {
            "Content-Type":
            "application/json; charset=utf-8"
        }

        response = requests.request(method='POST', url=url, json=params,headers=headers)
        # response = func.HttpRequest(method='POST',url=url, body=params, headers=headers)
        logging.info(f"response.get_body is {response.text}")
        if response!=200:
            return func.HttpResponse('Failed',status_code=210)
        else:
            return func.HttpResponse('Success',status_code=200)
        # Construct a mock HTTP request.
        # req = func.HttpRequest(
        #     method='GET',
        #     body=None,
        #     url='http://localhost:7071/api/GetUserDAL',
        #     params={'id': id,'password':password})


        # request_result=func.HttpRequest(method='POST', url=url, body=bytes,headers=headers)
        # result=conn.request(method='POST', url=url, params=params,headers=headers)
        # ss=conn.getresponse()
        # logging.info(f'result is {ss}')
        # conn.close()
    #     return func.HttpResponse()
    # else:
    #     return func.HttpResponse(
    #          "This HTTP triggered function executed successfully. Pass a password in the query string or in the request body for a personalized response.",
    #          status_code=200
    #     )
    return func.HttpResponse('Success', status_code=200)

# {"id": "1", "password": "123"}
