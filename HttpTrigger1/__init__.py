import logging
import json
import pandas as pd
import tables
from azure.storage.blob import BlockBlobService
from io import StringIO
import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    file_path=""
    df = pd.read_excel('file_path')  
    output  = df.to_csv(index=False) 

    STORAGEACCOUNTNAME= "*****"
    STORAGEACCOUNTKEY= "*****"
    blobService = BlockBlobService(account_name=STORAGEACCOUNTNAME, account_key=STORAGEACCOUNTKEY)

    blobService.create_blob_from_text('csv', 'test2.csv', output)
    name = {"test":"test"}
   
    return func.HttpResponse(
            json.dumps(name),
            mimetype="application/json",
    )
