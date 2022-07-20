package main

import (
	{% if cookiecutter.use_cobra_cmd == "y" %}"flag"
	"fmt"
	"{{cookiecutter.app_name}}/version"{% endif %}
	{% if cookiecutter.use_cobra_cmd == "y" %}
	"{{cookiecutter.app_name}}/cmd"
	"github.com/pkg/profile"
	{% endif %}
)

func main() {

    {% if cookiecutter.use_cobra_cmd == "y" %}
	if version.Profile == "on"{
		if version.ProfileType == "CPU"{
			defer profile.Start(profile.CPUProfile, profile.ProfilePath(".")).Stop()
		}
		if version.ProfileType == "MEM"{
			defer profile.Start(profile.MemProfile, profile.MemProfileRate(1), profile.ProfilePath(".")).Stop()
		}
	}

    cmd.Execute()
	{% else %}
	versionFlag := flag.Bool("version", false, "Version")
	flag.Parse()

	if *versionFlag {
		fmt.Println("Build Date:", version.BuildDate)
        fmt.Println("Git Commit:", version.GitCommit)
        fmt.Println("Version:", version.Version)
        fmt.Println("Go Version:", version.GoVersion)
        fmt.Println("OS / Arch:", version.OsArch)
		return
	}
	fmt.Println("Hello.")
    {% endif %}
}
