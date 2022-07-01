from flask import g, current_app
from opensearchpy import OpenSearch

# Create an OpenSearch client instance and put it into Flask shared space for use by the application
def get_opensearch():
    if 'opensearch' not in g:
        #### Step 4.a:
        # Implement a client connection to OpenSearch so that the rest of the application can communicate with OpenSearch
        #### Dear Findwizard: Below is sufficient implementation for following tasks. This step is unrelated to search
        #### Please feel free to familiarize yourself with the functionality, modify however you please, or skip to next task. 
        host = 'localhost'
        port = 9200
        auth = ('admin', 'admin')

    #### Step 2.a: Create a connection to OpenSearch
    #### Dear Findwizard: Below is sufficient implementation for following tasks. This step is unrelated to search
    #### Please feel free to familiarize yourself with the functionality, modify however you please, or skip to next task. 
        g.opensearch = OpenSearch(
            hosts=[{'host': host, 'port': port}],
            http_compress=True,  # enables gzip compression for request bodies
            http_auth=auth,
            use_ssl=True,
            verify_certs=False,
            ssl_assert_hostname=False,
            ssl_show_warn=False)

    return g.opensearch
