# Copyright 2012 OpenMetric LLC.
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

import six

from gnocchiclient.common import base


def _get_opt_path(simple_params=None, **kwargs):
    l = []
    simple_params = simple_params or []
    # get simple paramters
    for key in simple_params:
        val = kwargs.get(key)
        if val:
            l.append(key + '=' + val)
    # get metadata query paramters
    metaquery = kwargs.get('metaquery')
    if metaquery:
        l.extend(metaquery.split(':'))

    return '&'.join(l)


class Metric(base.Resource):
    def __repr__(self):
        return "<Metric %s>" % self._info

    def data(self, **kwargs):
        return self.manager.data(self, **kwargs)


class MetricManager(base.Manager):
    resource_class = Metric

    def list(self, **kwargs):
        opts_path = _get_opt_path(**kwargs)
        path = '/metric'
        if opts_path:
            path = '/v1%s?%s' % (path, opts_path)
        else:
            path = '/v1%s' % path
        return self._list(path, 'metric')
