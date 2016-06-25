#!/usr/bin/python
# -*- coding: utf-8 -*-

# Ansible module to manage vmwarevcloudair docker machines
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
module: docker_machine_vmwarevcloudair
short_description: Create a vmwarevcloudair docker host machine using docker-machine
description:
  - Manage the life cycle of an VMWare VCloud Air docker machine
options:
  name:
    description:
      - Name of the managed docker-machine
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
  username:
    description:
      - required vCloud Air Username.
    default: null
    required: true
  password:
    description:
      - required vCloud Air Password.
    default: null
    required: true
  computeid:
    description:
      - Compute ID (if using Dedicated Cloud).
    default: null
    required: false
  vdcid:
    description:
      - Virtual Data Center ID.
    default: null
    required: false
  orgvdcnetwork:
    description:
      - Organization VDC Network to attach.
    default: null
    required: false
  edgegateway:
    description:
      - Organization Edge Gateway.
    default: null
    required: false
  publicip:
    description:
      - Org Public IP to use.
    default: null
    required: false
  catalog:
    description:
      - Catalog.
    default: null
    required: false
  catalogitem:
    description:
      - Catalog Item.
    default: null
    required: false
  provision:
    description:
      - Install Docker binaries.
    default: null
    required: false
  cpu_count:
    description:
      - VM CPU Count.
    default: null
    required: false
  memory_size:
    description:
      - VM Memory Size in MB.
    default: null
    required: false
  ssh_port:
    description:
      - SSH port.
    default: null
    required: false
  docker_port:
    description:
      - Docker port.
    default: null
    required: false

'''

from ansible.module_utils.docker_machine_common import *


def main():
    argument_spec = dict(
        username=dict(type='str', required=True),
        password=dict(type='str', required=True),
        computeid=dict(type='str'),
        vdcid=dict(type='str'),
        orgvdcnetwork=dict(type='str'),
        edgegateway=dict(type='str'),
        publicip=dict(type='str'),
        catalog=dict(type='str'),
        catalogitem=dict(type='str'),
        provision=dict(type='bool'),
        cpu_count=dict(type='int'),
        memory_size=dict(type='int'),
        ssh_port=dict(type='int'),
        docker_port=dict(type='int')
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

    MachineManager('vmwarevcloudair', machine, results)
    machine.module.exit_json(**results)


# import module snippets
from ansible.module_utils.basic import *

if __name__ == '__main__':
    main()
