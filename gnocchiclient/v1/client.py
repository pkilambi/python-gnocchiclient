# Copyright 2012 OpenStack Foundation
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.


from gnocchiclient import client as gnocchi_client
from gnocchiclient.openstack.common.apiclient import client
from gnocchiclient.v1 import metric
from gnocchiclient.v1 import archive_policy


class Client(object):
    """Client for the Gnocchi v1 API.

    :param string endpoint: A user-supplied endpoint URL for the gnocchi
                            service.
    :param function token: Provides token for authentication.
    :param integer timeout: Allows customization of the timeout for client
                            http requests. (optional)
    """

    def __init__(self, *args, **kwargs):
        """Initialize a new client for the Gnocchi v1 API."""
        self.auth_plugin = kwargs.get('auth_plugin') \
            or gnocchi_client.get_auth_plugin(*args, **kwargs)
        self.client = client.HTTPClient(
            auth_plugin=self.auth_plugin,
            region_name=kwargs.get('region_name'),
            endpoint_type=kwargs.get('endpoint_type'),
            original_ip=kwargs.get('original_ip'),
            verify=kwargs.get('verify'),
            cert=kwargs.get('cert'),
            timeout=kwargs.get('timeout'),
            timings=kwargs.get('timings'),
            keyring_saver=kwargs.get('keyring_saver'),
            debug=kwargs.get('debug'),
            user_agent=kwargs.get('user_agent'),
            http=kwargs.get('http')
        )

        self.http_client = client.BaseClient(self.client)
        self.metrics = metric.MetricManager(self.http_client)
        self.archive_policy = archive_policy.ArchivePolicyManager(self.http_client)
