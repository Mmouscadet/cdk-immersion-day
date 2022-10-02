from aws_cdk import (
    CfnOutput,
    RemovalPolicy,
    Stack
)
from constructs import Construct
from aws_solutions_constructs.aws_cloudfront_s3 import CloudFrontToS3

class ImmersionDayStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        
         # first we dploy an s3 bucket with its cloudfront distribution and its logging facilities ()
        myCloudFrontToS3 = CloudFrontToS3(
            self, 'ImmersionDayCDK', insert_http_security_headers=False)

        myCloudFrontToS3.s3_bucket.apply_removal_policy(RemovalPolicy.DESTROY)
        myCloudFrontToS3.cloud_front_logging_bucket.apply_removal_policy(RemovalPolicy.DESTROY)
        myCloudFrontToS3.s3_logging_bucket.apply_removal_policy(RemovalPolicy.DESTROY)


        CfnOutput(self, "CloudFrontDistribution", value=myCloudFrontToS3.cloud_front_web_distribution.distribution_domain_name)
        CfnOutput(self, "WebSiteBucket", value=myCloudFrontToS3.s3_bucket.bucket_name)