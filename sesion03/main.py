import ppg


rrs_list = [0.8, 0.9, 1.0, 1.1]

bpm = ppg.calcular_bpm(0.8)
print("BPM calculado:", bpm)


bpm_prom = ppg.calcular_bpms(rrs_list)
print("Promedio de BPM:", bpm_prom)