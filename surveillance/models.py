from django.db import models

# ! -------------------------------------------------------------------------------------------


class Before_Implementation_Title (models.Model) :
   
    row_number = models.IntegerField()                           # شماره ردیف 
    row_description = models.CharField(max_length=150)




class Before_Implementation_Subtitle (models.Model) :

    before_implementation_title = models.ForeignKey(Before_Implementation_Title, on_delete=models.CASCADE)

    row_number = models.IntegerField()
    row_description = models.CharField(max_length=150)
    deliverable = models.CharField(max_length=100)
    base_price = models.IntegerField(null=True,blank=True)



# ! ------------------------------------------------------------------------------------------


class During_Implementation_Monthly_Title (models.Model) :
   
    row_number = models.IntegerField()                           # شماره ردیف 
    row_description = models.CharField(max_length=150)




class During_Implementation_Monthly_Subtitle (models.Model) :

    during_implementation_monthly_title = models.ForeignKey(During_Implementation_Monthly_Title, on_delete=models.CASCADE)

    row_number = models.IntegerField()
    row_description = models.CharField(max_length=150)
    deliverable = models.CharField(max_length=100)
    base_price = models.IntegerField(null=True,blank=True)

# ! ------------------------------------------------------------------------------------------


class During_Implementation_Case_Title (models.Model) :
   
    row_number = models.IntegerField()                           # شماره ردیف 
    row_description = models.CharField(max_length=150)




class During_Implementation_Case_Subtitle (models.Model) :

    during_implementation_case_title = models.ForeignKey(During_Implementation_Case_Title, on_delete=models.CASCADE)

    row_number = models.IntegerField()
    row_description = models.CharField(max_length=150)
    deliverable = models.CharField(max_length=100)
    base_price = models.IntegerField(null=True,blank=True)
    repetition = models.IntegerField(null=True,blank=True)


# ! ------------------------------------------------------------------------------------------

#
#class During_Implementation_Technical_Title (models.Model) :
#   
#    row_number = models.IntegerField()                           # شماره ردیف 
#    row_description = models.CharField(max_length=150)
#
#
#
#
#class During_Implementation_Technical_Subtitle (models.Model) :
#
#    during_implementation_technical_title = models.ForeignKey(During_Implementation_Technical_Title, on_delete=models.CASCADE)
#
#    row_number = models.IntegerField()
#    row_description = models.CharField(max_length=150)
#    deliverable = models.CharField(max_length=100)
#    base_price = models.IntegerField(null=True,blank=True)
#

# ! ------------------------------------------------------------------------------------------


class After_Implementation_Title (models.Model) :
   
    row_number = models.IntegerField()                           # شماره ردیف 
    row_description = models.CharField(max_length=150)




class After_Implementation_Subtitle (models.Model) :

    after_implementation_title = models.ForeignKey(After_Implementation_Title, on_delete=models.CASCADE)

    row_number = models.IntegerField()
    row_description = models.CharField(max_length=150)
    deliverable = models.CharField(max_length=100)
    base_price = models.IntegerField(null=True,blank=True)

# ! ------------------------------------------------------------------------------------------


class Support (models.Model) :
    row_number = models.IntegerField()
    row_name = models.CharField(max_length=160)
    base_price = models.IntegerField(null=True,blank=True)
    time_duration = models.IntegerField(null=True,blank=True)
    number = models.IntegerField(null=True,blank=True)
    cost = models.IntegerField(null=True,blank=True)


class Estimated_Amount_Coefficient (models.Model):
    
    equipment_coefficient = models.FloatField()
    steel_coefficient = models.FloatField()
    rural_water_coefficient = models.FloatField()
    shipping_coefficient = models.FloatField()
    under_pressure_irrigation_coefficient = models.FloatField()
    mechanical_facilities_coefficient = models.FloatField()
    electrical_facilities_coefficient = models.FloatField()
    railway_airport_highways_coefficient = models.FloatField()
    railway_airport_highways_type_1_2_coefficient = models.FloatField()







