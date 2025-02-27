"""
    DEFUZZYFICATION
    mengubah nilai fuzzy menjadi crisp menggunakan metode centroid
    N(member_value[N] * rule_value[N])/member_value[N] + member_value[N+1]
"""
"""
    NILAI INFERENCE
1   sangat_bersih   -> 0% 
2   bersih          -> 12.5%
3   cukup_bersih    -> 25%
4   sedikit_bersih  -> 37.5%
5   rata_rata       -> 50%
6   sedikit_kotor   -> 62.5%
7   cukup_kotor     -> 75%
8   kotor           -> 87.5%
9   sangat_kotor    -> 100%
"""
# def crisp(member1:float,member2:float,member3:float,member4:float)->int:
#     defuzzy = (member1 * 0) + (member2 * 40) + (member3 * 60) + (member4 * 100)
#     print(member1)
#     print(member2)
#     result = defuzzy/(member1 + member2 + member3 + member4)
#     return result

def actual(fuzzy:list) -> int:
    sum_inf = (fuzzy[0] * 0) + (fuzzy[1] * 40) + (fuzzy[2] * 60) + (fuzzy[3] * 100)
    sum_div = sum(fuzzy)
    result = sum_inf/sum_div
    return int(result)        

def crisp(inference:dict)->float:
    sangat_bersih = sum(inference['sangat_bersih'])
    bersih = sum(inference['bersih'])
    cukup_bersih = sum(inference['cukup_bersih'])
    sedikit_bersih = sum(inference['sedikit_bersih'])
    rata_rata = sum(inference['rata_rata'])
    sedikit_kotor = sum(inference['sedikit_kotor'])
    cukup_kotor = sum(inference['cukup_kotor'])
    kotor = sum(inference['kotor'])
    sangat_kotor = sum(inference['sangat_kotor'])
    
    print(f"""
          DEFUZZ
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
    
    sum_inference = (sangat_bersih * 0) + (bersih * 12.5) + (cukup_bersih * 25) + (sedikit_bersih * 37.5) + (rata_rata * 50) + (sedikit_kotor * 62.5) + (cukup_kotor * 75) + (kotor * 87.5) + (sangat_kotor * 100)
    sum_divide = sangat_bersih + bersih + cukup_bersih + sedikit_bersih + rata_rata + sedikit_kotor + cukup_kotor + kotor + sangat_kotor
    result = sum_inference/sum_divide
    print(f"""
          OUTPUT
          sum inference : {sum_inference}
          sum divide    : {sum_divide}
          result        : {result}
          """)
    return result    