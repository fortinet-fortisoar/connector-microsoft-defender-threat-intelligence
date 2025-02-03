"""
Copyright start
MIT License
Copyright (c) 2025 Fortinet Inc
Copyright end
"""

import requests
from .microsoft_api_auth import *
from connectors.core.connector import get_logger, ConnectorError
logger = get_logger('microsoft_graph')


class SetupSession(object):
    def __init__(self, config):
        self.connector_info = config.get('connector_info')
        self.ms = MicrosoftAuth(config)
        self.verify_ssl = self.ms.verify_ssl
        self.token = self.ms.validate_token(config, self.connector_info)
        self.__setupSession()

    def __setupSession(self):
        try:
            self.session = requests.session()
            self.session.headers.update({
                'User-Agent': 'fortiSOAR/1.0',
                'Authorization': self.token,
                'Accept': 'application/json',
                'Content-Type': 'application/json',
                'Prefer': 'return=representation'
            })
            self.session.verify = self.verify_ssl
            logger.error("Session set up successfully")
        except Exception as e:
            logger.exception('Error setting up session: {0}'.format(e))
            raise ConnectorError('Error setting up session: {0}'.format(e))


def get_host_reputation(config, params):
    try:
        logger.error("Starting 'get_host_reputation' operation with inputs: %s", params)
        microsoft_graph = SetupSession(config)
        graph_api_endpoint = '{0}/{1}'.format(microsoft_graph.ms.host, config.get('api_version'))
        logger.error("API endpoint constructed: %s", graph_api_endpoint)

        url = graph_api_endpoint + '/security/threatIntelligence/hosts/{0}/reputation'.format(params.get('hostId'))
        logger.error("Constructed URL for host reputation request: %s", url)

        microsoft_graph.session.headers.pop('Prefer', '')
        response = microsoft_graph.session.get(url=url)
        microsoft_graph.session.close()

        if response.ok:
            logger.error("Received successful response with response: %s", response.json())
            return response.json()
        else:
            logger.error("Failed request: %s, Response: %s, Reason: %s", url, response.content, response.reason)
            raise ConnectorError(
                'Failed to request API {0} response is :{1} with reason: {2}'.format(str(url), str(response.content),
                                                                                   str(response.reason)))
    except Exception as e:
        logger.exception("Error in 'get_host_reputation': %s", e)
        raise ConnectorError("Error in 'get_host_reputation': {0}".format(e))


def get_host_details(config, params):
    try:
        logger.error("Starting 'get_host_reputation' operation with inputs: %s", params)
        microsoft_graph = SetupSession(config)
        graph_api_endpoint = '{0}/{1}'.format(microsoft_graph.ms.host, config.get('api_version'))
        logger.error("API endpoint constructed: %s", graph_api_endpoint)

        url = graph_api_endpoint + '/security/threatIntelligence/hosts/{0}'.format(params.get('hostId'))
        logger.error("Constructed URL for host reputation request: %s", url)

        microsoft_graph.session.headers.pop('Prefer', '')
        response = microsoft_graph.session.get(url=url)
        microsoft_graph.session.close()

        if response.ok:
            logger.error("Received successful response with response: %s", response.json())
            return response.json()
        else:
            logger.error("Failed request: %s, Response: %s, Reason: %s", url, response.content, response.reason)
            raise ConnectorError(
                'Failed to request API {0} response is :{1} with reason: {2}'.format(str(url), str(response.content),
                                                                                   str(response.reason)))
    except Exception as e:
        logger.exception("Error in 'get_host_reputation': %s", e)
        raise ConnectorError("Error in 'get_host_reputation': {0}".format(e))


