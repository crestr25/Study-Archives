# Notes: Dev Environment
---

`$ go help [command]` -> all commands available <br>
`$ go env` -> all go env vars.<br>
`$ go version` -> Go install version <br>
`$ go get` -> adjust dependencies in go.mod file <br>
`$ go install` -> install go.mod dependency packages <br>
`$ go fmt` -> format go code <br>

## Go Modules

A module is a collection of Go packages stored in a file tree with a go.mod file at its root.

`go.mod` file defines the module's **Module path**, which serves also as the **import path** used for the root directory and its dependency requirement (the other modules needed for a successful build).

- Creating a `go module`
    1. `$ go mod init <namespace>`, Initialize the module by creating a `go.mod` file, with the definition for the module's path.
- Adding a dependency to a `go module`
    1. Get the dependency on the code, once it is called the dependency will be added along with the respective indirect dependencies.
    2. `go list -m all`, lists all dependencies.
    3. a `go.sum` is created to store the checksum of all dependencies.
- Upgrading a dependency on a `go module`
    1. `go get <dependency>@v0.0.1`, the command upgrades dependency to the specified version after the `@`.
    2. `go list -m -versions <dependency>`, list all available versions for a dependency, useful if an upgrade breaks the code.

## Go Workspace

`GOPATH`, Points to the workspace.<br>
`GOROOT`, Points to the binary installation of GO.

One folder with any name. Inside it should have the following three folders.
- ***bin***, Where we store binary files, compiled files.
- ***pkg***, Where archive files are stored so it does not need to recompile.
- ***src***, Namespacing and package management.
    - github.com/<git_user>
    - we use `go get` to use external packages.


