#!/usr/bin/python
# -*- coding: utf-8 -*-

# Ansible module to manage openstack docker machines
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
module: docker_machine_openstack
short_description: Create an Openstack docker host machine using docker-machine
description:
  - Manage the life cycle of an OpenStack docker machine
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
  auth_url:
    description:
      - Keystone service base URL.
    default: null
    required: false
  flavor_id:
    description:
      - Identify the flavor that will be used for the machine.
    default: null
    required: false
  flavor_name:
    description:
      - The flavor that will be used for the machine.
    default: null
    required: false
  image_id:
    description:
      - Identify the image that will be used for the machine.
    default: null
    required: false
  image_name:
    description:
      - Identify the image that will be used for the machine.
    default: null
    required: false
  active_timeout:
    description:
      - The timeout in seconds until the OpenStack instance must be active.
    default: null
    required: false
  availability_zone:
    description:
      - The availability zone in which to launch the server.
    default: null
    required: false
  domain_name:
    description:
      - Domain to use for authentication (Keystone v3 only).
    default: null
    required: false
  domain_id:
    description:
      - Domain to use for authentication (Keystone v3 only).
    default: null
    required: false
  endpoint_type:
    description:
      - 'Endpoint type can be internalURL, adminURL on publicURL. If is a helper for the driver to choose the right URL
         in the OpenStack service catalog. If not provided the default id publicURL'
    default: null
    required: false
  floatingip_pool:
    description:
      - 'The IP pool that will be used to get a public IP can assign it to the machine. If there is an IP address
         already allocated but not assigned to any machine, this IP will be chosen and assigned to the machine. If there
         is no IP address already allocated a new IP will be allocated and assigned to the machine.'
    default: null
    required: false
  keypair_name:
    description:
      - Specify the existing Nova keypair to use.
    default: null
    required: false
  insecure:
    description:
      - 'Explicitly allow openstack driver to perform “insecure” SSL (https) requests. The server’s certificate will not
         be verified against any certificate authorities. This option should be used with caution.'
    default: null
    required: false
  ip_version:
    description:
      - If the instance has both IPv4 and IPv6 address, you can select IP version. If not provided 4 will be used.
    default: null
    required: false
  net_name:
    description:
      - 'Identify the private network the machine will be connected on. If your OpenStack project project contains only
         one private network it will be use automatically.'
    default: null
    required: false
  net-id:
    description:
      - 'Identify the private network the machine will be connected on. If your OpenStack project project contains only
         one private network it will be use automatically.'
    default: null
    required: false
  password:
    description:
      -  User password. It can be omitted if the standard environment variable OS_PASSWORD is set.
    default: null
    required: false
  private_key_file:
    description:
      - Used with --openstack-keypair-name, associates the private key to the keypair.
    default: null
    required: false
  region:
    description:
      - The region to work on. Can be omitted if there is only one region on the OpenStack.
    default: null
    required: false
  sec_groups:
    description:
      - 'If security groups are available on your OpenStack you can specify a comma separated list to use for the
         machine (e.g. secgrp001,secgrp002).'
    default: null
    required: false
  username:
    description:
      - User identifier to authenticate with.
    default: null
    required: false
  ssh_port:
    description:
      - Customize the SSH port if the SSH server on the machine does not listen on the default port.
    default: null
    required: false
  ssh_user:
    description:
      - The username to use for SSH into the machine. If not provided root will be used.
    default: null
    required: false
  tenant_name:
    description:
      - Identify the tenant in which the machine will be created.
    default: null
    required: false
  tenant-id:
    description:
      - Identify the tenant in which the machine will be created.
    default: null
    required: false
'''

from ansible.module_utils.docker_machine_common import *


def main():
    argument_spec = dict(
        auth_url=dict(type='str', required=True),
        # TODO: Either id or name is required, but not both for flavor
        flavor_id=dict(type='str'),
        flavor_name=dict(type='str'),
        # TODO: Either id or name is required, but not both for image.
        image_id=dict(type='str'),
        image_name=dict(type='str'),
        active_timeout=dict(type='str'),
        availability_zone=dict(type='str'),
        domain_id=dict(type='str'),
        domain_name=dict(type='str'),
        endpoint_type=dict(type='str'),
        floatingip_pool=dict(type='str'),
        keypair_name=dict(type='str'),
        insecure=dict(type='str'),
        ip_version=dict(type='str'),
        net_id=dict(type='str'),
        net_name=dict(type='str'),
        password=dict(type='str'),
        private_key_file=dict(type='str'),
        region=dict(type='str'),
        sec_groups=dict(type='str'),
        username=dict(type='str'),
        ssh_port=dict(type='str'),
        ssh_user=dict(type='str'),
        tenant_id=dict(type='str'),
        tenant_name=dict(type='str')
    )

    mutually_exclusive = [
        ['flavor_id', 'flavor_name'],
        ['image_id', 'image_name']
        ['domain_id', 'domain_name'],
        ['net_id', 'net_name'],
        ['tenant_id', 'tenant_name']
    ]

    machine = AnsibleDockerMachine(
            argument_spec=argument_spec,
            supports_check_mode=True,
            mutually_exclusive=mutually_exclusive
    )

    results = dict(
            changed=False,
            actions=[],
            machine={}
    )

    MachineManager('openstack', machine, results)
    machine.module.exit_json(**results)


# import module snippets
from ansible.module_utils.basic import *

if __name__ == '__main__':
    main()
