#!/usr/bin/python
# -*- coding: utf-8 -*-

# Ansible module to manage vmwarevsphere docker machines
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
module: docker_machine_vmwarevsphere
short_description: Create a VMWare vSphere docker host machine using docker-machine
description:
  - Manage the life cycle of an VMWare vSphere docker machine
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
      - required vSphere Username.
    default: null
    required: true
  password:
    description:
      - vSphere Password.
    default: null
    required: true
  cpu_count:
    description:
      - CPU number for Docker VM.
    default: null
    required: false
  memory_size:
    description:
      - Size of memory for Docker VM (in MB).
    default: null
    required: false
  disk_size:
    description:
      - Size of disk for Docker VM (in MB).
    default: null
    required: false
  boot2docker_url:
    description:
      - URL for boot2docker image.
    default: null
    required: false
  vcenter:
    description:
      - IP/hostname for vCenter (or ESXi if connecting directly to a single host).
    default: null
    required: false
  vcenter_port:
    description:
      - vSphere Port for vCenter.
    default: null
    required: false
  network:
    description:
      - Network where the Docker VM will be attached.
    default: null
    required: false
  datastore:
    description:
      - Datastore for Docker VM.
    default: null
    required: false
  datacenter:
    description:
      - Datacenter for Docker VM (must be set to ha-datacenter when connecting to a single host).
    default: null
    required: false
  pool:
    description:
      - Resource pool for Docker VM.
    default: null
    required: false
  hostsystem:
    description:
      - vSphere compute resource where the docker VM will be instantiated (use /* or / if using a cluster).
    default: null
    required: false
'''

from ansible.module_utils.docker_machine_common import *


def main():
    argument_spec = dict(
        username=dict(type='str', required=True),
        password=dict(type='str', required=True),
        cpu_count=dict(type='int'),
        memory_size=dict(type='int'),
        boot2docker_url=dict(type='str'),
        vcenter=dict(type='str'),
        vcenter_port=dict(type='int'),
        disk_size=dict(type='int'),
        network=dict(type='str'),
        datastore=dict(type='str'),
        datacenter=dict(type='str'),
        pool=dict(type='str'),
        hostsystem=dict(type='str')
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

    MachineManager('vmwarevsphere', machine, results)
    machine.module.exit_json(**results)


# import module snippets
from ansible.module_utils.basic import *

if __name__ == '__main__':
    main()
