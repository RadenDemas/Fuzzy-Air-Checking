"""
    FUZZY RULE (PM2.5)
    IF bersih THEN udara_bersih 0 - 15                      -> 0 - 15 - 30
    IF sedikit_bersih THEN udara_sedikit_bersih 16 - 65 + 15-> 15 - 30 - 65 - 80
    IF sedikit_kotor THEN udara_sedikit_kotor 66 - 150 + 15 -> 65 - 80 - 150 - 165 
    IF kotor THEN kotor > 150                               -> >150
    Data by BMKG
"""
"""
    FUZZY RULE (PM10)
    IF bersih THEN udara_bersih 0 - 50                      -> 0 - 50 - 50 - 75         / 0 - 0 - 40 - 70
    IF sedikit_bersih THEN udara_sedikit_bersih 51 - 150    -> 0 - 50 - 75 - 150 - 175  / 40 - 70 - 140 - 170  
    IF sedikit_kotor THEN udara_sedikit_kotor 151 - 350     -> 150 - 175 - 350 - 375    / 140 - 170 - 340 - 370  
    IF kotor THEN kotor 351 - 420                           -> 350 - 375 - 500 - 500    / 340 - 370 - 500 - 500
    Data by BMKG
"""
#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
"""
    FUZZY RULE (MQ2)
    IF aman THEN udara_bersih 0 - 300 ppm -> speed 0% -> bersih
    IF peringatan THEN udara_sedikit_kotor 300 - 600 ppm -> speed 50% -> sedikit_bersih & sedikit_kotor
    IF bahaya THEN udara kotor 600> ppm -> speed 100% -> cukup kotor
    Data by 
"""
#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
"""
    NILAI INFERENCE
1   sangat_bersih -> 0% 
2   bersih -> 12.5%
3   cukup_bersih -> 25%
4   sedikit_bersih -> 37.5%
5   rata_rata -> 50%
6   sedikit_kotor -> 62.5%
7   cukup_kotor -> 75%
8   kotor -> 87.5%
9   sangat_kotor -> 100%
"""
#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
"""
    INFERENCE RULE FOR PM2.5 AND PM10
    bersih          + bersih            = sangat_bersih
================================================================
    bersih          + sedikit_bersih    = bersih
    bersih          + sedikit_kotor     = cukup_bersih
    bersih          + kotor             = rata_rata
================================================================
    sedikit_bersih  + sedikit_bersih    = sedikit_bersih
    sedikit_bersih  + sedikit_kotor     = rata_rata
    sedikit_bersih  + kotor             = cukup_kotor
================================================================
    sedikit_kotor   + sedikit_kotor     = sedikit_kotor
    sedikit_kotor   + kotor             = kotor
================================================================
    kotor           + kotor             = sangat kotor
"""
#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
"""
    FUZZY RULE PM (PM2.5,PM10)
1     IF PM2.5 bersih         AND PM10 bersih         THEN sangat_bersih
2     IF PM2.5 bersih         AND PM10 sedikit_bersih THEN bersih
3     IF PM2.5 bersih         AND PM10 sedikit_kotor  THEN cukup_bersih
4     IF PM2.5 bersih         AND PM10 kotor          THEN sedikit_bersih
5     IF PM2.5 sedikit_bersih AND PM10 bersih         THEN bersih
6     IF PM2.5 sedikit_bersih AND PM10 sedikit_bersih THEM sedikit_bersih
7     IF PM2.5 sedikit_bersih AND PM10 sedikit_kotor  THEN rata_rata
8     IF PM2.5 sedikit_bersih AND PM10 kotor          THEN cukup_kotor
9     IF PM2.5 sedikit_kotor  AND PM10 bersih         THEN cukup_bersih
10    IF PM2.5 sedikit_kotor  AND PM10 sedikit_bersih THEN rata_rata
11    IF PM2.5 sedikit_kotor  AND PM10 sedikit_kotor  THEN sedikit_kotor
12    IF PM2.5 sedikit_kotor  AND PM10 kotor          THEN kotor
13    IF PM2.5 kotor          AND PM10 bersih         THEN rata-rata
14    IF PM2.5 kotor          AND PM10 sedikit_bersih THEN cukup_kotor
15    IF PM2.5 kotor          AND PM10 sedikit_kotor  THEN kotor
16    IF PM2.5 kotor          AND PM10 kotor          THEN sangat_kotor
"""
#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
"""
    INFERENCE RULE FOR RULE PM (PM2.5&PM10) AND MQ2
    sangat_bersih   + aman          = sangat_bersih
    sangat_bersih   + peringatan    = rata_rata
    sangat_bersih   + bahaya        = kotor
================================================================
    bersih          + aman          = bersih
    bersih          + peringatan    = sedikit_kotor
    bersih          + bahaya        = kotor
================================================================
    cukup_bersih    + aman          = cukup_bersih
    cukup_bersih    + peringatan    = sedikit_kotor
    cukup_bersih    + bahaya        = kotor
================================================================
    sedikit_bersih  + aman          = sedikit_berish
    sedikit_bersih  + peringatan    = kotor
    sedikit_bersih  + bahaya        = sangat_kotor
================================================================
    rata-rata       + aman          = rata_rata
    rata-rata       + peringatan    = kotor
    rata-rata       + bahaya        = sangat_kotor
================================================================
    sedikit_kotor   + aman          = sedikit_kotor
    sedikit_kotor   + peringatan    = sangat_kotor
    sedikit_kotor   + bahaya        = sangat_kotor
================================================================
    cukup_kotor     + aman          = cukup_kotor
    cukup_kotor     + peringatan    = sangat_kotor
    cukup_kotor     + bahaya        = sangat_kotor
================================================================
    kotor           + aman          = kotor
    kotor           + peringatan    = sangat_kotor
    kotor           + bahaya        = sangat_kotor
================================================================
    sangat_kotor    + aman          = sangat_kotor
    sangat_kotor    + peringatan    = sangat_kotor
    sangat_kotor    + bahaya        = sangat_kotor
"""
#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
"""
    FUZZY RULE (PM(PM2.5,PM10),MQ2)
    IF PM sangat_bersih     OR  MQ2 aman        THEN sangat_bersih
    IF PM sangat_bersih     AND MQ2 peringatan  THEN rata_rata
    IF PM sangat_bersih     AND MQ2 bahaya      THEN kotor
================================================================    
    IF PM bersih            OR  MQ2 aman        THEN bersih
    IF PM bersih            AND MQ2 peringatan  THEN sedikit_kotor
    IF PM bersih            AND MQ2 bahaya      THEN sangat_kotor
================================================================    
    IF PM cukup_bersih      OR  MQ2 aman        THEN cukup_bersih
    IF PM cukup_bersih      AND MQ2 peringatan  THEN cukup_kotor
    IF PM cukup_bersih      AND MQ2 bahaya      THEN sangat_kotor
================================================================
    IF PM sedikit_bersih    OR  MQ2 aman        THEN sedikit_bersih
    IF PM sedikit_bersih    AND MQ2 peringatan  THEN kotor
    IF PM sedikit_bersih    AND MQ2 bahaya      THEN sangat_kotor
================================================================
    iF PM rata_rata         OR  MQ2 aman        THEN rata_rata
    iF PM rata_rata         AND MQ2 peringatan  THEN sangat_kotor
    iF PM rata_rata         AND MQ2 bahaya      THEN sangat_kotor
================================================================
    IF PM sedikit_kotor     OR  MQ2 aman        THEN sedikit_kotor
    IF PM sedikit_kotor     AND MQ2 peringatan  THEN sangat_kotor
    IF PM sedikit_kotor     AND MQ2 bahaya      THEN sangat_kotor
================================================================
    IF PM cukup_kotor       OR  MQ2 aman        THEN cukup_kotor
    IF PM cukup_kotor       AND MQ2 peringatan  THEN sangat_kotor
    IF PM cukup_kotor       AND MQ2 bahaya      THEN sangat_kotor
================================================================
    IF PM kotor             OR  MQ2 aman        THEN kotor
    IF PM kotor             AND MQ2 peringatan  THEN sangat_kotor
    IF PM kotor             AND MQ2 bahaya      THEN sangat_kotor
================================================================
    If PM sangat_kotor      OR  MQ2 aman        THEN sangat_kotor
    If PM sangat_kotor      AND MQ2 peringatan  THEN sangat_kotor
    If PM sangat_kotor      AND MQ2 bahaya      THEN sangat_kotor
"""

