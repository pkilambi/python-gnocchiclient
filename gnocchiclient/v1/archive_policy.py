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


CREATE_ATTR = [
    "name",
    "back_window",
    "definition",
]

UPDATE_ATTR = CREATE_ATTR + ["aggregation_methods"]


class ArchivePolicy(base.Resource):
    def __repr__(self):
        return "<ArchivePolicy %s>" % self._info

    def data(self, **kwargs):
        return self.manager.data(self, **kwargs)


class ArchivePolicyManager(base.Manager):
    resource_class = ArchivePolicy

    def list(self, **kwargs):
        path = '/v1/archive_policy'
        return self._list(path, 'archive_policy')

    def get(self, name):
        path = '/v1/archive_policy/%s' % name
        try:
            return self._list(path, expect_single=True)[0]
        except IndexError:
            return None

    def create(self, **kwargs):
        path = '/v1/archive_policy'
        new = dict((key, value) for (key, value) in kwargs.items()
                   if (key in UPDATE_ATTR))
        return self._create(path, new)

    def update(self, name, **kwargs):
        archive_policy = self.get(name)
        if archive_policy is None:
            raise exc.CommandError('ArchivePolicy not found: %s' % name)
        updated = archive_policy.to_dict()
        kwargs = dict((k, v) for k, v in kwargs.items()
                      if k in updated and (k in UPDATE_ATTR))
        utils.merge_nested_dict(updated, kwargs, depth=1)
        return self._update("/v1/archive_policy/%s" % name, updated)

    def delete(self, name):
        return self._delete('/v1/archive_policy/%s' % name)

