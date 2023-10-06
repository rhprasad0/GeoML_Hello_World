import json
import boto3
import os
import numpy as np

# grab environment variables
ENDPOINT_NAME = os.environ['ENDPOINT_NAME']
runtime= boto3.client('runtime.sagemaker')

# Maybe I'll hook this up the the database to grab these, 
# but this will do for now
def get_continent(continent_id):
    if continent_id == 1:
        return "Africa"
    elif continent_id == 2:
        return "Asia"
    elif continent_id == 3:
        return "Australia"
    elif continent_id == 4:
        return "Europe"
    elif continent_id == 5:
        return "North America"
    elif continent_id == 6:
        return "Oceania"
    elif continent_id == 7:
        return "South America"
    elif continent_id == 8:
        return "Antarctica"
    else:
        return "Something is wrong :-("

# This is weird, but since I am using the default input_fn, predict_fn,
# and output_fn provided by SageMaker, it needs NumPy to go in and will spit
# out NumPy... apparently as a string? Anyway... this code just works.
def lambda_handler(event, context):
    lon_in = float(event['lon'])
    lat_in = float(event['lat'])
    print("lon = " + str(lon_in))
    print("lat = " + str(lat_in))
    data = np.array([[lon_in,lat_in]])
    payload_data = json.dumps(data.tolist())
    print(f"payload: {payload_data}")
    response = runtime.invoke_endpoint(EndpointName=ENDPOINT_NAME,
                                       ContentType='application/json',
                                       Body=payload_data)
    result = response['Body'].read().decode('utf-8')
    print(result)
    continent_id = int(result[1]) # This is a mere string, grab the number from it
    return {"prediction:":get_continent(continent_id)}
