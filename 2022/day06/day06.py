packet = False
with open("input", "r") as f:
    signal = f.read().strip()
    for i in range(0, len(signal)):
        if len(set(signal[i:i+4])) == 4 and not packet:
            print("packet", i+4)
            packet=True
        if len(set(signal[i:i+14])) == 14:
            print("signal", i+14) 
            break

