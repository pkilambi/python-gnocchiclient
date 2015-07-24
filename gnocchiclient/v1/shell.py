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

from gnocchiclient.common import utils
import gnocchiclient.exc as exc


def do_metric_list(cc, args={}):
    """List metrics."""
    meters = cc.metrics.list()
    field_labels = ['Archive Policy Name', 'Name', 'Metric ID', 'User ID', 'Project ID']
    fields = ['archive_policy_name', 'name', 'id',
              'created_by_user_id', 'created_by_project_id']
    utils.print_list(meters, fields, field_labels,
                     sortby=0)


def do_archive_policy_list(cc, args={}):
    """List archive policy """
    aps = cc.archive_policy.list()
    field_labels = ['Name', 'Aggregation methods', 'Back Window', 'Definition']
    fields = ['name', 'aggregation_methods', 'back_window', 'definition']
    utils.print_list(aps, fields, field_labels,
                     sortby=0)
