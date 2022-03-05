import json

print('Loading function')


def lambda_handler(event, context):
    # parse out query string params
    transactionId = event['queryStringParameters']['transactionId']
    transactionType = event['queryStringParameters']['type']
    transactionAmount = event['queryStringParameters']['amount']

    print('transactionId = ' + transactionId)
    print('transactionType = ' + transactionType)
    print('transactionAmount = ' + transactionAmount)

    # Construct the body of theresponse json object
    transactionResponse = {}
    transactionResponse['transactionId'] = transactionId
    transactionResponse['type'] = transactionType
    transactionResponse['amount'] = transactionAmount
    transactionResponse['message'] = 'Hello from Lambda Land'

    # Construct http response object
    responseObject = {}
    responseObject['statusCode'] = 200
    responseObject['headers'] = {}
    responseObject['headers']['Content-Type'] = 'application/json'
    responseObject['body'] = json.dumps(transactionResponse)

    # return the response object
    return responseObject
