import rubrik_cdm

rubrik = rubrik_cdm.Connect()

# Retrieve summary information for the "Python SDK" SLA Domain
sla_name = "Python SDK"

sla_summary_information = rubrik.get('v1', '/sla_domain?name={}'.format(sla_name))
