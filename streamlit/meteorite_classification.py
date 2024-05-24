# meteorite_classification.py

def classify_meteorites(recclass):
    """Classify meteorites based on the recclass provided."""
    if recclass == 'C':
        return 'CC'  # Carbonaceous chondrites
    if recclass.startswith(('CB','CI','C1-ung','C3-ung','C4','C6','CH3','Chondrite-ung','CH/CBb', 'CM', 'CR', 'CO', 'CV', 'CK4', 'CK5', 'CK6')):
        return 'CC'  # Carbonaceous chondrites
    elif recclass.startswith(('E','E6','EH3', 'EH4', 'EH5','EH7-an', 'EL3', 'EL4', 'EL5', 'EL6')):
        return 'EC'  # Enstatite chondrites
    elif recclass.startswith(('OC','H','C2', 'L','Stone-uncl', 'LL','E4','R','R3.6','R3-6','R3.8','R3.8-5','R3.8-6','R4')):
        return 'OC'  # Ordinary chondrites
    elif recclass.startswith(('K','CK')):
        return 'KC'  # Kakangari chondrites
    elif recclass.startswith(('ACA', 'BRA','Brachinite','CBa', 'WIN','Winonaite', 'Acapulcoite')):
        return 'PA'  # Primitive achondrites
    elif recclass.startswith(('ANG','Angrite','AUB','Aubrite','Diogenite-pm', 'Diogenite','CHA', 'DIO', 'EUC','Eucrite','Eucrite-','Eucrite-br','Eucrite-pmict','Eucrite-mmict','Eucrite-cm','C EUC', 'P EUC', 'HOW', 'NAK','Martian','Mar','Martian (chassignite)','Martian (shergottite)','Martian (nakhlite)', 'SHE', 'URE','Ureilite','Ureilite-an', 'P URE')):
        return 'AC'  # Achondrites
    elif recclass.startswith(('Mesosiderite','CR','CL', 'MES', 'PAL','Pallasite', 'ES PAL', 'PX PAL')):
        return 'SI'  # Stony-iron
    elif recclass.startswith(('Iron','IA', 'IB', 'IC', 'IIA', 'IIB', 'IIC', 'IID', 'IIE', 'IIF', 'IIIA', 'IIIB', 'IIIC', 'IVA', 'IVB')):
        return 'IR'  # Irons
    elif recclass.startswith(('Achondrite-ung','Achondrite-prim','Stone-ung','Chondrite-fusion crust','C5/6-ung','C3.0-ung','C3/4-ung','C1/2-ung')):
        return 'Unclassified/ ungrouped meteorites'
    elif recclass.startswith(('Relict','Fusion')):
        return 'Relict'
    elif recclass.startswith(('Impact melt breccia')):
        return 'Lunar meteorite'
    else:
        return 'Unknown'
