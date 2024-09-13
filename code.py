#Read data from Azure Key Vault using databricks dbutils command

certificate = dbutils.secrets.get(scope = "Azure Key Vault Name", key = "Certificate File Name")

#Save this certificate to *.pem file on Databricks. Below code will create a dummy certificate.pem in write mode and write the content of certificate (certificate from AKV) in to created dummy certificate.pem file.

with open("certificate.pem","w+") as f:
    f.write(certificate)
    f.close()

cert_file = "certificate.pem"

from zeep import Settings, exceptions
from zeep.client import Client
from zeep.transports import Transport
from requests import Session
from requests.auth import HTTPBasicAuth

#using request create session. username and password is login details of services could be SAP server or any other server
'''
params description
Settings

strict: When set to True, Zeep enforces strict XML schema validation. This means that the SOAP client will check the XML against the WSDL schema definitions and raise errors if the XML does not conform to the schema. If set to False, the client will be more lenient and may accept XML that does not strictly follow the schema.
xml_huge_tree: When set to True, this option allows Zeep to handle very large XML documents by using an alternative XML parser that can process large XML files more efficiently. This is useful if you are working with large responses from the SOAP service and need to avoid issues with XML parsing.
raw_response: When set to True, Zeep will return the raw XML response from the server instead of parsing it into a Python object. This can be useful for debugging or when you need to process the raw XML data manually.
force_https: When set to False, Zeep will not enforce HTTPS for the service endpoint, allowing HTTP connections if they are specified. If set to True, Zeep will automatically force the use of HTTPS for secure communication.

transport

timeout: This parameter sets the maximum amount of time (in seconds) that the client will wait for a response from the server. This is for the entire request and response cycle.
operation_timeout: This parameter sets the maximum amount of time (in seconds) that the client will wait specifically for the SOAP operation to complete. This can be useful if you want to apply a different timeout setting specifically for the operation phase.
session: This parameter allows you to pass a requests.Session object to manage connections. Using a Session object can help manage connection pooling, session-wide configurations, and custom settings like headers, authentication, or client certificates.

'''
settings = Settings(strict = True, xml_huge_tree = True, raw_response = True, force_https = False)
session = Session()
# Update username and password as per your requirement
session.auth = HTTPBasicAuth(username,password)
session.cert = cert_file
transport = Transport(timeout = "value", operation_timeout = "value",session = session )
# Update wsdl with url and path of xml file.
cleint = Client(wsdl, settings = settings, transport = transport )
#Update endpoint url for the service
Client.service._binding_options["address"] = "enter url of service"