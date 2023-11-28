import os
from azure.storage.blob import BlobServiceClient

storage_account_name = os.environ['newfuncapp666']
storage_account_key = os.environ['g33Mtk8bDVX+pBjrzsUVZT9cA4tuMCefxJbvb0HMkQs7Tbeor2tfE4ZMX7RNT0te12abLb03vnVo+AStfDkppg==']
container_name = 'newcon'
blob_name = 'data.json'

    # Create a BlobServiceClient
blob_service_client = BlobServiceClient(account_url=f"https://{storage_account_name}.blob.core.windows.net", credential=storage_account_key)

    # Get the container and blob client
container_client = blob_service_client.get_container_client(container_name)
blob_client = container_client.get_blob_client(blob_name)

    # Download blob content as bytes
blob_data = blob_client.download_blob().readall()

    # Convert bytes to string (assuming it's a JSON file)
json_content = blob_data.decode('utf-8')

    # Do something with the JSON content
print(json_content)

print(f"Processed {blob_name} successfully.")