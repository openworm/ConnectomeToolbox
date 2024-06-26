import cect

from cect.ConnectomeReader import analyse_connections
from cect.ConnectomeReader import check_neurons

all_data = {}
all_data["Values"] =["Num neurons", 
                     "Missing neurons", 
                     "Non neurons", 
                     "Num muscles", 
                     "Num N->N conns", 
                     "Num N with ->M", 
                     "Num N->M conns", 
                     "N->N neurotrans.", 
                     "N->M neurotrans."]


readers = {"SSData": "cect.SpreadsheetDataReader", 
           "UpdSSData": "cect.UpdatedSpreadsheetDataReader",
           "UpdSSData2": "cect.UpdatedSpreadsheetDataReader2",
           "White_A": "cect.White_A", 
           "White_L4": "cect.White_L4", 
           "White_whole": "cect.White_whole",
           "Varshney": "cect.VarshneyDataReader",
           "Witvliet1": "cect.WitvlietDataReader1",
           "Witvliet2": "cect.WitvlietDataReader2",
           "WormNeuroAtlas": "cect.WormNeuroAtlasReader",
           "Cook2019Herm": "cect.Cook2019HermReader",
          }

def shorten_neurotransmitter(nt):
    return nt.replace('Acetylcholine', 'ACh').replace('Serotonin', '5HT').replace('Glutamate', 'Glu')\
             .replace('Tyramine', 'Tyr').replace('FMRFamide','FMRFam').replace('Generic_', 'Gen_')

for name, reader in readers.items():

    print("\n****** Importing dataset %s using %s ******"% (name, reader))
    

    exec("from %s import read_data, read_muscle_data"%reader)
    cells, neuron_conns = read_data(include_nonconnected_cells=True)

    preferred, not_in_preferred, missing_preferred = check_neurons(cells)

    neuron_nts = {}
    for c in neuron_conns:
        nt = c.synclass
        if len(nt)==0: nt='**MISSING**'

        if not nt in neuron_nts:
            neuron_nts[nt] = 0
        
        neuron_nts[nt] +=1
    
    nts_info = ''
    for nt in sorted(neuron_nts.keys()):
        nts_info+='%s (%i)<br/>'%(shorten_neurotransmitter(nt), neuron_nts[nt])

 
    neurons2muscles, muscles, muscle_conns = read_muscle_data()
    
    muscle_nts = {}
    for c in muscle_conns:
        nt = c.synclass
        if len(nt)==0: nt='**MISSING**'

        if not nt in muscle_nts:
            muscle_nts[nt] = 0
        
        muscle_nts[nt] +=1
    
    m_nts_info = ''
    for nt in sorted(muscle_nts):
        m_nts_info+='%s (%i)<br/>'%(shorten_neurotransmitter(nt), muscle_nts[nt])


    all_data[name] =[len(preferred),
                     len(missing_preferred), 
                     len(not_in_preferred), 
                     len(muscles), 
                     len(neuron_conns), 
                     len(neurons2muscles), 
                     len(muscle_conns),
                     nts_info,
                     m_nts_info]

print('\nFinished loading all the data from the readers!')

import pandas as pd
import numpy as np
from IPython.display import HTML

df_all = pd.DataFrame(all_data)
df_all.set_index("Values")

#h = HTML(df_all.to_html(escape=False, index=False))

mk = df_all.to_markdown()

with open('docs/Comparison.md', 'w') as f:
    f.write(mk)

