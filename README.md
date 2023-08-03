# Testing Lambda Functions Locally Using AWS CDK and SAM
A setup to test my Python Lambda scripts locally before deploying them to AWS 
## Technologies
* Python
* AWS CDK
* Docker
* AWS SAM
* Docker
* Windows CMD / Linux Terminal
* AWS Lambda

## Project Overview

First setup your local environment by making sure the required dependencies are installed (AWS CDK, AWS SAM, Docker) then run the cdk init function in your local directory.

Next, install all library dependencies by installing the requirements.txt file in your .venv environment

Finally, run configure your test file with some test output and simulate your tests scenarios locally using AWS CDK, AWS SAM, and Docker.

## Detailed Breakdown

After creating your project directory, run command below:
```
cdk init app --language python
```

This will setup your AWS CDK environment with boilerplate files and supply a .venv for you

Install all the required dependencies
```
python -m pip install -r requirements.txt
```

Create folder for test file and then create the test file itself:
```
mkdir lambda
cd lambda
touch test.py
```

Run the below command to create the cdk.out folder and associated files:
```
cdk synth
```

If you are having trouble running this command, try:
* Closing and reopening VSCode
* Update npm
* Granting user modify access to the directory where the project resides
* Running the command from CMD instead of VSCode terminal
* Running the command from CMD as an administrator (this is what fixed the issue for me)

For whatever reason, Node really did not like being run from VSCode terminal. I kept the following error when running the previous command from the VSCode terminal: 
```
Error: EPERM: operation not permitted cdk_venv/python3.7/site-packages/jsii/_embedded/jsii/jsii-runtime.js:10408
```

Now invoke SAM to run the Lambda script locally in Docker and return the output.
```
sam local invoke -t ./cdk.out/AwsLambdaLocalTestStack.template.json
```

Now we can use SAM to generate some events for us using our Lambda function.

Create our events folder:

```
mkdir events
cd events
sam local generate-event sns notification
```

Now copy the output from the previous command, create an sns_event.json file and then paste in the output json.

Let's back out of our current directory and go to the root directory:

```
cd ..
```

Now we can run that same SAM command:

```
sam local invoke -t ./cdk.out/AwsLambdaLocalTestStack.template.json
```

Except we add the following parameters:

```
sam local invoke -t ./cdk.out/AwsLambdaLocalTestStack.template.json -e ./events/sns_event.json
```

We can use this process to simulate different events / use cases for our Lambda functions locally (using Docker) before we deploy any of these functions to our production environment. Great for unit testing.
