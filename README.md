## About the connector

<p>This document provides information about the Microsoft Defender Threat Intelligence Connector, which facilitates automated interactions, with a Microsoft Defender Threat Intelligence server using FortiSOAR&trade; playbooks. Add the Microsoft Defender Threat Intelligence Connector as a step in FortiSOAR&trade; playbooks and perform automated operations with Microsoft Defender Threat Intelligence.</p>

### Version information

Connector Version: 1.0.0


Authored By: SpryIQ.co

Certified: No
## Installing the connector
<p>From FortiSOAR&trade; 5.0.0 onwards, use the <strong>Connector Store</strong> to install the connector. For the detailed procedure to install a connector, click <a href="https://docs.fortinet.com/document/fortisoar/0.0.0/installing-a-connector/1/installing-a-connector" target="_top">here</a>.<br>You can also use the following <code>yum</code> command as a root user to install connectors from an SSH session:</p>
`yum install cyops-connector-microsoft-defender-threat-intelligence`

## Prerequisites to configuring the connector
- You must have the URL of Microsoft Defender Threat Intelligence server to which you will connect and perform automated operations and credentials to access that server.
- The FortiSOAR&trade; server should have outbound connectivity to port 443 on the Microsoft Defender Threat Intelligence server.

Also, before setting up the **Microsoft Defender Threat Intelligence Connector**, ensure the following requirements are met:

