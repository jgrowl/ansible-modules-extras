#!/usr/bin/python
# -*- coding: utf-8 -*-

# Ansible module to manage digitalocean docker machines
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
module: docker_machine_digitalocean
short_description: Create a digitalocean docker host machine using docker-machine
'''

from ansible.module_utils.docker_machine_common import *


def main():
    argument_spec = dict(
        access_token=dict(type='str'),
        image=dict(type='str'),
        # TODO: support all regions, ideally use external all to get all choices
        # , choices=['nyc3']
        region=dict(type='str'),
        size=dict(type='str'),
        ipv6=dict(type='bool'),
        private_networking=dict(type='bool'),
        backups=dict(type='bool'),
        userdata=dict(type='str'),
        ssh_user=dict(type='str'),
        ssh_port=dict(type='str'),
        ssh_key_fingerprint=dict(type='str')
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

    MachineManager('digitalocean', machine, results)
    machine.module.exit_json(**results)


# import module snippets
from ansible.module_utils.basic import *

if __name__ == '__main__':
    main()
