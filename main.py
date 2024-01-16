import argparse

from k8s_collector.collectors import K8SCollector

parser = argparse.ArgumentParser()
parser.add_argument("-n", "--namespace", type=str,
                    help="namespace to listen for resources, if not provided listen cluster-wide")
args = parser.parse_args()

collector = K8SCollector(namespace=args.namespace)
collector.collect()
