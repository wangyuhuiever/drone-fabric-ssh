# -*- coding: utf-8 -*-
import os


def load_from_envs():
    configs = {
        'envs': {}
    }
    print('input values')
    print('------------')
    for key, value in os.environ.items():
        if key == 'PLUGIN_ENVS':
            print(value)
            for v in value:
                configs['envs'].update(v)
        elif key.startswith('PLUGIN_'):
            configs.update({
                key[7:].lower(): value
            })
        elif key.startswith('DRONE_'):
            configs['envs'].update({
                key: value
            })
    for key, value in configs.items():
        print(key, value)
    must_list = ['host', 'username', 'scripts']
    for key in must_list:
        if key not in configs:
            raise ValueError(f'请填写{key}')
    if 'password' not in configs and 'key' not in configs:
        raise ValueError("请填写password或key")
    port = configs.get('port')
    if not port:
        configs.update({'port': 22})
    else:
        try:
            port = int(configs.get('port'))
            configs.update({'port': port})
        except Exception as e:
            raise ValueError('port需为数字')
    configs.update({
        'scripts': configs.get('scripts').split(',')
    })

    return configs


