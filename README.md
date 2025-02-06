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

## Minimum Permissions Required
- For minimum permissions required, refer to Minimum Permissions Table section at the end of this document.
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
## Getting Access Tokens

You can obtain authentication tokens to access the Microsoft Graph APIs using two methods:

1. **On behalf of the User – Delegated Permission.** For more information, see [https://docs.microsoft.com/en-us/graph/auth-v2-user](https://docs.microsoft.com/en-us/graph/auth-v2-user).

2. **Without a User – Application Permission.** For more information, see [https://docs.microsoft.com/en-us/graph/auth-v2-service](https://docs.microsoft.com/en-us/graph/auth-v2-service).

### Getting Access Tokens using the On behalf of the User – Delegated Permission method

1. Ensure that the required permissions are granted for the registration of the application. Navigate to **API Permissions** > **Add permission** > **Microsoft Graph** > **Delegated Permissions**.

   **Note:** The API Permission that should be granted to the registered application is mentioned in the Minimum permissions required for the 'Delegate-type' permission table.

2. The Redirect URL can be directed to any web application to receive responses from Azure AD. If you are unsure about what to set as a redirect URL, you can use `https://localhost/myapp`.

3. Copy the following URL and replace the `TENANT_ID`, `CLIENT_ID`, and `REDIRECT_URI` with your tenant ID, client ID, and the redirect URL:
https://login.microsoftonline.com/TENANT_ID/oauth2/v2.0/authorize?response_type=code&scope=offline_access%20https://graph.microsoft.com/.default&client_id=CLIENT_ID&redirect_uri=REDIRECT_URI

4. Enter the above link with the replaced values in your browser. You will be prompted to grant permissions for your Azure Service Management. You will be automatically redirected to a link with the following structure: `REDIRECT_URI?code=AUTH_CODE&session_state=SESSION_STATE`.

5. Copy the `AUTH_CODE` (without the `code=` prefix) and paste it in your instance configuration in the **Authorization Code** parameter.

6. Enter your client ID in the **Client ID** parameter field.

7. Enter your client secret in the **Client Secret** parameter field.

8. Enter your tenant ID in the **Tenant ID** parameter field.

9. Enter your redirect URL in the **Redirect URL** parameter field. By default, it is set to `https://localhost/myapp`.

### Getting Access Tokens using the Without a User – Application Permission method

1. Ensure that the required permissions are granted for the registration of the application.

For example, for a Microsoft Graph User, the API/Permission names that should be granted are:

- `Directory.Read.All`
- `Directory.ReadWrite.All`
- `GroupMember.Read.All`
- `Group.Read.All`
- `Group.ReadWrite.All`
- `IdentityRiskyUser.Read.All`
- `Mail.ReadBasic.All`
- `Mail.Read`
- `Mail.ReadWrite`
- `SecurityEvents.Read.All`
- `SecurityEvents.ReadWrite.All`
- `Policy.Read.All`
- `Policy.ReadWrite.ConditionalAccess` of type Application

2. Enter your client ID in the **Client ID** parameter field.

3. Enter your client secret in the **Client Secret** parameter field.

4. Enter your tenant ID in the **Tenant ID** parameter field.

### Getting Access Tokens using the Certificate Based Authentication method

1. Register an application with the Microsoft identity platform. To learn about creating an application, refer to [https://learn.microsoft.com/en-us/entra/identity-platform/quickstart-register-app#register-an-application](https://learn.microsoft.com/en-us/entra/identity-platform/quickstart-register-app#register-an-application).

2. Upload a CA certificate to the Azure portal. To learn about uploading the CA certificate, refer to [Uploading a CA certificate](https://learn.microsoft.com/en-us/azure/active-directory/develop/howto-create-self-signed-certificate#upload-the-certificate-to-your-application).

Note the thumbprint, start date, and expiration values once the certificate is uploaded.

3. Enter the certificate thumbprint and upload the corresponding private key in the Configuration Parameters.

## Minimum Permissions Table

To call the Microsoft Graph API and perform any action, you must be assigned specific permissions as defined in this section. To learn more, including how to choose permissions, see the [Microsoft Graph permissions reference](https://docs.microsoft.com/en-us/graph/permissions-reference).


<table border="1">
	<thead>
		<tr>
			<th>Action Name</th>
			<th>Permission Type</th>
			<th>Permissions (from least to most privileged)</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td rowspan="2">Get Risky Users List</td>
			<td>Delegated</td>
			<td><code>IdentityRiskyUser.Read.All</code></td>
		</tr>
		<tr>
			<td>Application</td>
			<td><code>IdentityRiskyUser.Read.All</code></td>
		</tr>
		<tr>
			<td rowspan="2">Get Risky User Details</td>
			<td>Delegated</td>
			<td><code>IdentityRiskyUser.Read.All</code></td>
		</tr>
		<tr>
			<td>Application</td>
			<td><code>IdentityRiskyUser.Read.All</code></td>
		</tr>
		<tr>
			<td rowspan="2">Get All Security Alerts</td>
			<td>Delegated</td>
			<td><code>SecurityEvents.Read.All</code>, <code>SecurityEvents.ReadWrite.All</code></td>
		</tr>
		<tr>
			<td>Application</td>
			<td><code>SecurityEvents.Read.All</code>, <code>SecurityEvents.ReadWrite.All</code></td>
		</tr>
		<tr>
			<td rowspan="2">Get Security Alert</td>
			<td>Delegated</td>
			<td><code>SecurityEvents.Read.All</code>, <code>SecurityEvents.ReadWrite.All</code></td>
		</tr>
		<tr>
			<td>Application</td>
			<td><code>SecurityEvents.Read.All</code>, <code>SecurityEvents.ReadWrite.All</code></td>
		</tr>
		<tr>
			<td rowspan="2">Update Security Alert</td>
			<td>Delegated</td>
			<td><code>SecurityEvents.ReadWrite.All</code></td>
		</tr>
		<tr>
			<td>Application</td>
			<td><code>SecurityEvents.ReadWrite.All</code></td>
		</tr>
		<tr>
			<td rowspan="2">Get Groups</td>
			<td>Delegated</td>
			<td><code>GroupMember.Read.All</code>, <code>Group.Read.All</code>, <code>Directory.Read.All</code>, <code>Group.ReadWrite.All</code>, <code>Directory.ReadWrite.All</code></td>
		</tr>
		<tr>
			<td>Application</td>
			<td><code>GroupMember.Read.All</code>, <code>Group.Read.All</code>, <code>Directory.Read.All</code>, <code>Group.ReadWrite.All</code>, <code>Directory.ReadWrite.All</code></td>
		</tr>
		<tr>
			<td rowspan="2">Get Users Within A Group</td>
			<td>Delegated</td>
			<td><code>GroupMember.Read.All</code>, <code>Group.Read.All</code>, <code>Directory.Read.All</code>, <code>Group.ReadWrite.All</code>, <code>Directory.ReadWrite.All</code></td>
		</tr>
		<tr>
			<td>Application</td>
			<td><code>GroupMember.Read.All</code>, <code>Group.Read.All</code>, <code>Directory.Read.All</code>, <code>Group.ReadWrite.All</code>, <code>Directory.ReadWrite.All</code></td>
		</tr>
		<tr>
			<td rowspan="2">Search Messages in Users mailbox</td>
			<td>Delegated</td>
			<td><code>Mail.ReadWrite</code></td>
		</tr>
		<tr>
			<td>Application</td>
			<td><code>Mail.ReadWrite</code></td>
		</tr>
		<tr>
			<td rowspan="2">Delete Message</td>
			<td>Delegated</td>
			<td><code>Mail.ReadWrite</code></td>
		</tr>
		<tr>
			<td>Application</td>
			<td><code>Mail.ReadWrite</code></td>
		</tr>
		<tr>
			<td rowspan="2">Delete Messages Bulk</td>
			<td>Delegated</td>
			<td><code>Mail.ReadWrite</code></td>
		</tr>
		<tr>
			<td>Application</td>
			<td><code>Mail.ReadWrite</code></td>
		</tr>
		<tr>
			<td rowspan="2">Revoke user session</td>
			<td>Delegated</td>
			<td><code>User.ReadWrite.All</code>, <code>Directory.ReadWrite.All</code></td>
		</tr>
		<tr>
			<td>Application</td>
			<td><code>User.ReadWrite.All</code>, <code>Directory.ReadWrite.All</code></td>
		</tr>
		<tr>
			<td rowspan="2">Get All Named Locations</td>
			<td>Delegated</td>
			<td><code>Policy.Read.All</code></td>
		</tr>
		<tr>
			<td>Application</td>
			<td><code>Policy.Read.All</code></td>
		</tr>
		<tr>
			<td rowspan="2">Block IP Ranges</td>
			<td>Delegated</td>
			<td><code>Policy.Read.All</code> and <code>Policy.ReadWrite.ConditionalAccess</code></td>
		</tr>
		<tr>
			<td>Application</td>
			<td><code>Policy.Read.All</code> and <code>Policy.ReadWrite.ConditionalAccess</code></td>
		</tr>
		<tr>
			<td rowspan="2">Unblock IP ranges</td>
			<td>Delegated</td>
			<td><code>Policy.Read.All</code> and <code>Policy.ReadWrite.ConditionalAccess</code></td>
		</tr>
		<tr>
			<td>Application</td>
			<td><code>Policy.Read.All</code> and <code>Policy.ReadWrite.ConditionalAccess</code></td>
		</tr>
		<tr>
			<td rowspan="2">Create IP Named Location</td>
			<td>Delegated</td>
			<td><code>Policy.Read.All</code> and <code>Policy.ReadWrite.ConditionalAccess</code></td>
		</tr>
		<tr>
			<td>Application</td>
			<td><code>Policy.Read.All</code> and <code>Policy.ReadWrite.ConditionalAccess</code></td>
		</tr>
	</tbody>
</table>
