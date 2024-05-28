# Trafik Simülasyonu Projesi

Bu proje, SUMO (Simulation of Urban MObility) kullanarak kentsel trafik akışını modellemeyi ve analiz etmeyi amaçlamaktadır. Proje kapsamında trafik ışıklarının kontrolü, trafik akışının analizi ve paket teslim oranının değerlendirilmesi gibi hedefler gerçekleştirilmiştir.

## İçindekiler

- [Giriş](#giriş)
- [Gereksinimler](#gereksinimler)
- [Kurulum](#kurulum)
- [Kullanım](#kullanım)
- [Proje Adımları](#proje-adımları)
  - [Veri Toplama ve Hazırlık](#veri-toplama-ve-hazırlık)
  - [TLS Tanımlama](#tls-tanımlama)
  - [Simülasyonun Çalıştırılması](#simülasyonun-çalıştırılması)
  - [Performans Değerlendirmesi](#performans-değerlendirmesi)
- [Sonuç ve Öneriler](#sonuç-ve-öneriler)
- [Katkıda Bulunanlar](#katkıda-bulunanlar)
- [Lisans](#lisans)

## Giriş

Bu proje, SUMO kullanarak şehir içi trafik akışını modellemeyi ve analiz etmeyi amaçlamaktadır. SUMO, açık kaynak kodlu bir trafik simülasyon yazılımıdır ve şehir içi trafik akışını simüle etmek için kullanılır. Proje, trafik ışıklarının doğru şekilde modellenmesi, trafik akışının analizi ve paket teslim oranının değerlendirilmesi gibi hedefler içermektedir.

## Gereksinimler

- Python 3.6+
- SUMO (Simulation of Urban MObility)
- OpenStreetMap (OSM) API
- TraCI (Traffic Control Interface)

## Kurulum

### SUMO Kurulumu

SUMO'yu kurmak için aşağıdaki adımları izleyin:

1. [SUMO'nun resmi sitesinden](https://www.eclipse.org/sumo/) en son sürümünü indirin.
2. Kurulum talimatlarını izleyerek SUMO'yu sisteminize kurun.

### Python Kütüphaneleri

Gerekli Python kütüphanelerini kurmak için aşağıdaki komutu kullanın:

```bash
pip install traci
´´´
## Kullanım

Proje dosyalarını klonlayın ve gerekli kurulumları yaptıktan sonra aşağıdaki adımları izleyerek simülasyonu çalıştırın:

    Harita Verilerinin Çekilmesi:

    OpenStreetMap API'sini kullanarak gerekli harita verilerini çekin. Bunu yapmak için aşağıdaki Python kodunu kullanabilirsiniz:

    python
```bash
import os
import sumolib
from sumolib.net import readNet
from sumolib.output import write

os.system("wget -O map.osm 'https://www.openstreetmap.org/api/0.6/map?bbox=11.54,48.14,11.543,48.145'")

Verilerin SUMO Formatına Dönüştürülmesi:

OpenStreetMap verilerini SUMO formatına dönüştürmek için netconvert aracını kullanın:

bash

netconvert --osm-files map.osm -o map.net.xml

tls.add.xml Dosyasının Oluşturulması:

Trafik ışıklarını tanımlamak için tls.add.xml dosyasını oluşturun. Örnek bir tls.add.xml dosyası aşağıdaki gibidir:

xml

<additional>
  <tlLogic id="traffic_light_1" type="static" programID="1" offset="0">
    <phase duration="31" state="GGggrrrrGGggrrrr"/>
    <phase duration="5"  state="yyggrrrryyggrrrr"/>
    <phase duration="6"  state="rrGGrrrrrrGGrrrr"/>
    <phase duration="5"  state="rryyrrrrrryyrrrr"/>
    <phase duration="31" state="rrrrGGggrrrrGGgg"/>
    <phase duration="5"  state="rrrryyggrrrryygg"/>
    <phase duration="6"  state="rrrrrrGGrrrrrrGG"/>
    <phase duration="5"  state="rrrrrryyrrrrrryy"/>
  </tlLogic>
</additional>

Simülasyonun Başlatılması:

Simülasyonu başlatmak için aşağıdaki komutu kullanın:

bash

sumo-gui -c your_simulation.sumocfg

Alternatif olarak, GUI olmadan simülasyonu çalıştırmak isterseniz:

bash

    sumo -c your_simulation.sumocfg

Test

Simülasyonun doğru çalıştığından emin olmak için aşağıdaki adımları izleyin:

    Simülasyonu çalıştırın ve trafik ışıklarının doğru çalışıp çalışmadığını kontrol edin.
    Trafik akışını gözlemleyin ve gerekli optimizasyonları yapın.

Katkıda Bulunanlar

    İsim Soyisim - Proje Yöneticisi
    İsim Soyisim - Geliştirici
    İsim Soyisim - Veri Analisti