def rule(PM25:dict,PM10:dict,MQ2:dict) -> dict:
    inference = {
        "sangat_bersih":[],
        "bersih":[],
        "cukup_bersih":[],
        "sedikit_bersih":[],
        "rata_rata":[],
        "sedikit_kotor":[],
        "cukup_kotor":[],
        "kotor":[],
        "sangat_kotor":[]
    }
    rulePM1  = min(PM25['bersih'],PM10['bersih'])                   #-> sangat_bersih
    rulePM2  = min(PM25['bersih'],PM10['sedikit_bersih'])           #-> bersih
    rulePM3  = min(PM25['bersih'],PM10['sedikit_kotor'])            #-> cukup_bersih
    rulePM4  = min(PM25['bersih'],PM10['kotor'])                    #-> sedikit_bersih -> rata_rata
    rulePM5  = min(PM25['sedikit_bersih'],PM10['bersih'])           #-> bersih
    rulePM6  = min(PM25['sedikit_bersih'],PM10['sedikit_bersih'])   #-> sedikit_bersih
    rulePM7  = min(PM25['sedikit_bersih'],PM10['sedikit_kotor'])    #-> rata_rata
    rulePM8  = min(PM25['sedikit_bersih'],PM10['kotor'])            #-> cukup_kotor
    rulePM9  = min(PM25['sedikit_kotor'],PM10['bersih'])            #-> cukup_bersih
    rulePM10 = min(PM25['sedikit_kotor'],PM10['sedikit_bersih'])    #-> rata_rata
    rulePM11 = min(PM25['sedikit_kotor'],PM10['sedikit_kotor'])     #-> sedikit_kotor
    rulePM12 = min(PM25['sedikit_kotor'],PM10['kotor'])             #-> kotor
    rulePM13 = min(PM25['kotor'],PM10['bersih'])                    #-> rata rata
    rulePM14 = min(PM25['kotor'],PM10['sedikit_bersih'])            #-> sedikit_kotor
    rulePM15 = min(PM25['kotor'],PM10['sedikit_kotor'])             #-> kotor
    rulePM16 = min(PM25['kotor'],PM10['kotor'])                     #-> sangat_kotor
    
    ruleMQ1 = min(rulePM1, MQ2['aman'])         #sangat_bersih
    ruleMQ2 = min(rulePM1, MQ2['peringatan'])   #rata_rata
    ruleMQ3 = min(rulePM1, MQ2['bahaya'])       #kotor
    
    ruleMQ4 = min(rulePM2, MQ2['aman'])         #bersih
    ruleMQ5 = min(rulePM2, MQ2['peringatan'])   #sedikit_kotor
    ruleMQ6 = min(rulePM2, MQ2['bahaya'])       #kotor
    
    ruleMQ7 = min(rulePM3, MQ2['aman'])         #cukup_bersih
    ruleMQ8 = min(rulePM3, MQ2['peringatan'])   #sedikit_kotor
    ruleMQ9 = min(rulePM3, MQ2['bahaya'])       #kotor
    
    ruleMQ10 = min(rulePM4, MQ2['aman'])        #sedikit_bersih
    ruleMQ11 = min(rulePM4, MQ2['peringatan'])  #kotor
    ruleMQ12 = min(rulePM4, MQ2['bahaya'])      #sangat_kotor
    
    ruleMQ13 = min(rulePM5, MQ2['aman'])        #bersih
    ruleMQ14 = min(rulePM5, MQ2['peringatan'])  #sedikit_kotor
    ruleMQ15 = min(rulePM5, MQ2['bahaya'])      #kotor
    
    ruleMQ16 = min(rulePM6, MQ2['aman'])        #sedikit_bersih
    ruleMQ17 = min(rulePM6, MQ2['peringatan'])  #kotor
    ruleMQ18 = min(rulePM6, MQ2['bahaya'])      #sangat_kotor

    ruleMQ19 = min(rulePM7, MQ2['aman'])        #rata_rata
    ruleMQ20 = min(rulePM7, MQ2['peringatan'])  #kotor
    ruleMQ21 = min(rulePM7, MQ2['bahaya'])      #sangat_kotor
    
    ruleMQ22 = min(rulePM8, MQ2['aman'])        #cukup_kotor
    ruleMQ23 = min(rulePM8, MQ2['peringatan'])  #sangat_kotor
    ruleMQ24 = min(rulePM8, MQ2['bahaya'])      #sangat_kotor
    
    ruleMQ25 = min(rulePM9, MQ2['aman'])        #cukup_bersih
    ruleMQ26 = min(rulePM9, MQ2['peringatan'])  #sedikit_kotor
    ruleMQ27 = min(rulePM9, MQ2['bahaya'])      #kotor
    
    ruleMQ28 = min(rulePM10, MQ2['aman'])        #rata_rata
    ruleMQ29 = min(rulePM10, MQ2['peringatan'])  #kotor
    ruleMQ30 = min(rulePM10, MQ2['bahaya'])      #sangat_kotor
    
    ruleMQ31 = min(rulePM11, MQ2['aman'])       #sedikit_kotor
    ruleMQ32 = min(rulePM11, MQ2['peringatan']) #sangat_kotor
    ruleMQ33 = min(rulePM11, MQ2['bahaya'])     #sangat_kotor
    
    ruleMQ34 = min(rulePM12, MQ2['aman'])       #kotor
    ruleMQ35 = min(rulePM12, MQ2['peringatan']) #sangat_kotor
    ruleMQ36 = min(rulePM12, MQ2['bahaya'])     #sangat_kotor
    
    ruleMQ37 = min(rulePM13, MQ2['aman'])       #rata_rata
    ruleMQ38 = min(rulePM13, MQ2['peringatan']) #kotor
    ruleMQ39 = min(rulePM13, MQ2['bahaya'])     #sangat_kotor
    
    ruleMQ40 = min(rulePM14, MQ2['aman'])       #sedikit_kotor
    ruleMQ41 = min(rulePM14, MQ2['peringatan']) #sangat_kotor
    ruleMQ42 = min(rulePM14, MQ2['bahaya'])     #sangat_kotor
    
    ruleMQ43 = min(rulePM15, MQ2['aman'])       #kotor
    ruleMQ44 = min(rulePM15, MQ2['peringatan']) #sangat_kotor
    ruleMQ45 = min(rulePM15, MQ2['bahaya'])     #sangat_kotor
    
    ruleMQ46 = min(rulePM16, MQ2['aman'])       #sangat_kotor
    ruleMQ47 = min(rulePM16, MQ2['peringatan']) #sangat_kotor
    ruleMQ48 = min(rulePM16, MQ2['bahaya'])     #sangat_kotor
    
    sangat_bersih = [ruleMQ1]
    bersih = [ruleMQ4,ruleMQ13]
    cukup_bersih = [ruleMQ7,ruleMQ25]
    sedikit_bersih = [ruleMQ10,ruleMQ16]
    rata_rata = [ruleMQ2,ruleMQ19,ruleMQ28,ruleMQ37]
    sedikit_kotor = [ruleMQ5,ruleMQ8,ruleMQ14,ruleMQ26,ruleMQ31,ruleMQ40]
    cukup_kotor = [ruleMQ22]
    kotor = [ruleMQ3, ruleMQ6, ruleMQ9, ruleMQ11, ruleMQ15, ruleMQ17, ruleMQ20, ruleMQ27,ruleMQ29,ruleMQ34,ruleMQ38,ruleMQ43]
    sangat_kotor = [ruleMQ12,ruleMQ18,ruleMQ21,ruleMQ23,ruleMQ24,ruleMQ30,ruleMQ32,ruleMQ33,ruleMQ35,ruleMQ36,ruleMQ39,ruleMQ41,ruleMQ42,ruleMQ44,ruleMQ45,ruleMQ46,ruleMQ47,ruleMQ48]
    
    print(f"""
          INFERENCE
          sangat bersih : {sangat_bersih}
          bersih        : {bersih}
          cukup bersih  : {cukup_bersih}
          sedikit bersih: {sedikit_bersih}
          rata rata     : {rata_rata}
          sedikit kotor : {sedikit_kotor}
          cukup kotor   : {cukup_kotor}
          kotor         : {kotor}
          sangat kotor  : {sangat_kotor}
          """)
    
    inference['sangat_bersih'].extend(sangat_bersih)
    inference['bersih'].extend(bersih)
    inference['cukup_bersih'].extend(cukup_bersih)
    inference['sedikit_bersih'].extend(sedikit_bersih)
    inference['rata_rata'].extend(rata_rata)
    inference['sedikit_kotor'].extend(sedikit_kotor)
    inference['cukup_kotor'].extend(cukup_kotor)
    inference['kotor'].extend(kotor)
    inference['sangat_kotor'].extend(sangat_kotor)
    
    return inference
def rule1(x:float)->float:
    if x>0:
        return x
    else:
        return x
    
def rule2(x:float)->float:
    if x>0:
        return x
    else:
        return x

def rule3(x:float)->float:
    if x>0:
        return x
    else:
        return x

def rule4(x:float)->float:
    if x>0:
        return x
    else:
        return x