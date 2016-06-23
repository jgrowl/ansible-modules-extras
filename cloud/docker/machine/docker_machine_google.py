#!/usr/bin/python
# -*- coding: utf-8 -*-

# Ansible module to manage google docker machines
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
module: docker_machine_google
short_description: Create a google docker host machine using docker-machine
description:
  - Manage the life cycle of a Google Compute Engine docker machine
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
  project:
    description:
      - The id of your project to use when launching the instance.
    default: null
    required: true
  zone:
    description:
      - The zone to launch the instance.
    default: null
    required: false
  machine_type:
    description:
      - The type of instance.
    default: null
    required: false
  machine_image:
    description:
      - The absolute URL to a base VM image to instantiate.
    default: null
    required: false
  username:
    description:
      - The username to use for the instance.
    default: null
    required: false
  scopes:
    description:
      - 'The scopes for OAuth 2.0 to Access Google APIs.
        See [Google Compute Engine Doc](https://cloud.google.com/storage/docs/authentication).'
    default: null
    required: false
  disk_size:
    description:
      - The disk size of instance.
    default: null
    required: false
  disk_type:
    description:
      - The disk type of instance.
    default: null
    required: false
  address:
    description:
      - Instance's static external IP (name or IP).
    default: null
    required: false
  preemptible:
    description:
      - Instance preemptibility.
    default: null
    required: false
  tags:
    description:
      - Instance tags (comma-separated).
    default: null
    required: false
  use_internal_ip:
    description:
      - 'When this option is used during create it will make docker-machine use internal rather than public NATed IPs.
         The flag is persistent in the sense that a machine created with it retains the IP. It's useful for managing
         docker machines from another machine on the same network e.g. while deploying swarm.'
    default: null
    required: false
  use_internal_ip_only:
    description:
      - 'When this option is used during create, the new VM will not be assigned a public IP address. This is useful
         only when the host running `docker-machine` is located inside the Google Cloud infrastructure; otherwise,
         `docker-machine` can't reach the VM to provision the Docker daemon. The presence of this flag implies
         `use_internal_ip`.'
    default: null
    required: false
  use_existing:
    description:
      - 'Don't create a new VM, use an existing one. This is useful when you'd like to provision Docker on a VM you
         created yourself, maybe because it uses create options not supported by this driver.'
    default: null
    required: false
'''

from ansible.module_utils.docker_machine_common import *


def main():
    argument_spec = dict(
        project=dict(type='str', required=True),
        zone=dict(type='str'),
        machine_type=dict(type='str'),
        machine_image=dict(type='str'),
        username=dict(type='str'),
        scopes=dict(type='str'),
        disk_size=dict(type='str'),
        disk_type=dict(type='str'),
        address=dict(type='str'),
        preemptible=dict(type='str'),
        tags=dict(type='str'),
        use_internal_ip=dict(type='bool'),
        use_internal_ip_only=dict(type='bool'),
        use_existing=dict(type='bool')
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

    MachineManager('google', machine, results)
    machine.module.exit_json(**results)


# import module snippets
from ansible.module_utils.basic import *

if __name__ == '__main__':
    main()