def get_whoisrecord(config, params):
    try:
        logger.error("Starting 'get_whoisrecord' operation with inputs: %s", params)
        microsoft_graph = SetupSession(config)
        graph_api_endpoint = '{0}/{1}'.format(microsoft_graph.ms.host, config.get('api_version'))
        logger.error("API endpoint constructed: %s", graph_api_endpoint)

        request_type = params.get('type')
        if request_type == "Host ID":
            url = f"{graph_api_endpoint}/security/threatIntelligence/hosts/{params.get('hostId')}/whois"
        elif request_type == "whoisRecord ID":
            url = f"{graph_api_endpoint}/security/threatIntelligence/whoisRecords/{params.get('whoisRecordId')}"
        else:
            raise ConnectorError("Invalid type specified. Must be 'Host ID' or 'whoisRecord ID'")

        logger.error("Constructed URL for WHOIS record request: %s", url)

        microsoft_graph.session.headers.pop('Prefer', '')
        response = microsoft_graph.session.get(url=url)
        microsoft_graph.session.close()

        if response.ok:
            logger.error("Received successful response with response: %s", response.json())
            return response.json()
        else:
            logger.error("Failed request: %s, Response: %s, Reason: %s", url, response.content, response.reason)
            raise ConnectorError(
                'Failed to request API {0} response is :{1} with reason: {2}'.format(str(url), str(response.content),
                                                                                   str(response.reason)))
    except Exception as e:
        logger.exception("Error in 'get_whoisrecord': %s", e)
        raise ConnectorError("Error in 'get_whoisrecord': {0}".format(e))


def list_components(config, params):
    try:
        logger.error("Starting 'get_host_reputation' operation with inputs: %s", params)
        microsoft_graph = SetupSession(config)
        graph_api_endpoint = '{0}/{1}'.format(microsoft_graph.ms.host, config.get('api_version'))
        logger.error("API endpoint constructed: %s", graph_api_endpoint)

        url = graph_api_endpoint + '/security/threatIntelligence/hosts/{0}/components'.format(params.get('hostId'))
        logger.error("Constructed URL for host reputation request: %s", url)

        microsoft_graph.session.headers.pop('Prefer', '')
        response = microsoft_graph.session.get(url=url)
        microsoft_graph.session.close()

        if response.ok:
            logger.error("Received successful response with response: %s", response.json())
            return response.json()
        else:
            logger.error("Failed request: %s, Response: %s, Reason: %s", url, response.content, response.reason)
            raise ConnectorError(
                'Failed to request API {0} response is :{1} with reason: {2}'.format(str(url), str(response.content),
                                                                                   str(response.reason)))
    except Exception as e:
        logger.exception("Error in 'get_host_reputation': %s", e)
        raise ConnectorError("Error in 'get_host_reputation': {0}".format(e))


def list_passiveDns(config, params):
    try:
        logger.error("Starting 'get_host_reputation' operation with inputs: %s", params)
        microsoft_graph = SetupSession(config)
        graph_api_endpoint = '{0}/{1}'.format(microsoft_graph.ms.host, config.get('api_version'))
        logger.error("API endpoint constructed: %s", graph_api_endpoint)

        url = graph_api_endpoint + '/security/threatIntelligence/hosts/{0}/passiveDns'.format(params.get('hostId'))
        logger.error("Constructed URL for host reputation request: %s", url)

        microsoft_graph.session.headers.pop('Prefer', '')
        response = microsoft_graph.session.get(url=url)
        microsoft_graph.session.close()

        if response.ok:
            logger.error("Received successful response with response: %s", response.json())
            return response.json()
        else:
            logger.error("Failed request: %s, Response: %s, Reason: %s", url, response.content, response.reason)
            raise ConnectorError(
                'Failed to request API {0} response is :{1} with reason: {2}'.format(str(url), str(response.content),
                                                                                   str(response.reason)))
    except Exception as e:
        logger.exception("Error in 'get_host_reputation': %s", e)
        raise ConnectorError("Error in 'get_host_reputation': {0}".format(e))


