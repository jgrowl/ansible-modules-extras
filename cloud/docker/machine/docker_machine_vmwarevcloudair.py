#!/usr/bin/python
# -*- coding: utf-8 -*-

# Ansible module to manage vmwarevcloudair docker machines
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
module: docker_machine_vmwarevcloudair
short_description: Create a vmwarevcloudair docker host machine using docker-machine
'''

from ansible.module_utils.docker_machine_common import *


def main():
    argument_spec = dict(
        username=dict(type='str', required=True),
        password=dict(type='str', required=True),
        computeid=dict(type='str'),
        vdcid=dict(type='str'),
        orgvdcnetwork=dict(type='str'),
        edgegateway=dict(type='str'),
        publicip=dict(type='str'),
        catalog=dict(type='str'),
        catalogitem=dict(type='str'),
        provision=dict(type='bool'),
        cpu_count=dict(type='int'),
        memory_size=dict(type='int'),
        ssh_port=dict(type='int'),
        docker_port=dict(type='int')
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

    MachineManager('vmwarevcloudair', machine, results)
    machine.module.exit_json(**results)


# import module snippets
from ansible.module_utils.basic import *

if __name__ == '__main__':
    main()
