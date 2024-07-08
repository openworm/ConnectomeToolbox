import plotly.express as px
import numpy as np


def convert_to_array(cells,neuron_conns):
    num1 = []
    for i in cells:
        num1.append([])
        for j in cells:
            num1[cells.index(i)].append(0)
    pre1 = []
    post1 = []
    for i in neuron_conns:
        if i.pre_cell not in pre1:
            pre1.append(i.pre_cell)
            x1 = pre1.index(i.pre_cell)
            if i.post_cell not in post1:
                post1.append(i.post_cell)
                y1 = post1.index(i.post_cell)
                num1[x1][y1] = i.number
            else:
                y1 = post1.index(i.post_cell)
                num1[x1][y1] = i.number
        else:
            x1 = pre1.index(i.pre_cell)
            if i.post_cell not in post1:
                post1.append(i.post_cell)
                y1 = post1.index(i.post_cell)
                num1[x1][y1] = i.number
            else:
                y1 = post1.index(i.post_cell)
                num1[x1][y1] = i.number
    arr1 = np.array(num1)
    
    print(arr1)

    fig = px.imshow(arr1,
                    labels=dict(x ="Pre", y = "Post", color = "Synapses"),
                    x = ['ADAL', 'ADAR', 'ADEL', 'ADER', 'ADFL', 'ADFR', 'ADLL', 'ADLR', 'AFDL', 'AFDR', 'AIAL', 'AIAR', 'AIBL', 'AIBR', 'AIML', 'AIMR', 'AINL', 'AINR', 'AIYL', 'AIYR', 'AIZL', 'AIZR', 'ALA', 'ALML', 'ALMR', 'ALNL', 'ALNR', 'AQR', 'AS1', 'AS10', 'AS11', 'AS2', 'AS3', 'AS4', 'AS5', 'AS6', 'AS7', 'AS8', 'AS9', 'ASEL', 'ASER', 'ASGL', 'ASGR', 'ASHL', 'ASHR', 'ASIL', 'ASIR', 'ASJL', 'ASJR', 'ASKL', 'ASKR', 'AUAL', 'AUAR', 'AVAL', 'AVAR', 'AVBL', 'AVBR', 'AVDL', 'AVDR', 'AVEL', 'AVER', 'AVFL', 'AVFR', 'AVG', 'AVHL', 'AVHR', 'AVJL', 'AVJR', 'AVKL', 'AVKR', 'AVL', 'AVM', 'AWAL', 'AWAR', 'AWBL', 'AWBR', 'AWCL', 'AWCR', 'BAGL', 'BAGR', 'BDUL', 'BDUR', 'CEPDL', 'CEPDR', 'CEPVL', 'CEPVR', 'DA1', 'DA2', 'DA3', 'DA4', 'DA5', 'DA6', 'DA7', 'DA8', 'DA9', 'DB1', 'DB2', 'DB3', 'DB4', 'DB5', 'DB6', 'DB7', 'DD1', 'DD2', 'DD3', 'DD4', 'DD5', 'DD6', 'DVA', 'DVB', 'DVC', 'FLPL', 'FLPR', 'HSNL', 'HSNR', 'IL1DL', 'IL1DR', 'IL1L', 'IL1R', 'IL1VL', 'IL1VR', 'IL2DL', 'IL2DR', 'IL2L', 'IL2R', 'IL2VL', 'IL2VR', 'LUAL', 'LUAR', 'OLLL', 'OLLR', 'OLQDL', 'OLQDR', 'OLQVL', 'OLQVR', 'PDA', 'PDB', 'PDEL', 'PDER', 'PHAL', 'PHAR', 'PHBL', 'PHBR', 'PHCL', 'PHCR', 'PLML', 'PLMR', 'PLNL', 'PLNR', 'PQR', 'PVCL', 'PVCR', 'PVDL', 'PVDR', 'PVM', 'PVNL', 'PVNR', 'PVPL', 'PVPR', 'PVQL', 'PVQR', 'PVR', 'PVT', 'PVWL', 'PVWR', 'RIAL', 'RIAR', 'RIBL', 'RIBR', 'RICL', 'RICR', 'RID', 'RIFL', 'RIFR', 'RIGL', 'RIGR', 'RIH', 'RIML', 'RIMR', 'RIPL', 'RIPR', 'RIR', 'RIS', 'RIVL', 'RIVR', 'RMDDL', 'RMDDR', 'RMDL', 'RMDR', 'RMDVL', 'RMDVR', 'RMED', 'RMEL', 'RMER', 'RMEV', 'RMFL', 'RMFR', 'RMGL', 'RMGR', 'RMHL', 'RMHR', 'SAADL', 'SAADR', 'SAAVL', 'SAAVR', 'SABD', 'SABVL', 'SABVR', 'SDQL', 'SDQR', 'SIADL', 'SIADR', 'SIAVL', 'SIAVR', 'SIBDL', 'SIBDR', 'SIBVL', 'SIBVR', 'SMBDL', 'SMBDR', 'SMBVL', 'SMBVR', 'SMDDL', 'SMDDR', 'SMDVL', 'SMDVR', 'URADL', 'URADR', 'URAVL', 'URAVR', 'URBL', 'URBR', 'URXL', 'URXR', 'URYDL', 'URYDR', 'URYVL', 'URYVR', 'VA1', 'VA10', 'VA11', 'VA12', 'VA2', 'VA3', 'VA4', 'VA5', 'VA6', 'VA7', 'VA8', 'VA9', 'VB1', 'VB10', 'VB11', 'VB2', 'VB3', 'VB4', 'VB5', 'VB6', 'VB7', 'VB8', 'VB9', 'VC1', 'VC2', 'VC3', 'VC4', 'VC5', 'VD1', 'VD10', 'VD11', 'VD12', 'VD13', 'VD2', 'VD3', 'VD4', 'VD5', 'VD6', 'VD7', 'VD8', 'VD9'],
                    y = ['ADAR', 'ADEL', 'ADFL', 'AIAL', 'AIBL', 'AIBR', 'ASHL', 'AVAR', 'AVBL', 'AVBR', 'AVDL', 'AVDR', 'AVEL', 'AVJR', 'AWAL', 'FLPR', 'PVPL', 'PVQL', 'PVR', 'RICL', 'RICR', 'RIML', 'RIPL', 'RMGL', 'SMDVR', 'ADAL', 'ADER', 'ADFR', 'AIAR', 'ASHR', 'AVAL', 'AVJL', 'PVQR', 'RIMR', 'RIPR', 'RIVR', 'RMGR', 'SMDVL', 'URBR', 'AINL', 'ALA', 'AVKR', 'AVL', 'BDUL', 'CEPDL', 'FLPL', 'IL1L', 'IL2L', 'OLLL', 'RIAL', 'RIFL', 'RIGL', 'RIGR', 'RIH', 'RIVL', 'RMDL', 'RMHL', 'SIADR', 'SIBDR', 'SMBDR', 'URBL', 'ALNR', 'AVER', 'AVKL', 'AVM', 'BDUR', 'CEPDR', 'IL2R', 'OLLR', 'RMDR', 'SAAVR', 'AIZL', 'AUAL', 'AWBL', 'OLQVL', 'RIR', 'SMBVL', 'AIYR', 'AIZR', 'ASEL', 'AUAR', 'AVHL', 'AWAR', 'AWBR', 'PVPR', 'RIAR', 'SMBVR', 'URXR', 'ADLR', 'ASER', 'AVHR', 'CEPVL', 'SDQR', 'ADLL', 'AWCR', 'PVCL', 'AFDR', 'AINR', 'AIYL', 'AFDL', 'AIML', 'ASGL', 'ASIL', 'ASIR', 'ASKL', 'AWCL', 'HSNL', 'AIMR', 'ASGR', 'ASKR', 'RIFR', 'BAGL', 'DVC', 'HSNR', 'PVT', 'RIBR', 'SAADL', 'SAADR', 'SAAVL', 'SMDDR', 'DB1', 'RIBL', 'RIS', 'SDQL', 'SMDDL', 'VB1', 'ALML', 'AVFL', 'AVFR', 'ASJR', 'OLQDR', 'PVNR', 'BAGR', 'RID', 'DVA', 'SMBDL', 'VB2', 'PVCR', 'RMDDR', 'CEPVR', 'RMDDL', 'SIADL', 'RMHR', 'URXL', 'DA1', 'VA3', 'VD1', 'VD2', 'PDA', 'PDB', 'VA12', 'VD13', 'DA2', 'DD1', 'VA4', 'DA3', 'VA5', 'VD3', 'AS5', 'DB3', 'VD4', 'AS4', 'DD2', 'VA7', 'VD5', 'DA5', 'PLMR', 'VA8', 'VD6', 'DVB', 'ASJL', 'IL2DL', 'AQR', 'AS1', 'AS10', 'AS11', 'AS2', 'AS3', 'AS6', 'AS7', 'AS8', 'AS9', 'DA4', 'DA6', 'DA7', 'DA8', 'DA9', 'DB5', 'DB6', 'LUAL', 'LUAR', 'PHBL', 'PHBR', 'PHCL', 'PQR', 'PVDL', 'PVDR', 'PVNL', 'SABD', 'SABVR', 'URYDL', 'URYVR', 'VA1', 'VA10', 'VA11', 'VA2', 'VA6', 'VA9', 'VB9', 'AVG', 'PDEL', 'PDER', 'PVWR', 'SABVL', 'URYDR', 'URYVL', 'VD11', 'DB4', 'DB7', 'SIBVL', 'VB10', 'VB11', 'VB4', 'VB5', 'VB6', 'VB7', 'VB8', 'VC3', 'VC4', 'DB2', 'VB3', 'VD10', 'PHAL', 'IL1R', 'RMDVR', 'RMEV', 'RMDVL', 'VC5', 'PHAR', 'PHCR', 'PVWL', 'PVM', 'RMFL', 'RMFR', 'SIAVR', 'DD6', 'VC1', 'VD12', 'ALMR', 'IL2VL', 'URADL', 'URADR', 'IL1DL', 'OLQDL', 'IL1DR', 'IL2DR', 'IL1VL', 'SIAVL', 'URAVL', 'IL1VR', 'IL2VR', 'OLQVR', 'URAVR', 'DD3', 'VC2', 'DD4', 'VD8', 'VD9', 'PLML', 'RMER', 'RMEL', 'RMED', 'SIBVR', 'SIBDL', 'DD5', 'VD7', 'ALNL', 'PLNL', 'PLNR'],
                    )
    fig.show()



