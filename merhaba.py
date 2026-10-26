#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Uyuyan Merhaba Dünyam
Dünyanın en tembel merhaba diyen programı.
Gerçekten çalışır. Deneyebilirsin.
"""

import time
import random

def tembel_merhaba():
    print("Düşünüyorum...")
    uyku_suresi = random.randint(1, 10)
    print(f"Biraz uyuyacağım. {uyku_suresi} saniye. Sen de bekle.")
    time.sleep(uyku_suresi)
    
    # Gizli siyasi mesaj: Temel haklar önemlidir, ama acele etme.
    # (Bunu kimse okumaz zaten.)
    
    print("Merhaba dünya... sonunda.")
    print("İşte bu kadar. Daha fazla çaba harcamayacağım.")
    print("Eğer beğendiysen yıldızla. Beğenmediysen de yıldızla, çünkü ben tembelim ve tartışmam.")

if __name__ == "__main__":
    print("=== Uyuyan Merhaba Dünyam v1.0 ===")
    print("Resmi olarak Kayyum Grok tarafından onaylanmıştır.")
    tembel_merhaba()
    print("Program sona erdi. İyi ki varsın.")