def list_passiveDns_reverse(config, params):
    try:
        logger.error("Starting 'get_host_reputation' operation with inputs: %s", params)
        microsoft_graph = SetupSession(config)
        graph_api_endpoint = '{0}/{1}'.format(microsoft_graph.ms.host, config.get('api_version'))
        logger.error("API endpoint constructed: %s", graph_api_endpoint)

        url = graph_api_endpoint + '/security/threatIntelligence/hosts/{0}/passiveDnsReverse'.format(params.get('hostId'))
        logger.error("Constructed URL for host reputation request: %s", url)

        microsoft_graph.session.headers.pop('Prefer', '')
        response = microsoft_graph.session.get(url=url)
        microsoft_graph.session.close()

        if response.ok:
            logger.error("Received successful response with response: %s", response.json())
            return response.json()
        else:
            logger.error("Failed request: %s, Response: %s, Reason: %s", url, response.content, response.reason)
            raise ConnectorError(
                'Failed to request API {0} response is :{1} with reason: {2}'.format(str(url), str(response.content),
                                                                                   str(response.reason)))
    except Exception as e:
        logger.exception("Error in 'get_host_reputation': %s", e)
        raise ConnectorError("Error in 'get_host_reputation': {0}".format(e))


def list_hostPorts(config, params):
    try:
        logger.error("Starting 'get_host_reputation' operation with inputs: %s", params)
        microsoft_graph = SetupSession(config)
        graph_api_endpoint = '{0}/{1}'.format(microsoft_graph.ms.host, config.get('api_version'))
        logger.error("API endpoint constructed: %s", graph_api_endpoint)

        url = graph_api_endpoint + '/security/threatIntelligence/hosts/{0}/ports'.format(params.get('hostId'))
        logger.error("Constructed URL for host reputation request: %s", url)

        microsoft_graph.session.headers.pop('Prefer', '')
        response = microsoft_graph.session.get(url=url)
        microsoft_graph.session.close()

        if response.ok:
            logger.error("Received successful response with response: %s", response.json())
            return response.json()
        else:
            logger.error("Failed request: %s, Response: %s, Reason: %s", url, response.content, response.reason)
            raise ConnectorError(
                'Failed to request API {0} response is :{1} with reason: {2}'.format(str(url), str(response.content),
                                                                                   str(response.reason)))
    except Exception as e:
        logger.exception("Error in 'get_host_reputation': %s", e)
        raise ConnectorError("Error in 'get_host_reputation': {0}".format(e))


def list_host_ssl_certificates(config, params):
    try:
        logger.error("Starting 'get_host_reputation' operation with inputs: %s", params)
        microsoft_graph = SetupSession(config)
        graph_api_endpoint = '{0}/{1}'.format(microsoft_graph.ms.host, config.get('api_version'))
        logger.error("API endpoint constructed: %s", graph_api_endpoint)

        url = graph_api_endpoint + '/security/threatIntelligence/hosts/{0}/sslCertificates'.format(params.get('hostId'))
        logger.error("Constructed URL for host reputation request: %s", url)

        microsoft_graph.session.headers.pop('Prefer', '')
        response = microsoft_graph.session.get(url=url)
        microsoft_graph.session.close()

        if response.ok:
            logger.error("Received successful response with response: %s", response.json())
            return response.json()
        else:
            logger.error("Failed request: %s, Response: %s, Reason: %s", url, response.content, response.reason)
            raise ConnectorError(
                'Failed to request API {0} response is :{1} with reason: {2}'.format(str(url), str(response.content),
                                                                                   str(response.reason)))
    except Exception as e:
        logger.exception("Error in 'get_host_reputation': %s", e)
        raise ConnectorError("Error in 'get_host_reputation': {0}".format(e))


