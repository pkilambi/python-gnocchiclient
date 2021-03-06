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


from gnocchiclient.common import base
from gnocchiclient.common import utils
import gnocchiclient.exc as exc


UPDATE_ATTR = [
    "archive_policy_name"
]

class Metric(base.Resource):
    def __repr__(self):
        return "<Metric %s>" % self._info

    def data(self, **kwargs):
        return self.manager.data(self, **kwargs)


class MetricManager(base.Manager):
    resource_class = Metric

    def list(self):
        path = '/v1/metric'
        return self._list(path, 'metric')

    def get(self, metric_id):
        path = '/v1/metric/%s' % metric_id
        try:
            return self._list(path, expect_single=True)[0]
        except IndexError:
            return None

    def create(self, **kwargs):
        path = '/v1/metric'
        new = dict((key, value) for (key, value) in kwargs.items()
                   if (key in UPDATE_ATTR))
        return self._create(path, new)

    def update(self, id, **kwargs):
        metric = self.get(id)
        if metric is None:
            raise exc.CommandError('Metric not found: %s' % id)
        updated = metric.to_dict()
        kwargs = dict((k, v) for k, v in kwargs.items()
                      if k in updated and (k in UPDATE_ATTR))
        utils.merge_nested_dict(updated, kwargs, depth=1)
        return self._update("/v1/metric/%s" % id, updated)


