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
short_description: Create a openstack docker host machine using docker-machine
'''

from ansible.module_utils.docker_machine_common import *


def main():
    argument_spec = dict(
        auth_url=dict(type='str'),
        flavor_name=dict(type='str'),
        flavor_id=dict(type='str'),
        image_name=dict(type='str'),
        image_id=dict(type='str'),
        insecure=dict(type='str'),
        domain_name=dict(type='str'),
        domain_id=dict(type='str'),
        username=dict(type='str'),
        password=dict(type='str'),
        tenant_name=dict(type='str'),
        tenant_id=dict(type='str'),
        region=dict(type='str'),
        availability_zone=dict(type='str'),
        endpoint_type=dict(type='str'),
        net_name=dict(type='str'),
        net_id=dict(type='str'),
        sec_groups=dict(type='str'),
        floatingip_pool=dict(type='str'),
        ip_version=dict(type='str'),
        ssh_user=dict(type='str'),
        ssh_port=dict(type='str'),
        active_timeout=dict(type='str')
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

    MachineManager('openstack', machine, results)
    machine.module.exit_json(**results)


# import module snippets
from ansible.module_utils.basic import *

if __name__ == '__main__':
    main()
