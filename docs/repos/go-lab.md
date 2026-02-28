# go-lab

[View on GitHub](https://github.com/msashish/go-lab)

---

# go-lab go

## Run some basic code
    cd basics
    go run . 
    go run greet

## Call an external function..

    Go to https://go.dev/ and pick a module/package for using
    Change code to import module and use it        
    If we try running "go run ." then it fails
    Create a go.mod file that acts a requirement/dependency file. Without this, external modules do not get downlaoded.
        go mod init greet
        go run greet

## Create a module and call it externally
    Create a new module
        cd greeting
        go run greeting.com/greeting
    Call it in basics/greet.go
        cd basics
    Modify greet.go to call greeting.Hello(<input>)
    Modify basics/go.mod to apply "replace greeting.com/greeting => ../greeting"
        go run greet

## Create executable using build
        cd basics
        go build
        ./greet


## Learnings so far...
    Packages are published in modules. We hence have to import modules..

