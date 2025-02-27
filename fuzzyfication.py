import numpy as np
import skfuzzy as fuzzy

def fuzzy_PM25(value:float) -> dict:
    """ 
    Tingkat Kebersihan
    bersih          -> 0 - 10
    sedikit bersih  -> 10 - 19
    sedikit kotor   -> 19 - 30 / 19 - 35
    kotor           -> 30 - 35  / > 35
    
    Standar Keanggotaan PM2.5
    bersih          -> 0 - 0 - 10
    sedikit bersih  -> 0 - 10 - 12 - 19
    sedikit kotor   -> 12 - 19 - 30 - 35
    kotor           -> 30 - 35 - 200
    """
    range_PM25 = np.arange(0,201,1)
    data = {
        "bersih":float,
        "sedikit_bersih":float,
        "sedikit_kotor":float,
        "kotor":float        
    }
    
    # data['bersih'] = fuzzy.trapmf(range_PM25,[0,0,15,30])
    # data['sedikit_bersih'] = fuzzy.trapmf(range_PM25,[15,30,65,80])
    # data["sedikit_kotor"] = fuzzy.trapmf(range_PM25,[65,80,150,165])
    # data['kotor'] = fuzzy.trapmf(range_PM25,[150,165,200,200])
    
    data['bersih'] = fuzzy.trimf(range_PM25,[0,0,10])
    data['sedikit_bersih'] = fuzzy.trapmf(range_PM25,[0,10,12,19])
    data["sedikit_kotor"] = fuzzy.trapmf(range_PM25,[12,19,27,35])
    data['kotor'] = fuzzy.trapmf(range_PM25,[27,35,200,200])
    
    data["bersih"] = float(fuzzy.interp_membership(range_PM25,data["bersih"],value))
    data['sedikit_bersih'] = float(fuzzy.interp_membership(range_PM25,data["sedikit_bersih"],value))
    data["sedikit_kotor"] = float(fuzzy.interp_membership(range_PM25,data["sedikit_kotor"],value))
    data["kotor"] = float(fuzzy.interp_membership(range_PM25,data["kotor"],value))
    
    print(f"""
          DATA
          PM25  : {data}
          """)
    
    return data

def fuzzy_PM10(value:float) -> dict:
    """ 
    Tingkat Kebersihan PM2.5
    bersih          -> 0 - 22
    sedikit bersih  -> 22 - 41
    sedikit kotor   -> 41 - 75
    kotor           -> 75 - 110 / > 75 
    
    Standar Keanggotaan PM2.5
    bersih          -> 0 - 0 - 10 - 22
    sedikit bersih  -> 10 - 22 - 30 - 41
    sedikit kotor   -> 30 - 41 - 60 - 75
    kotor           -> 60 - 75 - 500 - 500
    """
    range_PM10 = np.arange(0,501,1)
    data = {
        "bersih":float,
        "sedikit_bersih":float,
        "sedikit_kotor":float,
        "kotor":float
    }
    
    data['bersih'] = fuzzy.trapmf(range_PM10,[0,0,10,22])
    data['sedikit_bersih'] = fuzzy.trapmf(range_PM10,[10,22,30,41])
    data["sedikit_kotor"] = fuzzy.trapmf(range_PM10,[30,41,60,75])
    data['kotor'] = fuzzy.trapmf(range_PM10,[60,75,500,500])
    
    data["bersih"] = float(fuzzy.interp_membership(range_PM10,data["bersih"],value))
    data['sedikit_bersih'] = float(fuzzy.interp_membership(range_PM10,data["sedikit_bersih"],value))
    data["sedikit_kotor"] = float(fuzzy.interp_membership(range_PM10,data["sedikit_kotor"],value))
    data["kotor"] = float(fuzzy.interp_membership(range_PM10,data["kotor"],value))
    
    print(f"""
          DATA
          PM10  : {data}
          """)
    
    return data

def fuzzy_MQ2(value:float)-> dict:
    range_MQ2 = np.arange(0,1001,1)
    data = {
        "aman":float,
        "peringatan":float,
        "bahaya":float
    }
    
    data['aman'] = fuzzy.trapmf(range_MQ2,[0,0,300,450])
    data['peringatan'] = fuzzy.trimf(range_MQ2,[300,450,600])
    data['bahaya'] = fuzzy.trapmf(range_MQ2,[450,600,1000,1000])
    
    data['aman'] = float(fuzzy.interp_membership(range_MQ2,data["aman"],value))
    data['peringatan'] = float(fuzzy.interp_membership(range_MQ2,data['peringatan'],value))
    data['bahaya'] = float(fuzzy.interp_membership(range_MQ2,data["bahaya"],value))
    
    print(f"""
          DATA
          MQ2  : {data}
          """)
    
    return data