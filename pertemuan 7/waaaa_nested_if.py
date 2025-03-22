def waa(HPP,DMGP,HPM,DMGM):
    while HPM or HPP > 0:
        if HPM > 0:
            print(f"HP moster = {HPM} - {DMGP}")
            HPM = HPM - DMGP
            if HPM > 0:
                print("oh moster masih hidup = nyerang pahlawan")
            elif HPM <= 0:
                return "koid"
        if HPP > 0:
            print(f"HP pahlawan= {HPP} - {DMGM}")
            HPP = HPP - DMGM
            if HPP > 0:
                print("oh pahlawan masih hidup = nyerang moster")
            elif HPP <= 0:
                return "cupu bettttttttttttttttt"
        
print(waa(100,10,50,50))
