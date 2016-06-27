#!/usr/bin/python
# -*- coding: utf-8 -*-

# Ansible module to manage docker machines
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
module: docker_machine_rackspace
short_description: Create a Rackspace docker host machine using docker-machine
description:
  - Manage the life cycle of a Rackspace docker machine
version_added: "2.2"
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
      - Rackspace account username.
    default: null
    required: true
  api_key:
    description:
      - Rackspace API key.
    default: null
    required: true
  region:
    description:
      - Rackspace region name.
    default: null
    required: true
  endpoint_type:
    description:
      - Rackspace endpoint type (adminURL, internalURL or the default publicURL).
    default: null
    required: false
  image_id:
    description:
      -Rackspace image ID. Default: Ubuntu 15.10 (Wily Werewolf) (PVHVM).
    default: null
    required: false
  flavor_id:
    description:
      - Rackspace flavor ID. Default: General Purpose 1GB.
    default: null
    required: false
  ssh_user:
    description:
      - SSH user for the newly booted machine.
    default: null
    required: false
  ssh_port:
    description:
      - SSH port for the newly booted machine.
    default: null
    required: false
  docker_install:
    description:
      - Set if Docker has to be installed on the machine.
    default: null
    required: false
'''

from ansible.module_utils.docker_machine_common import *


def main():
    argument_spec = dict(
        username=dict(type='str', required=True),
        api_key=dict(type='str', required=True),
        region=dict(type='str', required=True),
        endpoint_type=dict(type='str'),
        image_id=dict(type='str'),
        flavor_id=dict(type='str'),
        ssh_user=dict(type='str'),
        ssh_port=dict(type='str'),
        docker_install=dict(type='str')
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

    MachineManager('rackspace', machine, results)
    machine.module.exit_json(**results)


# import module snippets
from ansible.module_utils.basic import *

if __name__ == '__main__':
    main()
