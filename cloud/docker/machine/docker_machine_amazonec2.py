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
'''

from ansible.module_utils.docker_machine_common import *


def main():
    argument_spec = dict(
        access_key=dict(type='str', required=True),
        secret_key=dict(type='str', required=True),
        vpc_id=dict(type='str', required=True),
        session_token=dict(type='str'),
        ami=dict(type='str'),
        region=dict(type='str'),
        zone=dict(type='str'),
        subnet_id=dict(type='str'),
        security_group=dict(type='str'),
        instance_type=dict(type='str'),
        root_size=dict(type='str'),
        iam_instance_profile=dict(type='str'),
        ssh_user=dict(type='str'),
        request_spot_instance=dict(type='bool'),
        spot_price=dict(type='str'),
        private_address_only=dict(type='bool'),
        monitoring=dict(type='bool')
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
