# Client-Side Signed Certificate Authentication with Python (ZEEP)

*This project demonstrates how to authenticate using client-side signed certificates in Python, particularly for making SOAP requests using the ZEEP library.*

*Client-side certificates are often required in systems where mutual TLS (mTLS) authentication is enforced, ensuring both the client and server authenticate each other using certificates. This README will guide you through using client-side signed certificates to authenticate your SOAP requests in Python.*

## Table of Contents
1. Overview
2. Features
3. Official Documentation
4. Additional Information
5. Implementation

### Overview

In many systems that expose APIs (either REST or SOAP-based), authentication is required to access resources. The method of authentication can vary depending on server configuration—common methods include Basic Auth, OAuth, and Client-Side Certificate Authentication (mTLS).

### Features

- Supports client-side certificate authentication using mutual TLS (mTLS).
- Integrates with SOAP services through the ZEEP module.
- Demonstrates how to pass client certificates along with SOAP requests.
- Securely handles communication between the client and server.

### Requirements

- Python 3.x
- ZEEP module
- An existing client certificate, private key, and CA certificate

### Official Documentation

For more detailed information about the ZEEP library and its features, please refer to the official documentation. The documentation provides comprehensive guidance on how to use ZEEP, including configuration options, API methods, and advanced usage scenarios.

https://docs.python-zeep.org/en/master/

### Additional Information

Security Considerations: Client-side certificates are sensitive pieces of information. Ensure that you protect your private key by using proper file permissions and never hard-code sensitive credentials in your source code.

Debugging: Enable logging to see detailed output from ZEEP and the underlying session.

*ZEEP module uses the requests module for handling HTTP(S) requests. ZEEP is a SOAP client library in Python that abstracts the complexities of making SOAP requests and responses, but under the hood, it relies on requests to perform the actual HTTP(S) operations.*

### Implementation

In the provided code, we retrieve a certificate from Azure Key Vault using Databricks, save it as a local .pem file, and utilize it for client authentication in a Zeep session request. Additionally, we use a WSDL file stored locally as an XML file instead of referencing it via a URL.

