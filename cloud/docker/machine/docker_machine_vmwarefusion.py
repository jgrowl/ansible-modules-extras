#!/usr/bin/python
# -*- coding: utf-8 -*-

# Ansible module to manage vmwarefusion docker machines
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
module: docker_machine_vmwarefusion
short_description: Create a VMWare Fusion docker host machine using docker-machine
description:
  - Manage the life cycle of an VMWare Fusion docker machine
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
  boot2docker_url:
    description:
      - URL for boot2docker image.
    default: null
    required: false
  cpu_count:
    description:
      - Number of CPUs for the machine (-1 to use the number of CPUs available)
    default: null
    required: false
  disk_size:
    description:
      - Size of disk for host VM (in MB).
    default: null
    required: false
  memory_size:
    description:
      - Size of memory for host VM (in MB).
    default: null
    required: false
  no_share:
    description:
      - Disable the mount of your home directory.
    default: null
    required: false

'''

from ansible.module_utils.docker_machine_common import *


def main():
    argument_spec = dict(
        boot2docker_url=dict(type='str'),
        cpu_count=dict(type='int'),
        disk_size=dict(type='int'),
        memory_size=dict(type='int'),
        no_share=dict(type='bool')
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

    MachineManager('vmwarefusion', machine, results)
    machine.module.exit_json(**results)


# import module snippets
from ansible.module_utils.basic import *

if __name__ == '__main__':
    main()
