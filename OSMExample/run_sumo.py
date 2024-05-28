import traci
import sumolib

def control_traffic_lights():
    # SUMO haritasını yükle
    net = sumolib.net.readNet("map.net.xml")

    # Trafik ışıklarının listesini al
    traffic_lights = net.getTrafficLights()

    # Trafik ışıklarını yeşil ışık moduna geçir
    for tl in traffic_lights:
        traci.trafficlight.setRedYellowGreenState(tl.getID(), "GrGr")  # Örnek olarak "GrGr" (yeşil ışık) durumuna geçiriyoruz

    # Diğer trafik ışığı kontrollerini buraya ekleyebilirsiniz

# SUMO simülasyonunu başlat
sumoBinary = sumolib.checkBinary('sumo-gui')
traci.start([sumoBinary, "-c", "simple.sumocfg"])

# Trafik ışıklarını kontrol etmek için fonksiyonu çağır
control_traffic_lights()


