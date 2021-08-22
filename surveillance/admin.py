from django.contrib import admin

# Register your models here.

from .models import After_Implementation_Subtitle , After_Implementation_Title , Before_Implementation_Subtitle , Before_Implementation_Title 
from .models import During_Implementation_Case_Subtitle , During_Implementation_Case_Title , During_Implementation_Monthly_Subtitle , During_Implementation_Monthly_Title
from .models import Estimated_Amount_Coefficient , Support

admin.site.register(After_Implementation_Subtitle)
admin.site.register(After_Implementation_Title)
admin.site.register(Before_Implementation_Subtitle)
admin.site.register(Before_Implementation_Title)
admin.site.register(During_Implementation_Case_Subtitle)
admin.site.register(During_Implementation_Case_Title)
admin.site.register(During_Implementation_Monthly_Subtitle)
admin.site.register(During_Implementation_Monthly_Title)
admin.site.register(Estimated_Amount_Coefficient)
admin.site.register(Support)


