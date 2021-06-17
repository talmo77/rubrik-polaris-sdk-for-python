import pprint
from rubrik_polaris.rubrik_polaris import PolarisClient

pp = pprint.PrettyPrinter(indent=4)

domain = 'my-company'
username = 'john.doe@example.com'
password = 's3cr3tP_a55w0R)'

client = PolarisClient(domain, username, password, insecure=True)
connected_clusters = client.get_connected_clusters()
pp.pprint(connected_clusters)
