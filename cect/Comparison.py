import cect

from cect.ConnectomeReader import analyse_connections
from cect.ConnectomeReader import check_neurons

all_data = {}

reader_pages = {"Varshney":"Varshney_data",
                "White_A":"White_A_data",
                "White_L4":"White_L4_data",
                "White_whole":"White_whole_data",
                "Witvliet1":"Witvliet1_data",
                "Witvliet2":"Witvliet2_data",
                "WormNeuroAtlas":"WormNeuroAtlas_data",
                "Cook2019Herm":"Cook2019Herm_data",
                "":"_data",
                }

all_data[""] =["Num neurons", 
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
           "Varshney": "cect.VarshneyDataReader",
           "White_L4": "cect.White_L4", 
          }
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


# TODO: move elsewhere and make more generic
def get_cell_link(cell_name):

    url = None

    known_indiv = ['SABD']
    
    if cell_name in known_indiv:
        url = 'https://www.wormatlas.org/neurons/Individual Neurons/%sframeset.html'%cell_name
    elif cell_name[-2:].isnumeric():
        url = 'https://www.wormatlas.org/neurons/Individual Neurons/%sframeset.html'%cell_name[:-2]
    elif cell_name[-1].isdigit():
        url = 'https://www.wormatlas.org/neurons/Individual Neurons/%sframeset.html'%cell_name[:-1]
    elif len(cell_name)==3:
        url = 'https://www.wormatlas.org/neurons/Individual Neurons/%sframeset.html'%cell_name
    elif cell_name.endswith('L') or cell_name.endswith('R') or cell_name.endswith('EV') or cell_name.endswith('ED') or cell_name.endswith('BD'):
        url = 'https://www.wormatlas.org/neurons/Individual Neurons/%sframeset.html'%cell_name[:-1]

    if url is not None:
        return '[%s](%s)'%(cell_name, url)
    else:
        return cell_name
    


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

    ref = '[%s](%s.md)'%(name,reader_pages[name]) if name in reader_pages else name

    if name in reader_pages:
        with open('docs/%s.md'%reader_pages[name], 'w') as f:
            f.write('## %s\n'%name)

            cells = {'Neurons': preferred, 
                     "Missing neurons": missing_preferred, 
                     "Muscles": muscles}

            for t in cells:
                f.write('\n### %s (%i)\n| '%(t,len(cells[t])))
                for n in sorted(cells[t]):
                    f.write('%s | '%(get_cell_link(n)))


    all_data[ref] =[len(preferred),
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

df_all = pd.DataFrame(all_data).transpose()
#df_all.set_index("Values")

#h = HTML(df_all.to_html(escape=False, index=False))

mk = df_all.to_markdown()

with open('docs/Comparison.md', 'w') as f:
    f.write(mk)

