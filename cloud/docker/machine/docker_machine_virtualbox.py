#!/usr/bin/python
# -*- coding: utf-8 -*-

# Ansible module to manage virtualbox docker machines
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
module: docker_machine_virtualbox
short_description: Create an Oracle VirtualBox docker host machine using docker-machine
description:
  - Manage the life cycle of a Oracle VirtualBox docker machine
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
  memory:
    description:
      - Size of memory for the host in MB.
    default: null
    required: false
  cpu_count:
    description:
      - Number of CPUs to use to create the VM. Defaults to single CPU.
    default: null
    required: false
  disk_size:
    description:
      - Size of disk for the host in MB.
    default: null
    required: false
  host_dns_resolver:
    description:
      - Use the host DNS resolver. (Boolean value, defaults to false)
    default: null
    required: false
  boot2docker_url:
    description:
      - The URL of the boot2docker image. Defaults to the latest available version.
    default: null
    required: false
  import_boot2docker_vm:
    description:
      - The name of a Boot2Docker VM to import.
    default: null
    required: false
  hostonly_cidr:
    description:
      - The CIDR of the host only adapter.
    default: null
    required: false
  hostonly_nictype:
    description:
      - 'Host Only Network Adapter Type. Possible values are are ‘82540EM’ (Intel PRO/1000), ‘Am79C973’ (PCnet-FAST III)
         and ‘virtio’ Paravirtualized network adapter.'
    default: null
    required: false
  hostonly_nicpromisc:
    description:
      - Host Only Network Adapter Promiscuous Mode. Possible options are deny , allow-vms, allow-all
    default: null
    required: false
  no_share:
    description:
      - Disable the mount of your home directory
    default: null
    required: false
  no_dns_proxy:
    description:
      - Disable proxying all DNS requests to the host (Boolean value, default to false)
    default: null
    required: false
  no_vtx_check:
    description:
      - Disable checking for the availability of hardware virtualization before the vm is started
    default: null
    required: false
'''

from ansible.module_utils.docker_machine_common import *


def main():
    argument_spec = dict(
        memory=dict(type='int'),
        cpu_count=dict(type='int'),
        disk_size=dict(type='int'),
        host_dns_resolver=dict(type='bool'),
        boot2docker_url=dict(type='str'),
        import_boot2docker_vm=dict(type='str'),
        hostonly_cidr=dict(type='str'),
        hostonly_nictype=dict(type='str'),
        hostonly_nicpromisc=dict(type='str'),
        no_share=dict(type='bool'),
        no_dns_proxy=dict(type='bool'),
        no_vtx_check=dict(type='bool')
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

    MachineManager('virtualbox', machine, results)
    machine.module.exit_json(**results)


# import module snippets
from ansible.module_utils.basic import *

if __name__ == '__main__':
    main()
