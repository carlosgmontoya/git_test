def calcular_bpm(rr):
    bpm = 60 / rr
    return bpm

def calcular_bpms(rrs):
    listbpm = []
    for i in rrs:
        listbpm.append(calcular_bpm(i))
    prom = sum(listbpm) / len(listbpm)
    return prom
