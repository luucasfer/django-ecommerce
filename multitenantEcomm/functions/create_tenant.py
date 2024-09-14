#from django.apps import apps
#
#Tenant = apps.get_model('multitenantEcomm', 'Tenant')
#Domain = apps.get_model('multitenantEcomm', 'Domain')
#
#def run():
#    tenant = Tenant(schema_name='tenant1', name='Loja 1', paid_until='2025-12-31', on_trial=True)
#    tenant.save()
#
#    domain = Domain(domain='loja1.dominio.com', tenant=tenant)
#    domain.save()
#
#    print(f'Tenant {tenant.name} criado com sucesso com o domínio {domain.domain}')
#