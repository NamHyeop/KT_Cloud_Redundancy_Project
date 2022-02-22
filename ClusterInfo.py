from os import path
from kubernetes import client, config
import yaml


### 클러스터의 정보확인 기능 ######
# Configs can be set in Configuration class directly or using helper utility
# config.load_kube_config()
#
# print(config.load_kube_config())
# v1 = client.CoreV1Api()
# print("Listing pods with their IPs:")
# ret = v1.list_pod_for_all_namespaces(watch=False)
# for i in ret.items:
#     print("%s\t%s\t%s" % (i.status.pod_ip, i.metadata.namespace, i.metadata.name))

############################3#

##### 사용할 수 있느 API 기능 명시 #######
# def main():
#     # Configs can be set in Configuration class directly or using helper
#     # utility. If no argument provided, the config will be loaded from
#     # default location.
#     config.load_kube_config()
#
#     print("Supported APIs (* is preferred version):")
#     print("%-40s %s" %
#           ("core", ",".join(client.CoreApi().get_api_versions().versions)))
#     for api in client.ApisApi().get_api_versions().groups:
#         versions = []
#         for v in api.versions:
#             name = ""
#             if v.version == api.preferred_version.version and len(
#                     api.versions) > 1:
#                 name += "*"
#             name += v.version
#             versions.append(name)
#         print("%-40s %s" % (api.name, ",".join(versions)))
#
#
# if __name__ == '__main__':
#     main()
########################################

#####################경로에 위치하는 yaml 파일 생성 기능####################
# def main():
#     # Configs can be set in Configuration class directly or using helper
#     # utility. If no argument provided, the config will be loaded from
#     # default location.
#     config.load_kube_config()
#
#     with open(path.join(path.dirname("경로"), "nginx-deployment.yaml")) as f:
#         dep = yaml.safe_load(f)
#         k8s_apps_v1 = client.AppsV1Api()
#         resp = k8s_apps_v1.create_namespaced_deployment(
#             body=dep, namespace="default")
#         print("Deployment created. status='%s'" % resp.metadata.name)
#
#
# if __name__ == '__main__':
#     main()

##############################################################
def main():
    # Define the bearer token we are going to use to authenticate.
    # See here to create the token:
    # https://kubernetes.io/docs/tasks/access-application-cluster/access-cluster/
    aToken = "i5ocb4.3cv61dczfn1q7ynp "

    # Create a configuration object
    aConfiguration = client.Configuration()

    # Specify the endpoint of your Kube cluster
    aConfiguration.host = "https://192.167.56.30:443"

    # Security part.
    # In this simple example we are not going to verify the SSL certificate of
    # the remote cluster (for simplicity reason)
    aConfiguration.verify_ssl = False
    # Nevertheless if you want to do it you can with these 2 parameters
    # configuration.verify_ssl=True
    # ssl_ca_cert is the filepath to the file that contains the certificate.
    # configuration.ssl_ca_cert="certificate"

    aConfiguration.api_key = {"authorization": "Bearer " + aToken}

    # Create a ApiClient with our config
    aApiClient = client.ApiClient(aConfiguration)

    # Do calls
    v1 = client.CoreV1Api(aApiClient)
    print("Listing pods with their IPs:")
    ret = v1.list_pod_for_all_namespaces(watch=False)
    for i in ret.items:
        print("%s\t%s\t%s" %
              (i.status.pod_ip, i.metadata.namespace, i.metadata.name))


if __name__ == '__main__':
    main()
