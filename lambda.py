import json

print('Loading function')


def lambda_handler(event, context):
    #print("Received event: " + json.dumps(event, indent=2))
    print("lon = " + event['lon'])
    print("lat = " + event['lat'])
    return {"lat":event['lat'], 
            "lon":event['lon'], 
            "prediction":"MODEL PREDICTION"}
    #return event['lat']  # Echo back
    #raise Exception('Something went wrong')