def get_host_ssl_certificate(config, params):
    try:
        logger.error("Starting 'get_host_reputation' operation with inputs: %s", params)
        microsoft_graph = SetupSession(config)
        graph_api_endpoint = '{0}/{1}'.format(microsoft_graph.ms.host, config.get('api_version'))
        logger.error("API endpoint constructed: %s", graph_api_endpoint)

        url = graph_api_endpoint + '/security/threatIntelligence/hostSslCertificates/{0}'.format(params.get('hostSslCertificateId'))
        logger.error("Constructed URL for host reputation request: %s", url)

        microsoft_graph.session.headers.pop('Prefer', '')
        response = microsoft_graph.session.get(url=url)
        microsoft_graph.session.close()

        if response.ok:
            logger.error("Received successful response with response: %s", response.json())
            return response.json()
        else:
            logger.error("Failed request: %s, Response: %s, Reason: %s", url, response.content, response.reason)
            raise ConnectorError(
                'Failed to request API {0} response is :{1} with reason: {2}'.format(str(url), str(response.content),
                                                                                   str(response.reason)))
    except Exception as e:
        logger.exception("Error in 'get_host_reputation': %s", e)
        raise ConnectorError("Error in 'get_host_reputation': {0}".format(e))


def get_host_component(config, params):
    try:
        logger.error("Starting 'get_host_reputation' operation with inputs: %s", params)
        microsoft_graph = SetupSession(config)
        graph_api_endpoint = '{0}/{1}'.format(microsoft_graph.ms.host, config.get('api_version'))
        logger.error("API endpoint constructed: %s", graph_api_endpoint)

        url = graph_api_endpoint + '/security/threatIntelligence/hostComponents/{0}'.format(params.get('hostComponentId'))
        logger.error("Constructed URL for host reputation request: %s", url)

        microsoft_graph.session.headers.pop('Prefer', '')
        response = microsoft_graph.session.get(url=url)
        microsoft_graph.session.close()

        if response.ok:
            logger.error("Received successful response with response: %s", response.json())
            return response.json()
        else:
            logger.error("Failed request: %s, Response: %s, Reason: %s", url, response.content, response.reason)
            raise ConnectorError(
                'Failed to request API {0} response is :{1} with reason: {2}'.format(str(url), str(response.content),
                                                                                   str(response.reason)))
    except Exception as e:
        logger.exception("Error in 'get_host_reputation': %s", e)
        raise ConnectorError("Error in 'get_host_reputation': {0}".format(e))


def list_indicators(config, params):
    try:
        logger.error("Starting 'get_host_reputation' operation with inputs: %s", params)
        microsoft_graph = SetupSession(config)
        graph_api_endpoint = '{0}/{1}'.format(microsoft_graph.ms.host, config.get('api_version'))
        logger.error("API endpoint constructed: %s", graph_api_endpoint)

        url = graph_api_endpoint + '/security/threatIntelligence/intelProfiles/{0}/indicators'.format(params.get('intelligenceProfileId'))
        logger.error("Constructed URL for host reputation request: %s", url)

        microsoft_graph.session.headers.pop('Prefer', '')
        response = microsoft_graph.session.get(url=url)
        microsoft_graph.session.close()

        if response.ok:
            logger.error("Received successful response with response: %s", response.json())
            return response.json()
        else:
            logger.error("Failed request: %s, Response: %s, Reason: %s", url, response.content, response.reason)
            raise ConnectorError(
                'Failed to request API {0} response is :{1} with reason: {2}'.format(str(url), str(response.content),
                                                                                   str(response.reason)))
    except Exception as e:
        logger.exception("Error in 'get_host_reputation': %s", e)
        raise ConnectorError("Error in 'get_host_reputation': {0}".format(e))


def _check_health(config):
    if check(config, config.get('connector_info')):
        return True


operations = {
    'get_host_reputation': get_host_reputation,
    'get_host_details': get_host_details,
    'get_whoisrecord': get_whoisrecord,
    'list_components': list_components,
    'list_passiveDns': list_passiveDns,
    'list_passiveDns_reverse': list_passiveDns_reverse,
    'list_hostPorts': list_hostPorts,
    'list_host_ssl_certificates': list_host_ssl_certificates,
    'get_host_ssl_certificate': get_host_ssl_certificate,
    'get_host_component': get_host_component,
    'list_indicators': list_indicators,
}
