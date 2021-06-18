import pprint
from rubrik_polaris.rubrik_polaris import PolarisClient

pp = pprint.PrettyPrinter(indent=4)

domain = 'my-company'
username = 'john.doe@example.com'
password = 's3cr3tP_a55w0R)'
cluster_id = '5a4dd475-eb3d-4b01-bddb-f835bec54e17'

client = PolarisClient(domain, username, password, insecure=True)

cdm_sla_domains = client.get_cdm_cluster_sla_list(cluster_id)

pp.pprint(cdm_sla_domains)
