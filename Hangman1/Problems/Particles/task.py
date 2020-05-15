#  Posted from EduTools plugin
particle = ["Strange Quark", "Charm Quark", 'Electron Lepton', 'Muon Lepton', 'Photon Boson', 'Higgs boson Boson']
spin = ['1/2', '1', '0']
charge = ['-1/3', '2/3', '-1', '0']
x_spin = input()
y_charge = input()

if x_spin == spin[0]:
    if y_charge == charge[0]:
        print(particle[0])
    elif y_charge == charge[1]:
        print(particle[1])
    elif y_charge == charge[2]:
        print(particle[2])
    elif y_charge == charge[3]:
        print(particle[3])

elif x_spin == spin[1] and y_charge == charge[3]:
    print(particle[4])
elif x_spin == spin[2] and y_charge == charge[3]:
    print(particle[5])
else:
    print("Irgendeine Eingabe passt nicht")


# print(type(x1))
# print(type(x2))

