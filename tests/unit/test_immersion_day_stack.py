import aws_cdk as core
import aws_cdk.assertions as assertions

from immersion_day.immersion_day_stack import ImmersionDayStack

# example tests. To run these tests, uncomment this file along with the example
# resource in immersion_day/immersion_day_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = ImmersionDayStack(app, "immersion-day")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
