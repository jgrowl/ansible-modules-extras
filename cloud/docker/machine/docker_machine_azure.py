#!/usr/bin/python
# -*- coding: utf-8 -*-

# Ansible module to manage azure docker machines
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
module: docker_machine_azure
short_description: Create a azure docker host machine using docker-machine
description:
     - Manage the life cycle of a Microsoft Azure docker machine
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
  subscription_id:
    description:
      - Your Azure Subscription ID
    default: null
    required: true
  image:
    description:
      - Azure virtual machine image in the format of Publisher:Offer:Sku:Version
    default: null
    required: false
  location:
    description:
      - Azure region to create the virtual machine.
    default: null
    required: false
  resource_group:
    description:
      - Azure Resource Group name to create the resources in.
    default: null
    required: false
  size:
    description:
      - Size for Azure Virtual Machine.
    default: null
    required: false
  ssh_user:
    description:
      - Username for SSH login.
    default: null
    required: false
  vnet:
    description:
      - Azure Virtual Network name to connect the virtual machine.
    default: null
    required: false
  subnet:
    description:
      - Azure Subnet Name to be used within the Virtual Network.
    default: null
    required: false
  subnet_prefix:
    description:
      - 'Private CIDR block. Used to create subnet if it does not exist. Must match in the case that the subnet does
         exist.'
    default: null
    required: false
  availability_set:
    description:
      - Azure Availability Set to place the virtual machine into.
    default: null
    required: false
  open_port:
    description:
      - Make additional port number(s) accessible from the Internet [?]
    default: null
    required: false
  private_ip_address:
    description:
      - Specify a static private IP address for the machine.
    default: null
    required: false
  use_private_ip:
    description:
      - 'Use private IP address of the machine to connect. It’s useful for managing Docker machines from another machine
         on the same network e.g. while deploying Swarm.'
    default: null
    required: false
  no_public_ip:
    description:
      - 'Do not create a public IP address for the machine (implies use-private-ip). Should be used only when creating
         machines from an Azure VM within the same subnet.'
    default: null
    required: false
  static_public_ip:
    description:
      - Assign a static public IP address to the machine.
    default: null
    required: false
  docker_port:
    description:
      - Port number for Docker engine.
    default: null
    required: false
  environment:
    description:
      - Azure environment (e.g. AzurePublicCloud, AzureChinaCloud).
    default: null
    required: false
'''

from ansible.module_utils.docker_machine_common import *


def main():
    argument_spec = dict(
        subscription_id=dict(type='str', required=True),
        location=dict(type='str'),
        resource_group=dict(type='str'),
        size=dict(type='str'),
        ssh_user=dict(type='str'),
        vnet=dict(type='str'),
        subnet=dict(type='str'),
        subnet_prefix=dict(type='str'),
        availability_set=dict(type='str'),
        open_port=dict(type='str'),
        private_ip_address=dict(type='str'),
        use_private_ip=dict(type='bool'),
        no_public_ip=dict(type='bool'),
        static_public_ip=dict(type='string'),
        docker_port=dict(type='int'),
        environment=dict(type='str'),
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

    MachineManager('azure', machine, results)
    machine.module.exit_json(**results)


# import module snippets
from ansible.module_utils.basic import *

if __name__ == '__main__':
    main()
