from rubrik_polaris.rubrik_polaris import PolarisClient


domain = 'somedomin'
username = 'john.doe@somedomain.com'
password = 'xxxxxxxxx'
groupby = 'ObjectType'
slaTimeRange = 'SinceProtection'

client = PolarisClient(domain, username, password, insecure=True)
connected_clusters = client.get_connected_clusters()
 
i = 0

for each in connected_clusters:
	clusterid = connected_clusters[i]['id']	
	cluster_name = connected_clusters[i]['name']
	sla_domain = client.get_cdm_cluster_sla_list(clusterid)
	cdm_capacity = client.get_cdm_cluster_capacity(clusterid)['nodes'][0]['metric']
	capacity_bysla = client.get_cdm_cluster_capacitybysla(clusterid,groupby,slaTimeRange)
	i += 1 
	TB = 1000000000000
	TiB = 1099511627776
	GB = 1000000000

	f = 0

	print("**********************************************************************************************************************")
	print("Cluster Name:\t", cluster_name, "Cluster UUID:\t", clusterid)
	print("Used Capacity:\t",cdm_capacity['usedCapacity']/TB, "Total Capacity:\t",cdm_capacity['totalCapacity']/TB)
	print("**********************************************************************************************************************")

	if groupby == 'ObjectType':
		gType = 'enumValue';
	elif groupby == 'SlaDomain':
		gType = 'name'
		for sla in sla_domain:
			print("SLA Name:",sla['name'],"SLA ID:",sla['id'],"Object Count:",sla['protectedObjectCount'])
	elif groupby == 'Cluster':
		gType = 'name'

	for each in capacity_bysla:
		groupbyInfo = (capacity_bysla[f]['groupByInfo'])
		y = capacity_bysla[f]['snappableGroupBy'][0]['snappableConnection']['aggregation']
		print("GroupByInfo:\t",groupbyInfo[gType],"\t","Physical TB Usage:",y['physicalBytes']/TB,"\t","Archive TB Usage:",y['archiveStorage']/TB,"\t","Replicated TB Storage:",y['replicaStorage']/TB)
		f += 1
	
