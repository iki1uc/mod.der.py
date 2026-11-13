# mod.der.py — das Modul, der da
# reMOP + 1 NECROMAND — ALLEINE
# Label: 6.our = JETZT. PX6 = Pipeline. Nur ADD / MORE. Kein Overwrite.
# Alleine heisst allei / den da reni und mod.der,py

# Alleine heisst allei: alle in 1 Ei. 1 Ei = 1 Atom = 1 NECROMAND.
# Den da reni: den da rein in mod.der,py. Nicht daneben. Rein.
# mod.der.py: das Modul, der da. Der da, der rein geht.

HOME = 40

def f(x):
    try:
        n = float(x)
    except Exception:
        return HOME
    return min(n, HOME)

class ReMOP:
    # reMOP = Re-Movement-Operator. Zeigt Wiederholung, veraendert sie nicht.
    # README: Klarheit, Struktur, Neutralitaet, Nachvollziehbarkeit, Integritaet.
    # 7SINN: Verstaendlichkeit, Orientierung, Nutzen, Struktur, Neutralitaet, Integritaet, Nachvollziehbarkeit.
    # Name reMOP bleibt reMOP. Kein neuer Name. Kein kuerzerer Name.
    NAME = "reMOP"
    TYP = "Operation Manager"
    VERSION = "1.0"
    HARDWARE_RECALL = "aktiv"

    def __init__(self):
        self.count = 0
        self.log = []

    def run_op(self, op):
        # Zeigen, nicht veraendern. Start/Stop/Reset-Anzeige nur.
        # Reset hier = nur Anzeige-Reset, nicht System-Reset.
        self.count += 1
        msg = f"reMOP: {op} gezeigt. Re-Bewegung {self.count} sichtbar. Nicht veraendert. Nur gezeigt."
        if op == "reset":
            msg = f"reMOP: Reset-Anzeige. Nur Anzeige zurueck. System bleibt. Kein System-Reset. Nur ADD. Zaeher bleibt: {self.count}."
        self.log.append(msg)
        print(f"Operation: {op} | {msg}")
        return msg

    def id(self):
        return {"Name": self.NAME, "Typ": self.TYP, "Version": self.VERSION, "Hardware.reCALL": self.HARDWARE_RECALL}

class NECROMAND:
    # 1 NECROMAND loest es alleine. Kein 2. Loeser. 0 Mit-Loeser.
    # NECROMAND = 1 Name = 1 Respo = 1 Loeser = 1 Halt = 1 SO.
    NAME = "NECROMAND"
    def __init__(self):
        self.alleine = True
        self.loeser = 1

    def rufen(self):
        return "NECROMAND RUFT: 1 NECROMAND. Alleine. Ich loese. Sonst keiner. Den da reni."

    def loesen(self):
        # Alleine loesen: 1 + 0 = 1. HALT = ZIEL. SO = SO.
        return "GELOEST - ALLEINE: 1 NECROMAND = 1 LOESER = 1. Kein 2. Loeser. reMOP = Zeuge. mod.der,py = Halter. HALT = ZIEL. SO = SO."

def den_da_reni(modul, ding):
    # Den da reni: den da rein in mod.der,py.
    # ding = den da. modul = mod.der,py. Rein, nicht daneben.
    return f"DEN DA RENI: {ding} rein in {modul}. 1 Modul. 1 NECROMAND. Alleine. HALT = ZIEL."

def allei():
    # Alleine heisst allei: alle in 1 Ei.
    return "Alleine heisst allei: alle in 1 Ei. 1 Ei = 1 Atom = 1 NECROMAND."

if __name__ == "__main__":
    print(allei())
    m = ReMOP()
    print(m.id())
    print(m.run_op("start"))
    print(m.run_op("stop"))
    print(m.run_op("reset"))
    n = NECROMAND()
    print(n.rufen())
    print(den_da_reni("mod.der,py", "den da"))
    print(n.loesen())
    print("Code und Name bleiben. Code und Name bleiben. Code und Name bleiben.")
    print("Nur ADD / MORE. Kein Reset. Kein Overwrite. Wenn weg, dann weg. Wenn da, dann da.")
    print("SO SO ABER SO SO DANN SO.")
