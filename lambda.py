import logging
import boto3

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def startEc2Instance(envAwsRegion, envAwsInstancesIds):
    ec2 = boto3.client('ec2', region_name=envAwsRegion)
    ec2.start_instances(InstanceIds=envAwsInstancesIds)
    return {'started your instances': str(envAwsInstancesIds)}


def stopEc2Instance(envAwsRegion, envAwsInstancesIds):
    ec2 = boto3.client('ec2', region_name=envAwsRegion)
    ec2.stop_instances(InstanceIds=envAwsInstancesIds)
    return {'stoped your instances': str(envAwsInstancesIds)}



def handler(event, context):

    try:

        action = event.get("action", None)
        instances = event.get("instances", None)
        region = event.get("region", None)

        if action is not None and instances is not None and region is not None:

            if action == "start":

                result = startEc2Instance(region, instances)
                return result

            elif action == "stop":

                result = stopEc2Instance(region, instances)
                return result


    except Exception as e:
        return {
            "error": e
        }