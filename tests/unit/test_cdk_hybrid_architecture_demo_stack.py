import aws_cdk as core
import aws_cdk.assertions as assertions

from demo.cdk_hybrid_architecture_demo_stack import CdkHybridArchitectureDemoStack

# example tests. To run these tests, uncomment this file along with the example
# resource in cdk_hybrid_architecture_demo/cdk_hybrid_architecture_demo_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = CdkHybridArchitectureDemoStack(app, "cdk-hybrid-architecture-demo")
    template = assertions.Template.from_stack(stack)

    template.has_resource_properties("AWS::EC2::Instance", {
        "InstanceType": "t2.micro"
    })
