import aws_cdk as core
import aws_cdk.assertions as assertions

from aws_lambda_local_test.aws_lambda_local_test_stack import AwsLambdaLocalTestStack

# example tests. To run these tests, uncomment this file along with the example
# resource in aws_lambda_local_test/aws_lambda_local_test_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = AwsLambdaLocalTestStack(app, "aws-lambda-local-test")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
