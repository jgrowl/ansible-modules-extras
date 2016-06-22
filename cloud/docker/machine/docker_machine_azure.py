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
