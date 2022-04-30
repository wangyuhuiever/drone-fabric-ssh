# -*- coding: utf-8 -*-
from settings import load_from_envs
from fabric import Connection


def run():
    configs = load_from_envs()
    connect_value = {
        'inline_ssh_env': True,
        'host': configs.get('host'),
        'user': configs.get('username'),
        'port': configs.get('port') or 22,
    }
    if configs.get('password'):
        connect_value.update({
            'connect_kwargs': {
                'password': configs.get('password')
            }
        })

    scripts = configs.get('scripts')
    envs = configs.get('envs', {})
    # some value with special character may cause set env failed, so mandatory add '
    for key, value in envs.items():
        envs.update({key: "\'" + value + "\'"})
    with Connection(**connect_value) as client:
        for script in scripts:
            result = client.run(script, hide=True, env=envs)
            print('execute [%s] on [%s]' % (result.command, result.connection.host))
            print('result')
            print(result.stdout)