1. **Azure Application Registration (Required for Authentication)**
   - Register an application in Microsoft Entra Admin Center [(Guide)](https://learn.microsoft.com/en-us/graph/auth-register-app-v2).
   - Obtain the following values from the Azure portal:
     - **Application (Client) ID**
     - **Directory (Tenant) ID**
     - **Client Secret** (for app-based authentication)
     - **Authorization Code** (for user-based authentication)

2. **Grant API Permissions**
   - Go to **API Permissions** in the Azure app registration.
   - Add **Microsoft Graph API permissions** (based on your authentication method):
     - **Application Permissions**: Required for app-only authentication.
     - **Delegated Permissions**: Required if authenticating on behalf of a user.
   - Admin consent may be required depending on your organization’s policies.
   - Refer to [this guide](https://learn.microsoft.com/en-us/graph/auth-v2-user?tabs=http) for more details on permissions.

## Minimum Permissions Required
- N/A

## Configuring the connector
For the procedure to configure a connector, click [here](https://docs.fortinet.com/document/fortisoar/0.0.0/configuring-a-connector/1/configuring-a-connector)
### Configuration parameters
<p>In FortiSOAR&trade;, on the Connectors page, click the <strong>Microsoft Defender Threat Intelligence</strong> connector row (if you are in the <strong>Grid</strong> view on the Connectors page) and in the <strong>Configurations&nbsp;</strong> tab enter the required configuration details:&nbsp;</p>
<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>Get Access Token<br></td><td><br>
<strong>If you choose 'Without a User - Application Permission'</strong><ul><li>Server URL: Specify the service-based URI to connect and perform automated operations.</li><li>Tenant ID: Specify the ID of the tenant assigned to you by the Azure application registration portal.</li><li>Client ID: Specify the Unique Application ID of the Azure Active Directory application to create an authentication token required to access the API. For information on getting authentication tokens, see the Getting Authentication Tokens section.</li><li>Client Secret: Specify the Unique Client Secret of the Azure Active Directory application that is used to create an authentication token required to access the API. For information on how to get the secret key, see https://docs.microsoft.com/en-us/windows/security/threat-protection/microsoft-defender-atp/exposed-apis-create-app-webapp.</li></ul><strong>If you choose 'On behalf of User - Delegate Permission'</strong><ul><li>Server URL: Specify the service-based URI to connect and perform automated operations.</li><li>Tenant ID: Specify the ID of the tenant assigned to you by the Azure application registration portal.</li><li>Client ID: Specify the Unique Application ID of the Azure Active Directory application to create an authentication token required to access the API. For information on getting authentication tokens, see the Getting Authentication Tokens section.</li><li>Client Secret: Specify the Unique Client Secret of the Azure Active Directory application that is used to create an authentication token required to access the API. For information on how to get the secret key, see https://docs.microsoft.com/en-us/windows/security/threat-protection/microsoft-defender-atp/exposed-apis-create-app-webapp.</li><li>Authorization Code: Specify the authorization code that you acquired during the authorization step. For more information, see the Getting Access Tokens using the Delegate Permissions method section.</li><li>Redirect URL: The redirect_uri of your app, where authentication responses can be sent and received by your app. The redirect URL that you specify here must exactly match one of the redirect_uri's you have registered in your app registration portal.</li></ul></td></tr><tr><td>Verify SSL<br></td><td>Specifies whether the SSL certificate for the server is to be verified or not. <br/>By default, this option is set as True.<br></td></tr>
</tbody></table>

## Actions supported by the connector
The following automated operations can be included in playbooks and you can also use the annotations to access operations from FortiSOAR&trade; release 4.10.0 and onwards:
<table border=1><thead><tr><th>Function<br></th><th>Description<br></th><th>Annotation and Category<br></th></tr></thead><tbody><tr><td>Get Host Reputation<br></td><td>Retrieves security reputation and threat intelligence data for a specified host to assess its risk level and potential malicious activity.<br></td><td>get_host_reputation <br/>Containment<br></td></tr>
<tr><td>Get Host Details<br></td><td>Retrieves comprehensive host information including system details, network configurations, and associated threat intelligence data.<br></td><td>get_host_details <br/>Containment<br></td></tr>
<tr><td>Get Whois Record<br></td><td>Retrieves domain registration and ownership information through Whois lookup, either by host identifier or specific Whois record ID.<br></td><td>get_whoisrecord <br/>Containment<br></td></tr>
<tr><td>List Components<br></td><td>Retrieves an inventory of software components, services, and applications detected on the specified host system.<br></td><td>list_components <br/>Containment<br></td></tr>
<tr><td>List Passive DNS<br></td><td>Retrieves historical DNS resolution records showing how domain names have mapped to IP addresses over time.<br></td><td>list_passiveDns <br/>Containment<br></td></tr>
<tr><td>List Passive DNS Reverse<br></td><td>Retrieves historical reverse DNS records showing how IP addresses have mapped to domain names over time.<br></td><td>list_passiveDns_reverse <br/>Containment<br></td></tr>
<tr><td>List Host Ports<br></td><td>Retrieves a comprehensive list of open ports, associated services, and network protocols active on the specified host.<br></td><td>list_hostPorts <br/>Containment<br></td></tr>
<tr><td>List Host SSL Certificates<br></td><td>Retrieves all SSL/TLS certificates associated with the host, including validity dates, issuers, and certificate details.<br></td><td>list_host_ssl_certificates <br/>Containment<br></td></tr>
<tr><td>Get Host SSL Certificate<br></td><td>Retrieves detailed information about a specific SSL/TLS certificate, including chain of trust, cryptographic details, and validation status.<br></td><td>get_host_ssl_certificate <br/>Containment<br></td></tr>
<tr><td>Get Host Component<br></td><td>Retrieves detailed information about a specific software component, including version, configuration, and security status.<br></td><td>get_host_component <br/>Containment<br></td></tr>
<tr><td>List Indicators<br></td><td>Retrieves a comprehensive list of threat indicators, including IOCs, behavioral patterns, and security alerts from the specified intelligence profile.<br></td><td>list_indicators <br/>Containment<br></td></tr>
</tbody></table>

### operation: Get Host Reputation
#### Input parameters
<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>Host ID<br></td><td>Provide the IP address or Fully Qualified Domain Name (FQDN) of the host to retrieve its reputation information.<br>
</td></tr></tbody></table>

#### Output

 No output schema is available at this time.

### operation: Get Host Details
#### Input parameters
<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>Host ID<br></td><td>Enter either an IP address or Fully Qualified Domain Name (FQDN) to retrieve detailed host information and configurations.<br>
</td></tr></tbody></table>

#### Output

 No output schema is available at this time.

### operation: Get Whois Record
#### Input parameters
<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>Select Host ID or whoisRecord ID<br></td><td>Choose whether to look up Whois information using a host identifier or a specific Whois record ID.<br>
<strong>If you choose 'Host ID'</strong><ul><li>Host ID: </li></ul><strong>If you choose 'whoisRecord ID'</strong><ul><li>whoisRecord ID: </li></ul></td></tr></tbody></table>

#### Output

 No output schema is available at this time.

### operation: List Components
#### Input parameters
<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>Host ID<br></td><td>Enter the IP address or FQDN to list all detected components and services running on the host.<br>
</td></tr></tbody></table>

#### Output

 No output schema is available at this time.

### operation: List Passive DNS
#### Input parameters
<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>Host ID<br></td><td>Enter an IP address or FQDN to retrieve its historical DNS resolution records.<br>
</td></tr></tbody></table>

#### Output

 No output schema is available at this time.

### operation: List Passive DNS Reverse
#### Input parameters
<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>Host ID<br></td><td>Enter an IP address or FQDN to retrieve its historical reverse DNS resolution records.<br>
</td></tr></tbody></table>

#### Output

 No output schema is available at this time.

### operation: List Host Ports
#### Input parameters
<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>Host ID<br></td><td>Enter an IP address or FQDN to list all open ports and their associated services on the host.<br>
</td></tr></tbody></table>

#### Output

 No output schema is available at this time.

### operation: List Host SSL Certificates
#### Input parameters
<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>Host ID<br></td><td>Enter an IP address or FQDN to list all SSL certificates associated with the host.<br>
</td></tr></tbody></table>

#### Output

 No output schema is available at this time.

### operation: Get Host SSL Certificate
#### Input parameters
<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>Host Certificate ID<br></td><td>Enter the specific SSL certificate identifier to retrieve its detailed information.<br>
</td></tr></tbody></table>

#### Output

 No output schema is available at this time.

### operation: Get Host Component
#### Input parameters
<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>Host Component ID<br></td><td>Enter the specific component identifier to retrieve detailed information about that software component.<br>
</td></tr></tbody></table>

#### Output

 No output schema is available at this time.

### operation: List Indicators
#### Input parameters
<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>Intelligence Profile ID<br></td><td>Enter the intelligence profile identifier to retrieve associated threat indicators and IOCs.<br>
</td></tr></tbody></table>

#### Output

 No output schema is available at this time.
## Included playbooks
The `Sample - microsoft-defender-threat-intelligence - 1.0.0` playbook collection comes bundled with the Microsoft Defender Threat Intelligence connector. These playbooks contain steps using which you can perform all supported actions. You can see bundled playbooks in the **Automation** > **Playbooks** section in FortiSOAR<sup>TM</sup> after importing the Microsoft Defender Threat Intelligence connector.

- Get Host Reputation
- Get Host Details
- Get Whois Record
- List Components
- List Passive DNS
- List Passive DNS Reverse
- List Host Ports
- List Host SSL Certificates
- Get Host SSL Certificate
- Get Host Component
- List Indicators

**Note**: If you are planning to use any of the sample playbooks in your environment, ensure that you clone those playbooks and move them to a different collection, since the sample playbook collection gets deleted during connector upgrade and delete.
