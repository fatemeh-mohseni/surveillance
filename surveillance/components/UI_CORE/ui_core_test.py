from django.http import HttpResponse
from .ui_core import Collect_Data , Collect_Table_Data , Release_Data
import datetime
from ..CORE.REQUIREMENTS import Requirements

def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)




cc=Collect_Data(contract_name='fatemeh',Regional_coefficient='ghaojgh')
n=cc.Estimated_Amount_Dependent(estimates_amount_dependent='1400' , ea_electrical_facilities='sejrfng', ea_equipment='fogbre', ea_shipping='ofgnr' , ea_mechanical_facilities='jdng;ajg' , ea_rural_water='4352345', ea_steel='fgafng', ea_under_pressure_irrigation='435435')
print(':?????')

m=cc.Estimate_Amount(estimates_amount='324')

h=Collect_Table_Data()
b=h.raw(m,n)



print('******')
r=Release_Data(raw_data=b)
rr=r.send()
w=Requirements(rr)