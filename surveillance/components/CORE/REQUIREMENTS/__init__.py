from ....models import Estimated_Amount_Coefficient 

class Requirements():

# store whatever you calculate here
    container = {

    }

    def __init__(self,data_pack):
        
        self.data_pack = data_pack

        print('start')
        print()
        print()
        print(data_pack)
        print()
    
        print('@@@@@@@@@@@@@@@@')


    # first we need to calculate the estimated amount of project
    # lets call it 

        self.calculation_estimated_amount(raw_data=data_pack['raw_data'])

    # then its time to call before func to calculate whatever related to before statement
        self.before()    
    # then its time to call before func to calculate whatever related to pending statement
        raw_data=data_pack['raw_data']
        self.pending_monthly(covenant_period=raw_data[0]['covenant_period'])
    # i think it must be clear
        self.pending_casework()
    # same as upper    
        self.after()
        print(Requirements.container)

# ----------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------


    def calculation_estimated_amount (self ,raw_data ) :
        
        self.raw_data = raw_data
    # اگر مبلغ براورد کار را یکسره وارد کرده بود 
        if (self.raw_data[1]['estimates_amount']) != None :
            estimated_amount = float(self.raw_data[1]['estimates_amount'])
        else :
            estimated_amount = None
            
            
            estimates_amount_dependent = float(self.raw_data[0]['estimates_amount_dependent'] )
            ea_equipment = float(self.raw_data[0]['ea_equipment'] )
            ea_steel = float(self.raw_data[0]['ea_steel'] )
            ea_rural_water = float(self.raw_data[0]['ea_rural_water'] )
            ea_shipping = float(self.raw_data[0]['ea_shipping'] )
            ea_under_pressure_irrigation = float(self.raw_data[0]['ea_under_pressure_irrigation'] )
            ea_mechanical_facilities = float(self.raw_data[0]['ea_mechanical_facilities'] )
            ea_electrical_facilities = float(self.raw_data[0]['ea_electrical_facilities'] )
            ea_railway_airport_highways = float(self.raw_data[0]['ea_railway_airport_highways'] )
            ea_railway_airport_highways_type_1_2 = float(self.raw_data[0]['ea_railway_airport_highways_type_1_2'] )
            ea_special_equipment = float(self.raw_data[0]['ea_special_equipment'] ) # ضریب تجهیزات خاص که باید از کاربر گرفت


            coefficient = Estimated_Amount_Coefficient.objects.get(id=1)

            estimated_amount = estimates_amount_dependent - (ea_equipment*coefficient.equipment_coefficient) - (ea_steel*coefficient.steel_coefficient)
            estimated_amount -= (ea_rural_water*coefficient.rural_water_coefficient) + (ea_shipping*coefficient.shipping_coefficient) + (ea_under_pressure_irrigation*coefficient.under_pressure_irrigation_coefficient) 
            estimated_amount -= (ea_mechanical_facilities*coefficient.mechanical_facilities_coefficient) + (ea_electrical_facilities*coefficient.electrical_facilities_coefficient)
            estimated_amount -= (ea_railway_airport_highways*coefficient.railway_airport_highways_coefficient) + (ea_railway_airport_highways_type_1_2*coefficient.railway_airport_highways_type_1_2_coefficient)
             
            # نهایتا مقدار براورد اولیه پروژه مشخص شد 

        Requirements.container['estimated_amount'] = estimated_amount

    @staticmethod
    def before ():
        correction_coefficient_alpha = None
        # بر هزار تقسیم میکنیم تا واحد ان به میلیارد ریال تبدیل شود
        estimated_amount = Requirements.container['estimated_amount'] / 1000 

        if estimated_amount <= 40 :
            correction_coefficient_alpha = 0.0142 * estimated_amount
            Requirements.container['correction_coefficient_alpha'] = correction_coefficient_alpha
       
        elif 40<estimated_amount <=300 :
            correction_coefficient_alpha = 0.00135 * estimated_amount + 0.514
            Requirements.container['correction_coefficient_alpha'] = correction_coefficient_alpha
       
        elif 300<estimated_amount <= 1400 :
            correction_coefficient_alpha = 0.00052 * estimated_amount + 0.763
            Requirements.container['correction_coefficient_alpha'] = correction_coefficient_alpha
       
        elif 1400<estimated_amount <= 3300 :
            correction_coefficient_alpha = 0.0003 * estimated_amount + 1.071
            Requirements.container['correction_coefficient_alpha'] = correction_coefficient_alpha
       
        else :
            correction_coefficient_alpha = 0.000125 * estimated_amount + 1.6785
            Requirements.container['correction_coefficient_alpha'] = correction_coefficient_alpha
        
    def pending_monthly (self, covenant_period):

        self.covenant_period = covenant_period
        correction_coefficient_beta = None

        monthly_hypothetical_function = Requirements.container['estimated_amount'] /  self.covenant_period          # کارکرد فرضی ماهانه اجرا
        Requirements.container['monthly_hypothetical_function'] = monthly_hypothetical_function
        
        # بر هزار تقسیم میکنیم تا واحد ان به میلیارد ریال تبدیل شود
        monthly_hypothetical_function = monthly_hypothetical_function/1000


        if monthly_hypothetical_function <= 7 :
            correction_coefficient_beta = 0.0495 * monthly_hypothetical_function + 0.0415
            Requirements.container['correction_coefficient_beta'] = correction_coefficient_beta

            
        elif 7 < monthly_hypothetical_function <= 60 :
            correction_coefficient_beta = 0.033 * monthly_hypothetical_function + 0.157
            Requirements.container['correction_coefficient_beta'] = correction_coefficient_beta


        elif 60 < monthly_hypothetical_function <= 85 :
            correction_coefficient_beta = 0.019 * monthly_hypothetical_function + 0.997
            Requirements.container['correction_coefficient_beta'] = correction_coefficient_beta


        else:
            correction_coefficient_beta = 0.008 * monthly_hypothetical_function + 1.932 
            Requirements.container['correction_coefficient_beta'] = correction_coefficient_beta

    @staticmethod
    def pending_casework () :
        # بر هزار تقسیم میکنیم تا واحد ان به میلیارد ریال تبدیل شود
        estimated_amount = Requirements.container['estimated_amount'] / 1000 

        correction_coefficient_teta = None

        if estimated_amount <= 46 :
            correction_coefficient_teta = 0.0088 * estimated_amount + 0.08
            Requirements.container['correction_coefficient_teta'] = correction_coefficient_teta

        elif 46< estimated_amount <= 225 :
            correction_coefficient_teta = 0.0024 * estimated_amount + 0.3744 
            Requirements.container['correction_coefficient_teta'] = correction_coefficient_teta

        elif 225 < estimated_amount <= 950 :
            correction_coefficient_teta = 0.00034 * estimated_amount + 0.8379
            Requirements.container['correction_coefficient_teta'] = correction_coefficient_teta

        elif 950 < estimated_amount <= 3500:
            correction_coefficient_teta = 0.00012 * estimated_amount + 1.0469
            Requirements.container['correction_coefficient_teta'] = correction_coefficient_teta

        else:
            correction_coefficient_teta = 0.00000135 * estimated_amount + 1.41965
            Requirements.container['correction_coefficient_teta'] = correction_coefficient_teta


    @staticmethod
    def after():     # the calculation here is same as before
        # بر هزار تقسیم میکنیم تا واحد ان به میلیارد ریال تبدیل شود
        estimated_amount = Requirements.container['estimated_amount'] / 1000 

        correction_coefficient_epsilon = None

        if estimated_amount <= 40 : 
            correction_coefficient_epsilon = 0.0142 * estimated_amount
            Requirements.container['correction_coefficient_epsilon'] = correction_coefficient_epsilon

        elif 40 < estimated_amount <= 300 :
            correction_coefficient_epsilon = 0.00135 * estimated_amount + 0.514
            Requirements.container['correction_coefficient_epsilon'] = correction_coefficient_epsilon
       
        elif 300 < estimated_amount < 1400 :
            correction_coefficient_epsilon = 0.00052 * estimated_amount + 0.763
            Requirements.container['correction_coefficient_epsilon'] = correction_coefficient_epsilon
       
        elif 1400 < estimated_amount <= 3300 :
            correction_coefficient_epsilon = 0.0003 * estimated_amount + 1.071
            Requirements.container['correction_coefficient_epsilon'] = correction_coefficient_epsilon
        
        else:
            correction_coefficient_epsilon = 0.000125 * estimated_amount + 1.6785
            Requirements.container['correction_coefficient_epsilon'] = correction_coefficient_epsilon

























