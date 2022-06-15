import json
import requests
import pandas as pd


def handler(event, context):

    # TODO implementation
    df=pd.DataFrame({"A":[1,2,3],"B":[4,5,6]})
    print(df)

    return {
        'headers': {'Content-Type' : 'application/json'},
        'statusCode': 200,
        'body': json.dumps({"message": "Lambda Container image invoked!",
                            "event": event})
    }
