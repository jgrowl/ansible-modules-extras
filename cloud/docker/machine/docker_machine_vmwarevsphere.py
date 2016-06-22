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
short_description: Create a vmwarevsphere docker host machine using docker-machine
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
