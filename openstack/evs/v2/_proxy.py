# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.
from openstack import proxy2
from openstack.evs.v2 import volume as _volume
from openstack.evs.v2 import volume_ext as _volume_ext


class Proxy(proxy2.BaseProxy):
    # def create_volume(self, **attrs):
    #     """Create a new volume from attributes
    #
    #     :param dict attrs: Keyword arguments which will be used to create
    #                        a :class:`~openstack.evs.v2.volume.Volume`,
    #                        comprised of the properties on the Volume class.
    #
    #     :returns: The results of volume creation
    #     :rtype: :class:`~openstack.evs.v2.volume.Volume`
    #     """
    #     return self._create(_volume.Vloume, **attrs)
    #
    # def resize_volume(self, volume_id, **data):
    #     """
    #     post method to modify volume size
    #     :param volume_id: EVS volume_id
    #     :param data:
    #     :return: class:`~openstack.evs.v2.volume.ResizeVloume`
    #     """
    #     return self._create(_volume.ResizeVloume, volume_id=volume_id, **data)

    def create_volume_ext(self, **attrs):
        """Create a new volume from attributes

        :param dict attrs: Keyword arguments which will be used to create
                           a :class:`~openstack.evs.v2.volume_ext.Volume`,
                           comprised of the properties on the Volume class.

        :returns: The results of volume creation
        :rtype: :class:`~openstack.evs.v2.volume_ext.Volume`
        """
        return self._create(_volume_ext.VloumeExt, **attrs)

    def resize_volume_ext(self, volume_id, **data):
        """
        post method to modify volume size
        :param volume_id: EVS volume_id
        :param data:
        :return: class:`~openstack.evs.v2.volume_ext.ResizeVloume`
        """
        return self._create(_volume_ext.ResizeVloume, volume_id=volume_id, **data)
