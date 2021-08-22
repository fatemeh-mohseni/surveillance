from ..CORE.REQUIREMENTS import Requirements as requ
class Collect_Data () :
    '''
    
    collect input data from user

    '''

    def __init__(self,contract_name = None , contract_date=None , covenant_period=None , covenant_repeatation=None , year_matching_coefficient=None , farthest_distance=None , Feature_coefficient=None , Regional_coefficient=None) -> None:
        
        self.contract_name=contract_name
        self.contract_date = contract_date                                   # تاریخ انعقاد قرارداد
    #                   
        self.covenant_period = covenant_period                                 # طول مدت پیمان در قرارداد
        self.covenant_repeatation = covenant_repeatation                            # تعداد تکرار پیمان
    #               
        self.year_matching_coefficient = year_matching_coefficient                       # ضریب تطابق سال   
        self.farthest_distance = farthest_distance                               # فاصله میان دورترین ۲ نقطه در کارگاه (متر)
        self.Feature_coefficient = Feature_coefficient                             #  ضریب ویژگی کار (جدول رو میدیم از توش عدد رو وارد میکنه کاربر)
        self.Regional_coefficient = Regional_coefficient                            # ضریب منطقه ای 


    def Estimated_Amount_Dependent(self,estimates_amount_dependent=None,ea_equipment=None,ea_steel=None,ea_rural_water=None,ea_shipping=None , ea_under_pressure_irrigation=None , ea_mechanical_facilities=None , ea_electrical_facilities=None) :              


        self.estimates_amount_dependent = estimates_amount_dependent                      # مبلغ برآورد کل اجراي کار براساس آخرین فهرست بهاي پایه (براساس فهرست بهای پایه سال 1400)
        self.ea_equipment = ea_equipment                                    # مبلغ برآورد فصول مرتبط با تجهیزات (تبصره 1، جدول شمار 2-1)
        self.ea_steel = ea_steel                                        # مبلغ برآورد فصول مرتبط با کارهای فولادی و فولادی سنگین
        self.ea_rural_water = ea_rural_water                                  # مبلغ برآورد فصول مرتبط با تجهیزات رشته انتقال و توزیع آب روستایی (تبصره 2)
        self.ea_shipping = ea_shipping                                     # مبلغ برآورد فصل "حمل" یا "حمل و نقل" (تبصره 3)   
        self.ea_under_pressure_irrigation = ea_under_pressure_irrigation                    # مبلغ برآورد فصول 6 و 7 فهرست بهای واحد پایه رشته آبیاری تحت فشار (تبصره ۴)
        self.ea_mechanical_facilities = ea_mechanical_facilities                        # فهارس بهاي واحد پایه رشته تاسیسات برقی (تبصره ۴) 
        self.ea_electrical_facilities = ea_electrical_facilities                        # (تبصره ۴) فهارس بهاي واحد پایه رشته تاسیسات مکانیکی 

        self.ea_railway_airport_highways = None                     # مبلغ برآورد فصل 15 فهرست راه، راه آهن و باند فرودگاه و راهداری (تبصره 5)
        self.ea_railway_airport_highways_type_1_2 = None            # مبلغ برآورد فصل 15 فهرست راه، راه آهن و باند فرودگاه و راهداری در خصوص پروژه‌های بهسازی نوع یک و دو (تبصره 5)
        self.ea_special_equipment = None                            # مبلغ برآورد خرید تجهیزات خاص*
        

        listt=[self.estimates_amount_dependent , self.ea_equipment , self.ea_steel , self.ea_rural_water , self.ea_shipping , self.ea_under_pressure_irrigation , self.ea_mechanical_facilities , self.ea_electrical_facilities , self.ea_railway_airport_highways_type_1_2 , self.ea_railway_airport_highways, self.ea_special_equipment]

        raw_data1=self.jsonify1(listt=listt)
        return raw_data1


    def Estimate_Amount (self,estimates_amount=None) :

        self.estimates_amount = estimates_amount                                # مبلغ براورد اجرای کار

        list1 = [self.estimates_amount]
        raw_data2 = self.jsonify2(list1=list1)
        return raw_data2



    def jsonify1(self, listt):
                
        # neat data from __init__ func. & Estimated_Amount_Dependent

        raw_data1 = {
        'contract_name' : self.contract_name ,
        'contract_date' : self.contract_date ,
        'covenant_period' : self.covenant_period , 
        'covenant_repeatation' : self.covenant_repeatation ,
        'year_matching_coefficient' : self.year_matching_coefficient ,
        'farthest_distance' : self.farthest_distance ,
        'Feature_coefficient' : self.Feature_coefficient ,
        'Regional_coefficient' : self.Regional_coefficient ,
        'estimates_amount_dependent' : listt[0] ,
        'ea_equipment' : listt[1] ,
        'ea_steel' : listt[2] ,
        'ea_rural_water' : listt[3] ,
        'ea_shipping' : listt[4] ,
        'ea_under_pressure_irrigation' : listt[5] ,
        'ea_mechanical_facilities' : listt[6] ,
        'ea_electrical_facilities' :  listt[7] ,
        'ea_railway_airport_highways' : listt[8] ,
        'ea_railway_airport_highways_type_1_2' : listt[9] ,
        'ea_special_equipment' : listt[10],
        }

       
        
        return raw_data1

    def jsonify2(self,list1=None):

        # neat data from   Estimate_Amount 

        raw_data2 ={
        'estimates_amount' : list1[0]    
        }

        return raw_data2


# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


class Collect_Table_Data (Collect_Data) :


# اطلاعات دستی جدول هارو میگیره تو تابعای بیفور و ... و تو تابع خام میاد کل خروجی کلاس بالارو میکنه یه لیست و پس میده

    def raw (self, raw_data2 , raw_data1):

        global raw_data
        
        self.raw_data1 = raw_data1
        self.raw_data2 = raw_data2

        raw_data = [raw_data1, raw_data2]

        print('@@@@@@',raw_data)
        return raw_data

    # ---------------------------------------------------------

    def before (self , before_201010100=None , before_201040301=None ,before_201040302=None ,before_201040303=None ,before_201040304=None ,before_201040305=None ) :

        self.before_201010100 = before_201010100

        self.before_201040301 = before_201040301
        self.before_201040302 = before_201040302
        self.before_201040303 = before_201040303
        self.before_201040304 = before_201040304
        self.before_201040305 = before_201040305
        
        
        before_data = [self.before_201010100 , self.before_201040301 , self.before_201040302 , self.before_201040303 , self.before_201040304 , self.before_201040305]

        self.before_jsonify(before_data=before_data)

    def before_jsonify(self,before_data) :
        
        before_table_data = {
            'before_201010100' : before_data[0],
            'before_201040301' : before_data[1],
            'before_201040302' : before_data[2],
            'before_201040303' : before_data[3],
            'before_201040304' : before_data[4],
            'before_201040305' : before_data[5]
        }
        return before_table_data
    # ---------------------------------------------------------

    def pending_monthly(self):
        pass

    # ---------------------------------------------------------

    def pending_casework(self, pending_cw_302010105 = None, pending_cw_302020300 = None , pending_cw_302030400 = None , pending_cw_302040100 = None , pending_cw_302040200 = None , pending_cw_302040500 = None , pending_cw_302050000=None ):
        
        self.pending_cw_302010105 = pending_cw_302010105
        self.pending_cw_302020300 = pending_cw_302020300
        self.pending_cw_302030400 = pending_cw_302030400
        self.pending_cw_302040100 = pending_cw_302040100
        self.pending_cw_302040200 = pending_cw_302040200
        self.pending_cw_302040500 = pending_cw_302040500
        self.pending_cw_302050000 = pending_cw_302050000

        pending_casework_data = [self.pending_cw_302010105,self.pending_cw_302020300,self.pending_cw_302030400,self.pending_cw_302040100,self.pending_cw_302040200,self.pending_cw_302040500,self.pending_cw_302050000]

        self.pending_casework_jsonify(pending_casework_data=pending_casework_data)

    def pending_casework_jsonify(self,pending_casework_data):
        pending_casework_table_data = {
            'pending_cw_302010105' : pending_casework_data[0],
            'pending_cw_302020300' : pending_casework_data[1],
            'pending_cw_302030400' : pending_casework_data[2],
            'pending_cw_302040100' : pending_casework_data[3],
            'pending_cw_302040200' : pending_casework_data[4],
            'pending_cw_302040500' : pending_casework_data[5],
            'pending_cw_302050000' : pending_casework_data[6],
        }
        return pending_casework_table_data
    # ---------------------------------------------------------

    def pending_casework_repetition(self,pending_cwr_302010105=None, pending_cwr_302010202=None, pending_cwr_302010203=None , pending_cwr_302010204=None, pending_cwr_302020300=None, pending_cwr_302020400=None, pending_cwr_302020800=None, pending_cwr_302020900=None, pending_cwr_302021001=None, pending_cwr_302021002=None, pending_cwr_302040100=None,pending_cwr_302040200=None, pending_cwr_302040400=None, pending_cwr_302040500=None, pending_cwr_302050000=None ):
        
        self.pending_cwr_302010105 = pending_cwr_302010105
        self.pending_cwr_302010202 = pending_cwr_302010202
        self.pending_cwr_302010203 = pending_cwr_302010203
        self.pending_cwr_302010204 = pending_cwr_302010204

        self.pending_cwr_302020300 = pending_cwr_302020300
        self.pending_cwr_302020400 = pending_cwr_302020400
        self.pending_cwr_302020800 = pending_cwr_302020800
        self.pending_cwr_302020900 = pending_cwr_302020900

        self.pending_cwr_302021001 = pending_cwr_302021001
        self.pending_cwr_302021002 = pending_cwr_302021002
        self.pending_cwr_302040100 = pending_cwr_302040100
        self.pending_cwr_302040200 = pending_cwr_302040200

        self.pending_cwr_302040400 = pending_cwr_302040400
        self.pending_cwr_302040500 = pending_cwr_302040500
        self.pending_cwr_302050000 = pending_cwr_302050000
        
        pending_casework_repetition_data=[self.pending_cwr_302010105 , self.pending_cwr_302010202 , self.pending_cwr_302010203 ,
         self.pending_cwr_302010204 , self.pending_cwr_302020300 , self.pending_cwr_302020400 , 
         self.pending_cwr_302020800 , self.pending_cwr_302020900 , self.pending_cwr_302021001 , 
         self.pending_cwr_302021002 , self.pending_cwr_302040100 , self.pending_cwr_302040200 , 
         self.pending_cwr_302040400 , self.pending_cwr_302040500 , self.pending_cwr_302050000]

        return pending_casework_repetition_data

    def pending_technical(self,**kwargs):
        pass

    # ---------------------------------------------------------
    
    def after(self, after_401010100 = None ,after_401020400 = None , after_401020600 = None) :
        
        self.after_401010100 = after_401010100
        self.after_401020400 = after_401020400
        self.after_401020600 = after_401020600

        after_data = [self.after_401010100,self.after_401020400,self.after_401020600]
        self.after_jsonify(after_data=after_data)

    def after_jsonify(self,after_data):

        after_table_data ={
            'after_401010100' : after_data[0],
            'after_401020400' : after_data[1],
            'after_401020600' : after_data[2],
        }

        return after_table_data


    def support (self):
        pass

# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

class Release_Data(Collect_Table_Data):
    '''
    
    collect all data and send for calculation
    
    '''


    def __init__(self, raw_data=None, before_table_data=None , pending_casework_table_data=None , after_table_data=None) :
        
        self.raw_data = raw_data   # ورودی های خام ثابت که از کاربر میگیری
        self.before_table_data = before_table_data  # ورودی های جدول که کاربر باید وارد کنه برا قبل اجرا
        self.pending_casework_table_data = pending_casework_table_data   # ورودی های جدول که کاربر باید وارد کنه برا حین اجرا موردی
        self.after_table_data = after_table_data   # ورودی های جدول که کاربر باید وارد کنه برا یعد اجرا
 

    def send(self):


        # this func needs to be called each time for calculation
        # its functionallity is to pack datas and send them all for calculation

        data_pack = {
            'raw_data' : self.raw_data ,
            'before_table_data' : self.before_table_data ,
            'pending_casework_table_data' : self.pending_casework_table_data ,
            'after_table_data' : self.after_table_data,
        }

        # data packed 
        # now its ready for calculation


#this single line of code send data package to the Requirements class 
# inside of Requirements class we call another class to calculate and storage state 
# finally what do we have is a json base Variable of output      
        output = requ(data_pack=data_pack)



        return output