# cookiecutter-golang

Powered by [Cookiecutter](https://github.com/audreyr/cookiecutter), Cookiecutter Golang is a framework for jumpstarting production-ready go projects quickly.

## Features

- Generous `Makefile` with management commands
- Uses `go dep` (with optional go module support *requires go 1.11*)
- injects build time and git hash at build time.

## Optional Integrations

- Can use [viper](https://github.com/spf13/viper) for env var config
- Can use [cobra](https://github.com/spf13/cobra) for cli tools
- Can use [logrus](https://github.com/sirupsen/logrus) for logging
- Can create dockerfile for building go binary and dockerfile for final go binary (no code in final container)
- If docker is used adds docker management commands to makefile
- Option of TravisCI, CircleCI or None

## Constraints

- Uses `dep` or `mod` for dependency management
- Only maintained 3rd party libraries are used.

This project now uses docker multistage builds, you need at least docker version v17.05.0-ce to use the docker file in this template, [you can read more about multistage builds here](https://www.critiqus.com/post/multi-stage-docker-builds/).

## Usage

Let's pretend you want to create a project called "echoserver". Rather than starting from scratch maybe copying 
some files and then editing the results to include your name, email, and various configuration issues that always 
get forgotten until the worst possible moment, get cookiecutter to do all the work.

First, get Cookiecutter. Trust me, it's awesome:
```console
$ pip install cookiecutter
```

Alternatively, you can install `cookiecutter` with homebrew:
```console
$ brew install cookiecutter
```

Finally, to run it based on this template, type:
```console
$ cookiecutter https://github.com/YojimboSecurity/cookiecutter-golang.git
```

You will be asked about your basic info (name, project name, app name, etc.). This info will be used to customize your new project.

Warning: After this point, change 'David Johnson', etc to your own information.

Answer the prompts with your own desired [options](). For example:
```console
full_name [David Johnson]: David Johnson
github_username [YojimboSecurity]: YojimboSecurity
app_name [mygolangproject]: echoserver
project_short_description [A Golang project.]: Awesome Echo Server
docker_hub_username [YojimboSecurity]: YojimboSecurity
docker_image [YojimboSecurity/docker-alpine:latest]: YojimboSecurity/docker-alpine:latest
docker_build_image [YojimboSecurity/docker-alpine:gobuildimage]: YojimboSecurity/docker-alpine:gobuildimage
use_docker [y]: y
use_git [y]: y
use_logrus_logging [y]: y
use_viper_config [y]: y
use_cobra_cmd [y]: y
Select use_ci:
1 - travis
2 - circle
3 - none
Choose from 1, 2, 3 [1]: 1
```

Enter the project and take a look around:
```console
$ cd echoserver/
$ ls
```

Run `make help` to see the available management commands, or just run `make build` to build your project.
```console
$ make help
$ make build
$ ./bin/echoserver
```

## Credits

This is a fork of https://github.com/lacion/cookiecutter-golang.git
