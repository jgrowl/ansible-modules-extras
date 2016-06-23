#!/usr/bin/python
# -*- coding: utf-8 -*-

# Ansible module to manage amazonec2 docker machines
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
module: docker_machine_amazonec2
short_description: Create a amazonec2 docker host machine using docker-machine
description:
     - Manage the life cycle of an Amazon EC2 docker machine
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
  access_key:
    description:
      - Your access key id for the Amazon Web Services API.
    default: null
    required: true
  secret_key:
    description:
      - Your secret access key for the Amazon Web Services API.
    default: null
    required: true
  session_token:
    description:
      - Your session token for the Amazon Web Services API.
    default: null
    required: false
  ami:
    description:
      - The AMI ID of the instance to use.
    default: null
    required: false
  region:
    description:
      - The region to use when launching the instance.
    default: null
    required: false
  vpc_id:
    description:
      - Your VPC ID to launch the instance in.
    default: null
    required: false
  zone:
    description:
      - The AWS zone to launch the instance in (i.e. one of a,b,c,d,e).
    default: null
    required: false
  subnet_id:
    description:
      - AWS VPC subnet id.
    default: null
    required: false
  security_group:
    description:
      - AWS VPC security group name.
    default: null
    required: false
  tags:
    description:
      - AWS extra tag key-value pairs (comma-separated, e.g. key1,value1,key2,value2).
    default: null
    required: false
  instance_type:
    description:
      - The instance type to run.
    default: null
    required: false
  device_name:
    description:
      - The root device name of the instance.
    default: null
    required: false
  root_size:
    description:
      - The root disk size of the instance (in GB).
    default: null
    required: false
  volume_type:
    description:
      - The Amazon EBS volume type to be attached to the instance.
    default: null
    required: false
  iam_instance_profile:
    description:
      - The AWS IAM role name to be used as the instance profile.
    default: null
    required: false
  ssh_user:
    description:
      - The SSH Login username, which must match the default SSH user set in the ami used.
    default: null
    required: false
  request_spot_instance:
    description:
      - Use spot instances.
    default: null
    required: false
  spot_price:
    description:
      - Spot instance bid price (in dollars). Require the --amazonec2-request-spot-instance flag.
    default: null
    required: false
  use_private_address:
    description:
      - Use the private IP address for docker-machine, but still create a public IP address.
    default: null
    required: false
  private_address_only:
    description:
      - Use the private IP address only.
    default: null
    required: false
  monitoring:
    description:
      - Enable CloudWatch Monitoring.
    default: null
    required: false
  use_ebs_optimized_instance:
    description:
      - Create an EBS Optimized Instance, instance type must support it.
    default: null
    required: false
  ssh_keypath:
    description:
      - Path to Private Key file to use for instance. Matching public key with .pub extension should exist
    default: null
    required: false
  retries:
    description:
      - Set retry count for recoverable failures (use -1 to disable)
    default: null
    required: false

'''

from ansible.module_utils.docker_machine_common import *


def main():
    argument_spec = dict(
        access_key=dict(type='str', required=True),
        secret_key=dict(type='str', required=True),
        session_token=dict(type='str'),
        ami=dict(type='str'),
        region=dict(type='str'),
        vpc_id=dict(type='str', required=True),
        zone=dict(type='str'),
        subnet_id=dict(type='str'),
        security_group=dict(type='str'),
        tags=dict(type='str'),
        instance_type=dict(type='str'),
        device_name=dict(type='str'),
        root_size=dict(type='str'),
        volume_type=dict(type='str'),
        iam_instance_profile=dict(type='str'),
        ssh_user=dict(type='str'),
        request_spot_instance=dict(type='bool'),
        spot_price=dict(type='str'),
        use_private_address=dict(type='bool'),
        private_address_only=dict(type='bool'),
        monitoring=dict(type='bool'),
        use_ebs_optimized_instance=dict(type='bool'),
        ssh_keypath=dict(type='string'),
        retries=dict(type='int'),
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

    MachineManager('amazonec2', machine, results)
    machine.module.exit_json(**results)


# import module snippets
from ansible.module_utils.basic import *

if __name__ == '__main__':
    main()
