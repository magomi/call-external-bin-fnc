# Call binary from lambda function

Proof of concept how to call a binary from a 

## How it works

Base for running lambda functions is the linux platform. The environment
where a lambda function is running within can be read from different
environment variables. 

Unfortunately the directory where the lambda is installed is forbidden for 
calling external binaries. Therefore the binary needs to be prepared:
* copy it to a directory where execution is allowed
* set the executable flag for the binary

## Prepare the binary 

I choosed Go to implement and create the binary that can be run
on the AWS lambda runtime environment.

Go was choosen because of its ability compile native binaries for
different platforms.

For the proof of concept the binary only prints a json document to 
stdout.

* if necessary install a recent golang version (tested with version 1.10.4)
* switch into the `bin` directory
* call `go build gobin.go`

## Deploy to AWS

Deployment to AWS is straight forward. I used the AWS CLI.

* create a lambda `aws lambda create-function --function-name call-external-bin-fnc --runtime python3.8`
* zip the local lambda directory into an archive `zip -r call-external-bin-fnc.zip <path-to-the-local-lambda-dir>`
* upload the lambda code `aws lambda update-function-code --function-name call-external-bin-fnc`

Run It!  
