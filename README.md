# Drone Fabric SSH

when I use [appleboy/drone-ssh](https://github.com/appleboy/drone-ssh), I don't know why, when I set environment in drone-ssh envs section, it doesn't affect. so I build this image, integrity with [fabric](https://github.com/fabric/fabric).

## Usage
```yaml
  - name: deploy
    image: yuhuiwang/fabric-ssh
    pull: if-not-exists
    settings:
      host: 192.168.7.63
      username:
        from_secret: ubuntu_username
      password:
        from_secret: ubuntu_password
      port: 22
      envs:
        - FOO: BAR
      scripts:
        - echo $FOO
        - echo `TZ='UTC' date -d @${DRONE_BUILD_FINISHED} +%Y-%m-%d_%H-%M-%S`
    when:
      branch:
        - master
```
will output
```shell
execute [echo $FOO] on [192.168.7.63]
result
BAR

execute [echo `TZ='UTC' date -d @1651307238 +%Y-%m-%d_%H-%M-%S`] on [192.168.7.63]
result
2022-04-30_08-27-18
```

  