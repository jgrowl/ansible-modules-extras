#!/usr/bin/python
# -*- coding: utf-8 -*-

# Ansible module to manage softlayer docker machines
# (c) 2016, Jonathan Rowlands <jonrowlands83@gmail.com>
#
# This file is part of Ansible
#
# Ansible is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Ansible is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Ansible.  If not, see <http://www.gnu.org/licenses/>.

DOCUMENTATION = '''
---
module: docker_machine_softlayer
short_description: Create a softlayer docker host machine using docker-machine
description:
  - Manage the life cycle of an IBM Softlayer docker machine
options:
  name:
    description:
      -
  state:
    description:
      - 'I(absent) - A machine matching the specified name will be stopped and removed.'
      - 'I(present)" - Asserts the existence of a machine matching the name and any provided configuration parameters.
         If no machine matches the name, a container will be created. If a machine matches the name but the provided
         configuration does not match, the machine will be updated, if it can be. If it cannot be updated, it will be
         removed and re-created with the requested config. Use the recreate option to force the re-creation of the
         matching machine.'
      - 'I(started) - Asserts there is a running machine matching the name and any provided configuration. If no machine
         matches the name, a machine will be created and started. If a container matching the name is found but the
         configuration does not match, the container will be updated, if it can be. If it cannot be updated, it will be
         removed and a new container will be created with the requested configuration and started. Use recreate to
         always re-create a matching container, even if it is running. Use restart to force a matching machine to be
         stopped and restarted.'
      - 'I(stopped) - Asserts that the machine is first I(present), and then if the machine is running moves it to a
         stopped state.'
    required: false
    default: started
    choices:
      - absent
      - present
      - stopped
      - started
  memory:
    description:
      - Memory for host in MB.
    default: null
    required: false
  disk_size:
    description:
      - A value of 0 will set the SoftLayer default.
    default: null
    required: false
  user:
    description:
      - Username for your SoftLayer account, api key needs to match this user.
    default: null
    required: true
  api_key:
    description:
      - API key for your user account.
    default: null
    required: true
  region:
    description:
      - SoftLayer region.
    default: null
    required: false
  cpu:
    description:
      - Number of CPUs for the machine.
    default: null
    required: false
  hostname:
    description:
      - Hostname for the machine.
    default: null
    required: false
  domain:
    description:
      - Domain name for the machine.
    default: null
    required: true
  api_endpoint:
    description:
      - Change SoftLayer API endpoint.
    default: null
    required: false
  hourly_billing:
    description:
      - Specifies that hourly billing should be used, otherwise monthly billing is used.
    default: null
    required: false
  local_disk:
    description:
      - Use local machine disk instead of SoftLayer SAN.
    default: null
    required: false
  private_net_only:
    description:
      - Disable public networking.
    default: null
    required: false
  image:
    description:
      - OS Image to use.
    default: null
    required: false
  public_vlan_id:
    description:
      - Your public VLAN ID.
    default: null
    required: false
  private_vlan_id:
    description:
      - Your private VLAN ID.
    default: null
    required: false
'''

from ansible.module_utils.docker_machine_common import *


def main():
    argument_spec = dict(
        user=dict(type='str', required=True),
        api_key=dict(type='str', required=True),
        domain=dict(type='str', required=True),
        memory=dict(type='str'),
        disk_size=dict(type='str'),
        region=dict(type='str'),
        cpu=dict(type='str'),
        hostname=dict(type='str'),
        api_endpoint=dict(type='str'),
        hourly_billing=dict(type='str'),
        local_disk=dict(type='str'),
        private_net_only=dict(type='str'),
        image=dict(type='str'),
        public_vlan_id=dict(type='str'),
        private_vlan_id=dict(type='str')
    )

    machine = AnsibleDockerMachine(
            argument_spec=argument_spec,
            supports_check_mode=True,
    )

    results = dict(
            changed=False,
            actions=[],
            machine={}
    )

    MachineManager('softlayer', machine, results)
    machine.module.exit_json(**results)


# import module snippets
from ansible.module_utils.basic import *

if __name__ == '__main__':
    main()
