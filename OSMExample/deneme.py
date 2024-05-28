import sumolib

# SUMO haritasını yükle
net = sumolib.net.readNet("map.net.xml")

# Trafik ışıklarının listesini al
traffic_lights = net.getTrafficLights()

# Trafik ışıklarının ID'lerini yazdır
for tl in traffic_lights:
    print("Traffic light ID:", tl.getID())

#deeneme