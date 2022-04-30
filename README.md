# Drone Fabric SSH

```yaml
  - name: deploy
    image: yuhuiwang/fabric-ssh
    pull: always
    settings:
      host: 192.168.7.63
      username:
        from_secret: ubuntu_username
      password:
        from_secret: ubuntu_password
      port: 22
      envs:
        - FOO:BAR
      scripts:
        - echo $FOO
        - echo `TZ='UTC' date -d @${DRONE_BUILD_FINISHED} +%Y-%m-%d-%H-%M-%S`
    when:
      branch:
        - master

```
  