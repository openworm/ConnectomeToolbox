---
title: "Dataset: Test"
search:
  exclude: true
---


!!! example "Choose Dataset"

    <a href="../White_A_data_graph">White_A</a> <a href="../White_L4_data_graph">White_L4</a> <a href="../White_whole_data_graph">White_whole</a> <a href="../Varshney_data_graph">Varshney</a> <a href="../Bentley2016_MA_data_graph">Bentley2016_MA</a> <a href="../Bentley2016_PEP_data_graph">Bentley2016_PEP</a> <a href="../Cook2019Herm_data_graph">Cook2019Herm</a> <a href="../Cook2019Male_data_graph">Cook2019Male</a> <a href="../Cook2020_data_graph">Cook2020</a> <a href="../Brittin2021_data_graph">Brittin2021</a> <a href="../Witvliet1_data_graph">Witvliet1</a> <a href="../Witvliet2_data_graph">Witvliet2</a> <a href="../Witvliet3_data_graph">Witvliet3</a> <a href="../Witvliet4_data_graph">Witvliet4</a> <a href="../Witvliet5_data_graph">Witvliet5</a> <a href="../Witvliet6_data_graph">Witvliet6</a> <a href="../Witvliet7_data_graph">Witvliet7</a> <a href="../Witvliet8_data_graph">Witvliet8</a> <a href="../WormNeuroAtlas_data_graph">WormNeuroAtlas</a> <a href="../Randi2023_data_graph">Randi2023</a> <a href="../RipollSanchezShortRange_data_graph">RipollSanchezShortRange</a> <a href="../RipollSanchezMidRange_data_graph">RipollSanchezMidRange</a> <a href="../RipollSanchezLongRange_data_graph">RipollSanchezLongRange</a> <a href="../Yim2024_data_graph">Yim2024</a> <a href="../Yim2024NonNorm_data_graph">Yim2024NonNorm</a> <a href="../Wang2024Herm_data_graph">Wang2024Herm</a> <a href="../Wang2024Male_data_graph">Wang2024Male</a> <a href="../OpenWormUnified_data_graph">OpenWormUnified</a> <b><a href="../Test_data_graph">Test</a></b> <a href="../SSData_data_graph">SSData</a> <a href="../UpdSSData_data_graph">UpdSSData</a> <a href="../UpdSSData2_data_graph">UpdSSData2</a> <a href="../GleesonModel_data_graph">GleesonModel</a> <a href="../OlivaresModel_data_graph">OlivaresModel</a> 

    <i>Dummy dataset used for testing webpage/graph generation. <b>Do not assume any of these connections are correct!</b>.&nbsp;&nbsp;&nbsp;Python Reader: <a href="../api/cect/TestDataReader">TestDataReader</a></i>


    

!!! abstract inline "Choose Graph type"

    <b><a href="../Test_data_graph"> Graph</a></b> - <a href="../Test_data"> Matrix</a> - <a href="../Test_data_hiveplot"> Hive plot</a> -<a href="../Test_data_symmetry"> Symmetry</a> 


!!! tip  "Choose View"

    <b><a href="../Test_data_graph"> Raw Data</a></b> - <a href="../Neurons_Test_data_graph"> Neurons</a> - <a href="../Pharynx_Test_data_graph"> Pharynx</a> - <a href="../Social_Test_data_graph"> Social Network</a> - <a href="../Escape_Test_data_graph"> Escape Response Circuit</a> - <a href="../Full1_Test_data_graph"> Cook 2019 Fig 3</a> - <a href="../Loco1_Test_data_graph"> Locomotion 1</a> - <a href="../Loco2_Test_data_graph"> Locomotion 2</a> - <a href="../Loco3_Test_data_graph"> Locomotion 3</a> - <a href="../PeptidergicHubs_Test_data_graph"> Peptidergic Hubs</a> - <a href="../NonpharyngealH_Test_data_graph"> Nonpharyngeal Neurons (herm)</a> - <a href="../SensorySomaticH_Test_data_graph"> Sensory Neurons (somatic)</a> - <a href="../MotorSomaticH_Test_data_graph"> Motor Neurons (somatic)</a> - <a href="../InterneuronsSomaticH_Test_data_graph"> Interneurons (somatic)</a> - 

    <i>All of the cells present in the original connectome dataset</i>
=== "Chemical"

    ```{.plotly .no-auto-theme}
    { "file_path": "./assets/Test_Raw_Chemical_graph.json" }
    ```

=== "Electrical"

    ```{.plotly .no-auto-theme}
    { "file_path": "./assets/Test_Raw_Electrical_graph.json" }
    ```

=== "Acetylcholine"

    ```{.plotly .no-auto-theme}
    { "file_path": "./assets/Test_Raw_Acetylcholine_graph.json" }
    ```

=== "GABA"

    ```{.plotly .no-auto-theme}
    { "file_path": "./assets/Test_Raw_GABA_graph.json" }
    ```

=== "View info"

    **Raw Data** (Raw)
    
    _All of the cells present in the original connectome dataset_
    
    
    
    | Connection type | Total size | Values present | Nodes with pre connections | Nodes with post connections |
    | --- | --- | --- | --- | --- |
    |**Chemical** | (21, 21) matrix | 16 non-zero entries, avg. weight: 6.625, sum: 106.0| **<span style="color:#ff66cc;">ASHR</span>**, **<span style="color:#ff66cc;">AWBR</span>**, **<span style="color:#9966cc;">DB4</span>**, **<span style="color:#ff66cc;">DVA</span>**, **<span style="color:#ff3300;">I5</span>**, **<span style="color:#9966cc;">M4</span>**, **<span style="color:#ff3300;">PVCL</span>**, **<span style="color:#ff3300;">PVCR</span>**, **<span style="color:#9966cc;">VA6</span>**, **<span style="color:#9966cc;">VB6</span>**, **<span style="color:#9966cc;">VD3</span>**, **<span style="color:#9966cc;">VD6</span>** | **<span style="color:#ff66cc;">ASHR</span>**, **<span style="color:#ff3300;">AVBL</span>**, **<span style="color:#ff3300;">AVBR</span>**, **<span style="color:#9966cc;">DB4</span>**, **<span style="color:#9966cc;">DD4</span>**, **<span style="color:#9966cc;">M1</span>**, **<span style="color:#9966cc;">M4</span>**, **<span style="color:#ff3300;">PVCL</span>**, **<span style="color:#ff3300;">RMGR</span>**, **<span style="color:#9966cc;">VA3</span>**, **<span style="color:#9966cc;">VA6</span>**, **<span style="color:#9966cc;">VB2</span>**, **<span style="color:#9966cc;">VB6</span>**, **<span style="color:#9966cc;">VD6</span>** |
    |**Electrical** | (21, 21) matrix | 5 non-zero entries, avg. weight: 2.8, sum: 14.0| **<span style="color:#ff66cc;">ASHR</span>**, **<span style="color:#9966cc;">DB4</span>**, **<span style="color:#9966cc;">DD4</span>**, **<span style="color:#9966cc;">VB6</span>** | **<span style="color:#ff66cc;">ASKR</span>**, **<span style="color:#ff3300;">AVBL</span>**, **<span style="color:#9966cc;">DD5</span>**, **<span style="color:#9966cc;">VB6</span>** |
    |**Acetylcholine** | (21, 21) matrix | 13 non-zero entries, avg. weight: 7.615384615384615, sum: 99.0| **<span style="color:#ff66cc;">ASHR</span>**, **<span style="color:#ff66cc;">AWBR</span>**, **<span style="color:#9966cc;">DB4</span>**, **<span style="color:#ff66cc;">DVA</span>**, **<span style="color:#ff3300;">I5</span>**, **<span style="color:#9966cc;">M4</span>**, **<span style="color:#ff3300;">PVCL</span>**, **<span style="color:#ff3300;">PVCR</span>**, **<span style="color:#9966cc;">VA6</span>**, **<span style="color:#9966cc;">VB6</span>** | **<span style="color:#ff66cc;">ASHR</span>**, **<span style="color:#ff3300;">AVBL</span>**, **<span style="color:#ff3300;">AVBR</span>**, **<span style="color:#9966cc;">DB4</span>**, **<span style="color:#9966cc;">DD4</span>**, **<span style="color:#9966cc;">M1</span>**, **<span style="color:#9966cc;">M4</span>**, **<span style="color:#ff3300;">PVCL</span>**, **<span style="color:#ff3300;">RMGR</span>**, **<span style="color:#9966cc;">VB6</span>**, **<span style="color:#9966cc;">VD6</span>** |
    |**GABA** | (21, 21) matrix | 3 non-zero entries, avg. weight: 2.3333333333333335, sum: 7.0| **<span style="color:#9966cc;">VD3</span>**, **<span style="color:#9966cc;">VD6</span>** | **<span style="color:#9966cc;">VA3</span>**, **<span style="color:#9966cc;">VA6</span>**, **<span style="color:#9966cc;">VB2</span>** |
    
    
    | Nodes in current view<br/>(656 total)| Num cells in node<br/>(656 total) | Num in this dataset<br/>(21 total) | Cells |
    | --- | --- | --- | --- |
    |**<span style="color:#ff3300;">I1L</span>** |1 | 0 | <a href="../I1L" title="Pharyngeal interneuron" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#ff3300;">I1L</span></span></a>|
    |**<span style="color:#ff3300;">I1R</span>** |1 | 0 | <a href="../I1R" title="Pharyngeal interneuron" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#ff3300;">I1R</span></span></a>|
    |**<span style="color:#ff3300;">I2L</span>** |1 | 0 | <a href="../I2L" title="Pharyngeal interneuron" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#ff3300;">I2L</span></span></a>|
    |**<span style="color:#ff3300;">I2R</span>** |1 | 0 | <a href="../I2R" title="Pharyngeal interneuron" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#ff3300;">I2R</span></span></a>|
    |**<span style="color:#ff3300;">I3</span>** |1 | 0 | <a href="../I3" title="Pharyngeal interneuron" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#ff3300;">I3</span></span></a>|
    |**<span style="color:#ff3300;">I4</span>** |1 | 0 | <a href="../I4" title="Pharyngeal interneuron" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#ff3300;">I4</span></span></a>|
    |**<span style="color:#ff3300;">I5</span>** |1 | 1 | <a href="../I5" title="Pharyngeal interneuron" style="text-decoration:none;"><strong><span style="color:#ff3300;">I5</span></strong></a>|
    |**<span style="color:#ff3300;">I6</span>** |1 | 0 | <a href="../I6" title="Pharyngeal interneuron" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#ff3300;">I6</span></span></a>|
    |**<span style="color:#9966cc;">M1</span>** |1 | 1 | <a href="../M1" title="Pharyngeal motor neuron" style="text-decoration:none;"><strong><span style="color:#9966cc;">M1</span></strong></a>|
    |**<span style="color:#9966cc;">M2L</span>** |1 | 0 | <a href="../M2L" title="Pharyngeal motor neuron" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#9966cc;">M2L</span></span></a>|
    |**<span style="color:#9966cc;">M2R</span>** |1 | 0 | <a href="../M2R" title="Pharyngeal motor neuron" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#9966cc;">M2R</span></span></a>|
    |**<span style="color:#9966cc;">M3L</span>** |1 | 0 | <a href="../M3L" title="Pharyngeal motor neuron" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#9966cc;">M3L</span></span></a>|
    |**<span style="color:#9966cc;">M3R</span>** |1 | 0 | <a href="../M3R" title="Pharyngeal motor neuron" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#9966cc;">M3R</span></span></a>|
    |**<span style="color:#9966cc;">M4</span>** |1 | 1 | <a href="../M4" title="Pharyngeal motor neuron" style="text-decoration:none;"><strong><span style="color:#9966cc;">M4</span></strong></a>|
    |**<span style="color:#9966cc;">M5</span>** |1 | 0 | <a href="../M5" title="Pharyngeal motor neuron" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#9966cc;">M5</span></span></a>|
    |**<span style="color:#cc0033;">MCL</span>** |1 | 0 | <a href="../MCL" title="Pharyngeal polymodal neuron" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#cc0033;">MCL</span></span></a>|
    |**<span style="color:#cc0033;">MCR</span>** |1 | 0 | <a href="../MCR" title="Pharyngeal polymodal neuron" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#cc0033;">MCR</span></span></a>|
    |**<span style="color:#cc0033;">MI</span>** |1 | 0 | <a href="../MI" title="Pharyngeal polymodal neuron" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#cc0033;">MI</span></span></a>|
    |**<span style="color:#cc0033;">NSML</span>** |1 | 0 | <a href="../NSML" title="Pharyngeal polymodal neuron" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#cc0033;">NSML</span></span></a>|
    |**<span style="color:#cc0033;">NSMR</span>** |1 | 0 | <a href="../NSMR" title="Pharyngeal polymodal neuron" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#cc0033;">NSMR</span></span></a>|
    |**<span style="color:#ff66cc;">ADEL</span>** |1 | 0 | <a href="../ADEL" title="Sensory neuron (mechanosensory)" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#ff66cc;">ADEL</span></span></a>|
    |**<span style="color:#ff66cc;">ADER</span>** |1 | 0 | <a href="../ADER" title="Sensory neuron (mechanosensory)" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#ff66cc;">ADER</span></span></a>|
    |**<span style="color:#ff66cc;">ADFL</span>** |1 | 0 | <a href="../ADFL" title="Sensory neuron (amphid)" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#ff66cc;">ADFL</span></span></a>|
    |**<span style="color:#ff66cc;">ADFR</span>** |1 | 0 | <a href="../ADFR" title="Sensory neuron (amphid)" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#ff66cc;">ADFR</span></span></a>|
    |**<span style="color:#ff66cc;">ADLL</span>** |1 | 0 | <a href="../ADLL" title="Sensory neuron (amphid, nociceptive)" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#ff66cc;">ADLL</span></span></a>|
    |**<span style="color:#ff66cc;">ADLR</span>** |1 | 0 | <a href="../ADLR" title="Sensory neuron (amphid, nociceptive)" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#ff66cc;">ADLR</span></span></a>|
    |**<span style="color:#ff66cc;">AFDL</span>** |1 | 0 | <a href="../AFDL" title="Sensory neuron (amphid)" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#ff66cc;">AFDL</span></span></a>|
    |**<span style="color:#ff66cc;">AFDR</span>** |1 | 0 | <a href="../AFDR" title="Sensory neuron (amphid)" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#ff66cc;">AFDR</span></span></a>|
    |**<span style="color:#ff66cc;">ALML</span>** |1 | 0 | <a href="../ALML" title="Sensory neuron (mechanosensory)" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#ff66cc;">ALML</span></span></a>|
    |**<span style="color:#ff66cc;">ALMR</span>** |1 | 0 | <a href="../ALMR" title="Sensory neuron (mechanosensory)" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#ff66cc;">ALMR</span></span></a>|
    |**<span style="color:#ff66cc;">ALNL</span>** |1 | 0 | <a href="../ALNL" title="Sensory neuron (touch)" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#ff66cc;">ALNL</span></span></a>|
    |**<span style="color:#ff66cc;">ALNR</span>** |1 | 0 | <a href="../ALNR" title="Sensory neuron (touch)" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#ff66cc;">ALNR</span></span></a>|
    |**<span style="color:#ff66cc;">AQR</span>** |1 | 0 | <a href="../AQR" title="Sensory neuron (touch)" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#ff66cc;">AQR</span></span></a>|
    |**<span style="color:#ff66cc;">ASEL</span>** |1 | 0 | <a href="../ASEL" title="Sensory neuron (amphid)" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#ff66cc;">ASEL</span></span></a>|
    |**<span style="color:#ff66cc;">ASER</span>** |1 | 0 | <a href="../ASER" title="Sensory neuron (amphid)" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#ff66cc;">ASER</span></span></a>|
    |**<span style="color:#ff66cc;">ASGL</span>** |1 | 0 | <a href="../ASGL" title="Sensory neuron (amphid)" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#ff66cc;">ASGL</span></span></a>|
    |**<span style="color:#ff66cc;">ASGR</span>** |1 | 0 | <a href="../ASGR" title="Sensory neuron (amphid)" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#ff66cc;">ASGR</span></span></a>|
    |**<span style="color:#ff66cc;">ASHL</span>** |1 | 0 | <a href="../ASHL" title="Sensory neuron (amphid, nociceptive)" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#ff66cc;">ASHL</span></span></a>|
    |**<span style="color:#ff66cc;">ASHR</span>** |1 | 1 | <a href="../ASHR" title="Sensory neuron (amphid, nociceptive)" style="text-decoration:none;"><strong><span style="color:#ff66cc;">ASHR</span></strong></a>|
    |**<span style="color:#ff66cc;">ASIL</span>** |1 | 0 | <a href="../ASIL" title="Sensory neuron (amphid)" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#ff66cc;">ASIL</span></span></a>|
    |**<span style="color:#ff66cc;">ASIR</span>** |1 | 0 | <a href="../ASIR" title="Sensory neuron (amphid)" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#ff66cc;">ASIR</span></span></a>|
    |**<span style="color:#ff66cc;">ASJL</span>** |1 | 0 | <a href="../ASJL" title="Sensory neuron (amphid)" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#ff66cc;">ASJL</span></span></a>|
    |**<span style="color:#ff66cc;">ASJR</span>** |1 | 0 | <a href="../ASJR" title="Sensory neuron (amphid)" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#ff66cc;">ASJR</span></span></a>|
    |**<span style="color:#ff66cc;">ASKL</span>** |1 | 0 | <a href="../ASKL" title="Sensory neuron (amphid)" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#ff66cc;">ASKL</span></span></a>|
    |**<span style="color:#ff66cc;">ASKR</span>** |1 | 1 | <a href="../ASKR" title="Sensory neuron (amphid)" style="text-decoration:none;"><strong><span style="color:#ff66cc;">ASKR</span></strong></a>|
    |**<span style="color:#ff66cc;">AVM</span>** |1 | 0 | <a href="../AVM" title="Sensory neuron (mechanosensory)" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#ff66cc;">AVM</span></span></a>|
    |**<span style="color:#ff66cc;">AWAL</span>** |1 | 0 | <a href="../AWAL" title="Sensory neuron (amphid)" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#ff66cc;">AWAL</span></span></a>|
    |**<span style="color:#ff66cc;">AWAR</span>** |1 | 0 | <a href="../AWAR" title="Sensory neuron (amphid)" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#ff66cc;">AWAR</span></span></a>|
    |**<span style="color:#ff66cc;">AWBL</span>** |1 | 0 | <a href="../AWBL" title="Sensory neuron (amphid)" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#ff66cc;">AWBL</span></span></a>|
    |**<span style="color:#ff66cc;">AWBR</span>** |1 | 1 | <a href="../AWBR" title="Sensory neuron (amphid)" style="text-decoration:none;"><strong><span style="color:#ff66cc;">AWBR</span></strong></a>|
    |**<span style="color:#ff66cc;">AWCL</span>** |1 | 0 | <a href="../AWCL" title="Sensory neuron (amphid)" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#ff66cc;">AWCL</span></span></a>|
    |**<span style="color:#ff66cc;">AWCR</span>** |1 | 0 | <a href="../AWCR" title="Sensory neuron (amphid)" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#ff66cc;">AWCR</span></span></a>|
    |**<span style="color:#ff66cc;">BAGL</span>** |1 | 0 | <a href="../BAGL" title="Sensory neuron (O2, CO2, social signals, touch)" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#ff66cc;">BAGL</span></span></a>|
    |**<span style="color:#ff66cc;">BAGR</span>** |1 | 0 | <a href="../BAGR" title="Sensory neuron (O2, CO2, social signals, touch)" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#ff66cc;">BAGR</span></span></a>|
    |**<span style="color:#ff66cc;">CEMDL</span>** |1 | 0 | <a href="../CEMDL" title="Male head sensory neuron" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#ff66cc;">CEMDL</span></span></a>|
    |**<span style="color:#ff66cc;">CEMDR</span>** |1 | 0 | <a href="../CEMDR" title="Male head sensory neuron" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#ff66cc;">CEMDR</span></span></a>|
    |**<span style="color:#ff66cc;">CEMVL</span>** |1 | 0 | <a href="../CEMVL" title="Male head sensory neuron" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#ff66cc;">CEMVL</span></span></a>|
    |**<span style="color:#ff66cc;">CEMVR</span>** |1 | 0 | <a href="../CEMVR" title="Male head sensory neuron" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#ff66cc;">CEMVR</span></span></a>|
    |**<span style="color:#ff66cc;">CEPDL</span>** |1 | 0 | <a href="../CEPDL" title="Sensory neuron (cephalic)" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#ff66cc;">CEPDL</span></span></a>|
    |**<span style="color:#ff66cc;">CEPDR</span>** |1 | 0 | <a href="../CEPDR" title="Sensory neuron (cephalic)" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#ff66cc;">CEPDR</span></span></a>|
    |**<span style="color:#ff66cc;">CEPVL</span>** |1 | 0 | <a href="../CEPVL" title="Sensory neuron (cephalic)" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#ff66cc;">CEPVL</span></span></a>|
    |**<span style="color:#ff66cc;">CEPVR</span>** |1 | 0 | <a href="../CEPVR" title="Sensory neuron (cephalic)" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#ff66cc;">CEPVR</span></span></a>|
    |**<span style="color:#ff66cc;">DVA</span>** |1 | 1 | <a href="../DVA" title="Sensory neuron (mechanosensory)" style="text-decoration:none;"><strong><span style="color:#ff66cc;">DVA</span></strong></a>|
    |**<span style="color:#ff66cc;">FLPL</span>** |1 | 0 | <a href="../FLPL" title="Sensory neuron (mechanosensory)" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#ff66cc;">FLPL</span></span></a>|
    |**<span style="color:#ff66cc;">FLPR</span>** |1 | 0 | <a href="../FLPR" title="Sensory neuron (mechanosensory)" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#ff66cc;">FLPR</span></span></a>|
    |**<span style="color:#ff66cc;">HOA</span>** |1 | 0 | <a href="../HOA" title="Male sensory neuron" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#ff66cc;">HOA</span></span></a>|
    |**<span style="color:#ff66cc;">HOB</span>** |1 | 0 | <a href="../HOB" title="Male sensory neuron" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#ff66cc;">HOB</span></span></a>|
    |**<span style="color:#ff66cc;">IL1DL</span>** |1 | 0 | <a href="../IL1DL" title="Sensory neuron (cephalic)" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#ff66cc;">IL1DL</span></span></a>|
    |**<span style="color:#ff66cc;">IL1DR</span>** |1 | 0 | <a href="../IL1DR" title="Sensory neuron (cephalic)" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#ff66cc;">IL1DR</span></span></a>|
    |**<span style="color:#ff66cc;">IL1L</span>** |1 | 0 | <a href="../IL1L" title="Sensory neuron (cephalic)" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#ff66cc;">IL1L</span></span></a>|
    |**<span style="color:#ff66cc;">IL1R</span>** |1 | 0 | <a href="../IL1R" title="Sensory neuron (cephalic)" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#ff66cc;">IL1R</span></span></a>|
    |**<span style="color:#ff66cc;">IL1VL</span>** |1 | 0 | <a href="../IL1VL" title="Sensory neuron (cephalic)" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#ff66cc;">IL1VL</span></span></a>|
    |**<span style="color:#ff66cc;">IL1VR</span>** |1 | 0 | <a href="../IL1VR" title="Sensory neuron (cephalic)" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#ff66cc;">IL1VR</span></span></a>|
    |**<span style="color:#ff66cc;">IL2DL</span>** |1 | 0 | <a href="../IL2DL" title="Sensory neuron (cephalic)" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#ff66cc;">IL2DL</span></span></a>|
    |**<span style="color:#ff66cc;">IL2DR</span>** |1 | 0 | <a href="../IL2DR" title="Sensory neuron (cephalic)" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#ff66cc;">IL2DR</span></span></a>|
    |**<span style="color:#ff66cc;">IL2L</span>** |1 | 0 | <a href="../IL2L" title="Sensory neuron (cephalic)" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#ff66cc;">IL2L</span></span></a>|
    |**<span style="color:#ff66cc;">IL2R</span>** |1 | 0 | <a href="../IL2R" title="Sensory neuron (cephalic)" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#ff66cc;">IL2R</span></span></a>|
    |**<span style="color:#ff66cc;">IL2VL</span>** |1 | 0 | <a href="../IL2VL" title="Sensory neuron (cephalic)" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#ff66cc;">IL2VL</span></span></a>|
    |**<span style="color:#ff66cc;">IL2VR</span>** |1 | 0 | <a href="../IL2VR" title="Sensory neuron (cephalic)" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#ff66cc;">IL2VR</span></span></a>|
    |**<span style="color:#ff66cc;">OLLL</span>** |1 | 0 | <a href="../OLLL" title="Sensory neuron (cephalic)" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#ff66cc;">OLLL</span></span></a>|
    |**<span style="color:#ff66cc;">OLLR</span>** |1 | 0 | <a href="../OLLR" title="Sensory neuron (cephalic)" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#ff66cc;">OLLR</span></span></a>|
    |**<span style="color:#ff66cc;">OLQDL</span>** |1 | 0 | <a href="../OLQDL" title="Sensory neuron (cephalic)" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#ff66cc;">OLQDL</span></span></a>|
    |**<span style="color:#ff66cc;">OLQDR</span>** |1 | 0 | <a href="../OLQDR" title="Sensory neuron (cephalic)" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#ff66cc;">OLQDR</span></span></a>|
    |**<span style="color:#ff66cc;">OLQVL</span>** |1 | 0 | <a href="../OLQVL" title="Sensory neuron (cephalic)" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#ff66cc;">OLQVL</span></span></a>|
    |**<span style="color:#ff66cc;">OLQVR</span>** |1 | 0 | <a href="../OLQVR" title="Sensory neuron (cephalic)" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#ff66cc;">OLQVR</span></span></a>|
    |**<span style="color:#ff66cc;">PCAL</span>** |1 | 0 | <a href="../PCAL" title="Male sensory neuron" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#ff66cc;">PCAL</span></span></a>|
    |**<span style="color:#ff66cc;">PCAR</span>** |1 | 0 | <a href="../PCAR" title="Male sensory neuron" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#ff66cc;">PCAR</span></span></a>|
    |**<span style="color:#ff66cc;">PCBL</span>** |1 | 0 | <a href="../PCBL" title="Male sensory neuron" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#ff66cc;">PCBL</span></span></a>|
    |**<span style="color:#ff66cc;">PCBR</span>** |1 | 0 | <a href="../PCBR" title="Male sensory neuron" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#ff66cc;">PCBR</span></span></a>|
    |**<span style="color:#ff66cc;">PCCL</span>** |1 | 0 | <a href="../PCCL" title="Male sensory neuron" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#ff66cc;">PCCL</span></span></a>|
    |**<span style="color:#ff66cc;">PCCR</span>** |1 | 0 | <a href="../PCCR" title="Male sensory neuron" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#ff66cc;">PCCR</span></span></a>|
    |**<span style="color:#ff66cc;">PDEL</span>** |1 | 0 | <a href="../PDEL" title="Sensory neuron (mechanosensory)" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#ff66cc;">PDEL</span></span></a>|
    |**<span style="color:#ff66cc;">PDER</span>** |1 | 0 | <a href="../PDER" title="Sensory neuron (mechanosensory)" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#ff66cc;">PDER</span></span></a>|
    |**<span style="color:#ff66cc;">PHAL</span>** |1 | 0 | <a href="../PHAL" title="Sensory neuron (phasmid)" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#ff66cc;">PHAL</span></span></a>|
    |**<span style="color:#ff66cc;">PHAR</span>** |1 | 0 | <a href="../PHAR" title="Sensory neuron (phasmid)" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#ff66cc;">PHAR</span></span></a>|
    |**<span style="color:#ff66cc;">PHBL</span>** |1 | 0 | <a href="../PHBL" title="Sensory neuron (phasmid)" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#ff66cc;">PHBL</span></span></a>|
    |**<span style="color:#ff66cc;">PHBR</span>** |1 | 0 | <a href="../PHBR" title="Sensory neuron (phasmid)" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#ff66cc;">PHBR</span></span></a>|
    |**<span style="color:#ff66cc;">PHCL</span>** |1 | 0 | <a href="../PHCL" title="Sensory neuron (phasmid)" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#ff66cc;">PHCL</span></span></a>|
    |**<span style="color:#ff66cc;">PHCR</span>** |1 | 0 | <a href="../PHCR" title="Sensory neuron (phasmid)" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#ff66cc;">PHCR</span></span></a>|
    |**<span style="color:#ff66cc;">PHDL</span>** |1 | 0 | <a href="../PHDL" title="Male sensory neuron" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#ff66cc;">PHDL</span></span></a>|
    |**<span style="color:#ff66cc;">PHDR</span>** |1 | 0 | <a href="../PHDR" title="Male sensory neuron" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#ff66cc;">PHDR</span></span></a>|
    |**<span style="color:#ff66cc;">PLML</span>** |1 | 0 | <a href="../PLML" title="Sensory neuron (mechanosensory)" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#ff66cc;">PLML</span></span></a>|
    |**<span style="color:#ff66cc;">PLMR</span>** |1 | 0 | <a href="../PLMR" title="Sensory neuron (mechanosensory)" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#ff66cc;">PLMR</span></span></a>|
    |**<span style="color:#ff66cc;">PLNL</span>** |1 | 0 | <a href="../PLNL" title="Sensory neuron (touch)" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#ff66cc;">PLNL</span></span></a>|
    |**<span style="color:#ff66cc;">PLNR</span>** |1 | 0 | <a href="../PLNR" title="Sensory neuron (touch)" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#ff66cc;">PLNR</span></span></a>|
    |**<span style="color:#ff66cc;">PQR</span>** |1 | 0 | <a href="../PQR" title="Sensory neuron (touch)" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#ff66cc;">PQR</span></span></a>|
    |**<span style="color:#ff66cc;">PVDL</span>** |1 | 0 | <a href="../PVDL" title="Sensory neuron (mechanosensory)" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#ff66cc;">PVDL</span></span></a>|
    |**<span style="color:#ff66cc;">PVDR</span>** |1 | 0 | <a href="../PVDR" title="Sensory neuron (mechanosensory)" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#ff66cc;">PVDR</span></span></a>|
    |**<span style="color:#ff66cc;">PVM</span>** |1 | 0 | <a href="../PVM" title="Sensory neuron (mechanosensory)" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#ff66cc;">PVM</span></span></a>|
    |**<span style="color:#ff66cc;">R1AL</span>** |1 | 0 | <a href="../R1AL" title="Male sensory neuron" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#ff66cc;">R1AL</span></span></a>|
    |**<span style="color:#ff66cc;">R1AR</span>** |1 | 0 | <a href="../R1AR" title="Male sensory neuron" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#ff66cc;">R1AR</span></span></a>|
    |**<span style="color:#ff66cc;">R1BL</span>** |1 | 0 | <a href="../R1BL" title="Male sensory neuron" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#ff66cc;">R1BL</span></span></a>|
    |**<span style="color:#ff66cc;">R1BR</span>** |1 | 0 | <a href="../R1BR" title="Male sensory neuron" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#ff66cc;">R1BR</span></span></a>|
    |**<span style="color:#ff66cc;">R2AL</span>** |1 | 0 | <a href="../R2AL" title="Male sensory neuron" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#ff66cc;">R2AL</span></span></a>|
    |**<span style="color:#ff66cc;">R2AR</span>** |1 | 0 | <a href="../R2AR" title="Male sensory neuron" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#ff66cc;">R2AR</span></span></a>|
    |**<span style="color:#ff66cc;">R2BL</span>** |1 | 0 | <a href="../R2BL" title="Male sensory neuron" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#ff66cc;">R2BL</span></span></a>|
    |**<span style="color:#ff66cc;">R2BR</span>** |1 | 0 | <a href="../R2BR" title="Male sensory neuron" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#ff66cc;">R2BR</span></span></a>|
    |**<span style="color:#ff66cc;">R3AL</span>** |1 | 0 | <a href="../R3AL" title="Male sensory neuron" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#ff66cc;">R3AL</span></span></a>|
    |**<span style="color:#ff66cc;">R3AR</span>** |1 | 0 | <a href="../R3AR" title="Male sensory neuron" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#ff66cc;">R3AR</span></span></a>|
    |**<span style="color:#ff66cc;">R3BL</span>** |1 | 0 | <a href="../R3BL" title="Male sensory neuron" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#ff66cc;">R3BL</span></span></a>|
    |**<span style="color:#ff66cc;">R3BR</span>** |1 | 0 | <a href="../R3BR" title="Male sensory neuron" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#ff66cc;">R3BR</span></span></a>|
    |**<span style="color:#ff66cc;">R4AL</span>** |1 | 0 | <a href="../R4AL" title="Male sensory neuron" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#ff66cc;">R4AL</span></span></a>|
    |**<span style="color:#ff66cc;">R4AR</span>** |1 | 0 | <a href="../R4AR" title="Male sensory neuron" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#ff66cc;">R4AR</span></span></a>|
    |**<span style="color:#ff66cc;">R4BL</span>** |1 | 0 | <a href="../R4BL" title="Male sensory neuron" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#ff66cc;">R4BL</span></span></a>|
    |**<span style="color:#ff66cc;">R4BR</span>** |1 | 0 | <a href="../R4BR" title="Male sensory neuron" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#ff66cc;">R4BR</span></span></a>|
    |**<span style="color:#ff66cc;">R5AL</span>** |1 | 0 | <a href="../R5AL" title="Male sensory neuron" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#ff66cc;">R5AL</span></span></a>|
    |**<span style="color:#ff66cc;">R5AR</span>** |1 | 0 | <a href="../R5AR" title="Male sensory neuron" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#ff66cc;">R5AR</span></span></a>|
    |**<span style="color:#ff66cc;">R5BL</span>** |1 | 0 | <a href="../R5BL" title="Male sensory neuron" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#ff66cc;">R5BL</span></span></a>|
    |**<span style="color:#ff66cc;">R5BR</span>** |1 | 0 | <a href="../R5BR" title="Male sensory neuron" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#ff66cc;">R5BR</span></span></a>|
    |**<span style="color:#ff66cc;">R6AL</span>** |1 | 0 | <a href="../R6AL" title="Male sensory neuron" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#ff66cc;">R6AL</span></span></a>|
    |**<span style="color:#ff66cc;">R6AR</span>** |1 | 0 | <a href="../R6AR" title="Male sensory neuron" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#ff66cc;">R6AR</span></span></a>|
    |**<span style="color:#ff66cc;">R6BL</span>** |1 | 0 | <a href="../R6BL" title="Male sensory neuron" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#ff66cc;">R6BL</span></span></a>|
    |**<span style="color:#ff66cc;">R6BR</span>** |1 | 0 | <a href="../R6BR" title="Male sensory neuron" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#ff66cc;">R6BR</span></span></a>|
    |**<span style="color:#ff66cc;">R7AL</span>** |1 | 0 | <a href="../R7AL" title="Male sensory neuron" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#ff66cc;">R7AL</span></span></a>|
    |**<span style="color:#ff66cc;">R7AR</span>** |1 | 0 | <a href="../R7AR" title="Male sensory neuron" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#ff66cc;">R7AR</span></span></a>|
    |**<span style="color:#ff66cc;">R7BL</span>** |1 | 0 | <a href="../R7BL" title="Male sensory neuron" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#ff66cc;">R7BL</span></span></a>|
    |**<span style="color:#ff66cc;">R7BR</span>** |1 | 0 | <a href="../R7BR" title="Male sensory neuron" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#ff66cc;">R7BR</span></span></a>|
    |**<span style="color:#ff66cc;">R8AL</span>** |1 | 0 | <a href="../R8AL" title="Male sensory neuron" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#ff66cc;">R8AL</span></span></a>|
    |**<span style="color:#ff66cc;">R8AR</span>** |1 | 0 | <a href="../R8AR" title="Male sensory neuron" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#ff66cc;">R8AR</span></span></a>|
    |**<span style="color:#ff66cc;">R8BL</span>** |1 | 0 | <a href="../R8BL" title="Male sensory neuron" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#ff66cc;">R8BL</span></span></a>|
    |**<span style="color:#ff66cc;">R8BR</span>** |1 | 0 | <a href="../R8BR" title="Male sensory neuron" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#ff66cc;">R8BR</span></span></a>|
    |**<span style="color:#ff66cc;">R9AL</span>** |1 | 0 | <a href="../R9AL" title="Male sensory neuron" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#ff66cc;">R9AL</span></span></a>|
    |**<span style="color:#ff66cc;">R9AR</span>** |1 | 0 | <a href="../R9AR" title="Male sensory neuron" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#ff66cc;">R9AR</span></span></a>|
    |**<span style="color:#ff66cc;">R9BL</span>** |1 | 0 | <a href="../R9BL" title="Male sensory neuron" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#ff66cc;">R9BL</span></span></a>|
    |**<span style="color:#ff66cc;">R9BR</span>** |1 | 0 | <a href="../R9BR" title="Male sensory neuron" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#ff66cc;">R9BR</span></span></a>|
    |**<span style="color:#ff66cc;">SDQL</span>** |1 | 0 | <a href="../SDQL" title="Sensory neuron (touch)" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#ff66cc;">SDQL</span></span></a>|
    |**<span style="color:#ff66cc;">SDQR</span>** |1 | 0 | <a href="../SDQR" title="Sensory neuron (touch)" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#ff66cc;">SDQR</span></span></a>|
    |**<span style="color:#ff66cc;">SPCL</span>** |1 | 0 | <a href="../SPCL" title="Male sensory neuron" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#ff66cc;">SPCL</span></span></a>|
    |**<span style="color:#ff66cc;">SPCR</span>** |1 | 0 | <a href="../SPCR" title="Male sensory neuron" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#ff66cc;">SPCR</span></span></a>|
    |**<span style="color:#ff66cc;">SPDL</span>** |1 | 0 | <a href="../SPDL" title="Male sensory neuron" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#ff66cc;">SPDL</span></span></a>|
    |**<span style="color:#ff66cc;">SPDR</span>** |1 | 0 | <a href="../SPDR" title="Male sensory neuron" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#ff66cc;">SPDR</span></span></a>|
    |**<span style="color:#ff66cc;">SPVL</span>** |1 | 0 | <a href="../SPVL" title="Male sensory neuron" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#ff66cc;">SPVL</span></span></a>|
    |**<span style="color:#ff66cc;">SPVR</span>** |1 | 0 | <a href="../SPVR" title="Male sensory neuron" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#ff66cc;">SPVR</span></span></a>|
    |**<span style="color:#ff66cc;">URXL</span>** |1 | 0 | <a href="../URXL" title="Sensory neuron (O2, CO2, social signals, touch)" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#ff66cc;">URXL</span></span></a>|
    |**<span style="color:#ff66cc;">URXR</span>** |1 | 0 | <a href="../URXR" title="Sensory neuron (O2, CO2, social signals, touch)" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#ff66cc;">URXR</span></span></a>|
    |**<span style="color:#ff66cc;">URYDL</span>** |1 | 0 | <a href="../URYDL" title="Sensory neuron (cephalic)" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#ff66cc;">URYDL</span></span></a>|
    |**<span style="color:#ff66cc;">URYDR</span>** |1 | 0 | <a href="../URYDR" title="Sensory neuron (cephalic)" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#ff66cc;">URYDR</span></span></a>|
    |**<span style="color:#ff66cc;">URYVL</span>** |1 | 0 | <a href="../URYVL" title="Sensory neuron (cephalic)" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#ff66cc;">URYVL</span></span></a>|
    |**<span style="color:#ff66cc;">URYVR</span>** |1 | 0 | <a href="../URYVR" title="Sensory neuron (cephalic)" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#ff66cc;">URYVR</span></span></a>|
    |**<span style="color:#ff3300;">ADAL</span>** |1 | 0 | <a href="../ADAL" title="Layer 3 interneuron" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#ff3300;">ADAL</span></span></a>|
    |**<span style="color:#ff3300;">ADAR</span>** |1 | 0 | <a href="../ADAR" title="Layer 3 interneuron" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#ff3300;">ADAR</span></span></a>|
    |**<span style="color:#ff3300;">AIAL</span>** |1 | 0 | <a href="../AIAL" title="Layer 3 interneuron" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#ff3300;">AIAL</span></span></a>|
    |**<span style="color:#ff3300;">AIAR</span>** |1 | 0 | <a href="../AIAR" title="Layer 3 interneuron" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#ff3300;">AIAR</span></span></a>|
    |**<span style="color:#ff3300;">AIBL</span>** |1 | 0 | <a href="../AIBL" title="Layer 2 interneuron" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#ff3300;">AIBL</span></span></a>|
    |**<span style="color:#ff3300;">AIBR</span>** |1 | 0 | <a href="../AIBR" title="Layer 2 interneuron" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#ff3300;">AIBR</span></span></a>|
    |**<span style="color:#ff3300;">AIML</span>** |1 | 0 | <a href="../AIML" title="Category 4 interneuron" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#ff3300;">AIML</span></span></a>|
    |**<span style="color:#ff3300;">AIMR</span>** |1 | 0 | <a href="../AIMR" title="Category 4 interneuron" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#ff3300;">AIMR</span></span></a>|
    |**<span style="color:#ff3300;">AINL</span>** |1 | 0 | <a href="../AINL" title="Category 4 interneuron" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#ff3300;">AINL</span></span></a>|
    |**<span style="color:#ff3300;">AINR</span>** |1 | 0 | <a href="../AINR" title="Category 4 interneuron" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#ff3300;">AINR</span></span></a>|
    |**<span style="color:#ff3300;">AIYL</span>** |1 | 0 | <a href="../AIYL" title="Layer 3 interneuron" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#ff3300;">AIYL</span></span></a>|
    |**<span style="color:#ff3300;">AIYR</span>** |1 | 0 | <a href="../AIYR" title="Layer 3 interneuron" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#ff3300;">AIYR</span></span></a>|
    |**<span style="color:#ff3300;">AIZL</span>** |1 | 0 | <a href="../AIZL" title="Layer 3 interneuron" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#ff3300;">AIZL</span></span></a>|
    |**<span style="color:#ff3300;">AIZR</span>** |1 | 0 | <a href="../AIZR" title="Layer 3 interneuron" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#ff3300;">AIZR</span></span></a>|
    |**<span style="color:#ff3300;">ALA</span>** |1 | 0 | <a href="../ALA" title="Layer 3 interneuron" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#ff3300;">ALA</span></span></a>|
    |**<span style="color:#ff3300;">AUAL</span>** |1 | 0 | <a href="../AUAL" title="Layer 3 interneuron" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#ff3300;">AUAL</span></span></a>|
    |**<span style="color:#ff3300;">AUAR</span>** |1 | 0 | <a href="../AUAR" title="Layer 3 interneuron" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#ff3300;">AUAR</span></span></a>|
    |**<span style="color:#ff3300;">AVAL</span>** |1 | 0 | <a href="../AVAL" title="Layer 1 interneuron" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#ff3300;">AVAL</span></span></a>|
    |**<span style="color:#ff3300;">AVAR</span>** |1 | 0 | <a href="../AVAR" title="Layer 1 interneuron" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#ff3300;">AVAR</span></span></a>|
    |**<span style="color:#ff3300;">AVBL</span>** |1 | 1 | <a href="../AVBL" title="Layer 1 interneuron" style="text-decoration:none;"><strong><span style="color:#ff3300;">AVBL</span></strong></a>|
    |**<span style="color:#ff3300;">AVBR</span>** |1 | 1 | <a href="../AVBR" title="Layer 1 interneuron" style="text-decoration:none;"><strong><span style="color:#ff3300;">AVBR</span></strong></a>|
    |**<span style="color:#ff3300;">AVDL</span>** |1 | 0 | <a href="../AVDL" title="Layer 2 interneuron" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#ff3300;">AVDL</span></span></a>|
    |**<span style="color:#ff3300;">AVDR</span>** |1 | 0 | <a href="../AVDR" title="Layer 2 interneuron" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#ff3300;">AVDR</span></span></a>|
    |**<span style="color:#ff3300;">AVEL</span>** |1 | 0 | <a href="../AVEL" title="Layer 1 interneuron" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#ff3300;">AVEL</span></span></a>|
    |**<span style="color:#ff3300;">AVER</span>** |1 | 0 | <a href="../AVER" title="Layer 1 interneuron" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#ff3300;">AVER</span></span></a>|
    |**<span style="color:#ff3300;">AVFL</span>** |1 | 0 | <a href="../AVFL" title="Layer 3 interneuron" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#ff3300;">AVFL</span></span></a>|
    |**<span style="color:#ff3300;">AVFR</span>** |1 | 0 | <a href="../AVFR" title="Layer 3 interneuron" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#ff3300;">AVFR</span></span></a>|
    |**<span style="color:#ff3300;">AVG</span>** |1 | 0 | <a href="../AVG" title="Layer 3 interneuron" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#ff3300;">AVG</span></span></a>|
    |**<span style="color:#ff3300;">AVHL</span>** |1 | 0 | <a href="../AVHL" title="Layer 3 interneuron" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#ff3300;">AVHL</span></span></a>|
    |**<span style="color:#ff3300;">AVHR</span>** |1 | 0 | <a href="../AVHR" title="Layer 3 interneuron" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#ff3300;">AVHR</span></span></a>|
    |**<span style="color:#ff3300;">AVJL</span>** |1 | 0 | <a href="../AVJL" title="Layer 2 interneuron" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#ff3300;">AVJL</span></span></a>|
    |**<span style="color:#ff3300;">AVJR</span>** |1 | 0 | <a href="../AVJR" title="Layer 2 interneuron" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#ff3300;">AVJR</span></span></a>|
    |**<span style="color:#ff3300;">AVKL</span>** |1 | 0 | <a href="../AVKL" title="Layer 2 interneuron" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#ff3300;">AVKL</span></span></a>|
    |**<span style="color:#ff3300;">AVKR</span>** |1 | 0 | <a href="../AVKR" title="Layer 2 interneuron" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#ff3300;">AVKR</span></span></a>|
    |**<span style="color:#ff3300;">AVL</span>** |1 | 0 | <a href="../AVL" title="Layer 2 interneuron" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#ff3300;">AVL</span></span></a>|
    |**<span style="color:#ff3300;">BDUL</span>** |1 | 0 | <a href="../BDUL" title="Layer 3 interneuron" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#ff3300;">BDUL</span></span></a>|
    |**<span style="color:#ff3300;">BDUR</span>** |1 | 0 | <a href="../BDUR" title="Layer 3 interneuron" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#ff3300;">BDUR</span></span></a>|
    |**<span style="color:#ff3300;">CA01</span>** |1 | 0 | <a href="../CA01" title="Male interneuron" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#ff3300;">CA01</span></span></a>|
    |**<span style="color:#ff3300;">CA02</span>** |1 | 0 | <a href="../CA02" title="Male interneuron" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#ff3300;">CA02</span></span></a>|
    |**<span style="color:#ff3300;">CA03</span>** |1 | 0 | <a href="../CA03" title="Male interneuron" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#ff3300;">CA03</span></span></a>|
    |**<span style="color:#ff3300;">CA04</span>** |1 | 0 | <a href="../CA04" title="Male interneuron" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#ff3300;">CA04</span></span></a>|
    |**<span style="color:#ff3300;">CA05</span>** |1 | 0 | <a href="../CA05" title="Male interneuron" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#ff3300;">CA05</span></span></a>|
    |**<span style="color:#ff3300;">CA06</span>** |1 | 0 | <a href="../CA06" title="Male interneuron" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#ff3300;">CA06</span></span></a>|
    |**<span style="color:#ff3300;">CA07</span>** |1 | 0 | <a href="../CA07" title="Male interneuron" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#ff3300;">CA07</span></span></a>|
    |**<span style="color:#ff3300;">CA08</span>** |1 | 0 | <a href="../CA08" title="Male interneuron" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#ff3300;">CA08</span></span></a>|
    |**<span style="color:#ff3300;">CA09</span>** |1 | 0 | <a href="../CA09" title="Male interneuron" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#ff3300;">CA09</span></span></a>|
    |**<span style="color:#ff3300;">CP01</span>** |1 | 0 | <a href="../CP01" title="Male interneuron" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#ff3300;">CP01</span></span></a>|
    |**<span style="color:#ff3300;">CP02</span>** |1 | 0 | <a href="../CP02" title="Male interneuron" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#ff3300;">CP02</span></span></a>|
    |**<span style="color:#ff3300;">CP03</span>** |1 | 0 | <a href="../CP03" title="Male interneuron" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#ff3300;">CP03</span></span></a>|
    |**<span style="color:#ff3300;">CP04</span>** |1 | 0 | <a href="../CP04" title="Male interneuron" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#ff3300;">CP04</span></span></a>|
    |**<span style="color:#ff3300;">CP05</span>** |1 | 0 | <a href="../CP05" title="Male interneuron" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#ff3300;">CP05</span></span></a>|
    |**<span style="color:#ff3300;">CP06</span>** |1 | 0 | <a href="../CP06" title="Male interneuron" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#ff3300;">CP06</span></span></a>|
    |**<span style="color:#ff3300;">CP07</span>** |1 | 0 | <a href="../CP07" title="Male interneuron" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#ff3300;">CP07</span></span></a>|
    |**<span style="color:#ff3300;">CP08</span>** |1 | 0 | <a href="../CP08" title="Male interneuron" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#ff3300;">CP08</span></span></a>|
    |**<span style="color:#ff3300;">CP09</span>** |1 | 0 | <a href="../CP09" title="Male interneuron" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#ff3300;">CP09</span></span></a>|
    |**<span style="color:#ff3300;">DVB</span>** |1 | 0 | <a href="../DVB" title="Layer 3 interneuron" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#ff3300;">DVB</span></span></a>|
    |**<span style="color:#ff3300;">DVC</span>** |1 | 0 | <a href="../DVC" title="Layer 2 interneuron" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#ff3300;">DVC</span></span></a>|
    |**<span style="color:#ff3300;">DVE</span>** |1 | 0 | <a href="../DVE" title="Male interneuron" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#ff3300;">DVE</span></span></a>|
    |**<span style="color:#ff3300;">DVF</span>** |1 | 0 | <a href="../DVF" title="Male interneuron" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#ff3300;">DVF</span></span></a>|
    |**<span style="color:#ff3300;">DX1</span>** |1 | 0 | <a href="../DX1" title="Male interneuron" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#ff3300;">DX1</span></span></a>|
    |**<span style="color:#ff3300;">DX2</span>** |1 | 0 | <a href="../DX2" title="Male interneuron" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#ff3300;">DX2</span></span></a>|
    |**<span style="color:#ff3300;">DX3</span>** |1 | 0 | <a href="../DX3" title="Male interneuron" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#ff3300;">DX3</span></span></a>|
    |**<span style="color:#ff3300;">EF1</span>** |1 | 0 | <a href="../EF1" title="Male interneuron" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#ff3300;">EF1</span></span></a>|
    |**<span style="color:#ff3300;">EF2</span>** |1 | 0 | <a href="../EF2" title="Male interneuron" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#ff3300;">EF2</span></span></a>|
    |**<span style="color:#ff3300;">EF3</span>** |1 | 0 | <a href="../EF3" title="Male interneuron" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#ff3300;">EF3</span></span></a>|
    |**<span style="color:#ff3300;">LUAL</span>** |1 | 0 | <a href="../LUAL" title="Layer 3 interneuron" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#ff3300;">LUAL</span></span></a>|
    |**<span style="color:#ff3300;">LUAR</span>** |1 | 0 | <a href="../LUAR" title="Layer 3 interneuron" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#ff3300;">LUAR</span></span></a>|
    |**<span style="color:#ff3300;">MCML</span>** |1 | 0 | <a href="../MCML" title="Male head interneuron" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#ff3300;">MCML</span></span></a>|
    |**<span style="color:#ff3300;">MCMR</span>** |1 | 0 | <a href="../MCMR" title="Male head interneuron" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#ff3300;">MCMR</span></span></a>|
    |**<span style="color:#ff3300;">PDC</span>** |1 | 0 | <a href="../PDC" title="Male interneuron" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#ff3300;">PDC</span></span></a>|
    |**<span style="color:#ff3300;">PGA</span>** |1 | 0 | <a href="../PGA" title="Male interneuron" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#ff3300;">PGA</span></span></a>|
    |**<span style="color:#ff3300;">PVCL</span>** |1 | 1 | <a href="../PVCL" title="Layer 1 interneuron" style="text-decoration:none;"><strong><span style="color:#ff3300;">PVCL</span></strong></a>|
    |**<span style="color:#ff3300;">PVCR</span>** |1 | 1 | <a href="../PVCR" title="Layer 1 interneuron" style="text-decoration:none;"><strong><span style="color:#ff3300;">PVCR</span></strong></a>|
    |**<span style="color:#ff3300;">PVNL</span>** |1 | 0 | <a href="../PVNL" title="Layer 3 interneuron" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#ff3300;">PVNL</span></span></a>|
    |**<span style="color:#ff3300;">PVNR</span>** |1 | 0 | <a href="../PVNR" title="Layer 3 interneuron" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#ff3300;">PVNR</span></span></a>|
    |**<span style="color:#ff3300;">PVPL</span>** |1 | 0 | <a href="../PVPL" title="Layer 3 interneuron" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#ff3300;">PVPL</span></span></a>|
    |**<span style="color:#ff3300;">PVPR</span>** |1 | 0 | <a href="../PVPR" title="Layer 3 interneuron" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#ff3300;">PVPR</span></span></a>|
    |**<span style="color:#ff3300;">PVQL</span>** |1 | 0 | <a href="../PVQL" title="Layer 3 interneuron" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#ff3300;">PVQL</span></span></a>|
    |**<span style="color:#ff3300;">PVQR</span>** |1 | 0 | <a href="../PVQR" title="Layer 3 interneuron" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#ff3300;">PVQR</span></span></a>|
    |**<span style="color:#ff3300;">PVR</span>** |1 | 0 | <a href="../PVR" title="Layer 3 interneuron" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#ff3300;">PVR</span></span></a>|
    |**<span style="color:#ff3300;">PVT</span>** |1 | 0 | <a href="../PVT" title="Layer 2 interneuron" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#ff3300;">PVT</span></span></a>|
    |**<span style="color:#ff3300;">PVV</span>** |1 | 0 | <a href="../PVV" title="Male interneuron" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#ff3300;">PVV</span></span></a>|
    |**<span style="color:#ff3300;">PVWL</span>** |1 | 0 | <a href="../PVWL" title="Layer 2 interneuron" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#ff3300;">PVWL</span></span></a>|
    |**<span style="color:#ff3300;">PVWR</span>** |1 | 0 | <a href="../PVWR" title="Layer 2 interneuron" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#ff3300;">PVWR</span></span></a>|
    |**<span style="color:#ff3300;">PVX</span>** |1 | 0 | <a href="../PVX" title="Male interneuron" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#ff3300;">PVX</span></span></a>|
    |**<span style="color:#ff3300;">PVY</span>** |1 | 0 | <a href="../PVY" title="Male interneuron" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#ff3300;">PVY</span></span></a>|
    |**<span style="color:#ff3300;">PVZ</span>** |1 | 0 | <a href="../PVZ" title="Male interneuron" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#ff3300;">PVZ</span></span></a>|
    |**<span style="color:#ff3300;">RIAL</span>** |1 | 0 | <a href="../RIAL" title="Layer 1 interneuron" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#ff3300;">RIAL</span></span></a>|
    |**<span style="color:#ff3300;">RIAR</span>** |1 | 0 | <a href="../RIAR" title="Layer 1 interneuron" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#ff3300;">RIAR</span></span></a>|
    |**<span style="color:#ff3300;">RIBL</span>** |1 | 0 | <a href="../RIBL" title="Layer 2 interneuron" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#ff3300;">RIBL</span></span></a>|
    |**<span style="color:#ff3300;">RIBR</span>** |1 | 0 | <a href="../RIBR" title="Layer 2 interneuron" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#ff3300;">RIBR</span></span></a>|
    |**<span style="color:#ff3300;">RICL</span>** |1 | 0 | <a href="../RICL" title="Layer 2 interneuron" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#ff3300;">RICL</span></span></a>|
    |**<span style="color:#ff3300;">RICR</span>** |1 | 0 | <a href="../RICR" title="Layer 2 interneuron" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#ff3300;">RICR</span></span></a>|
    |**<span style="color:#ff3300;">RID</span>** |1 | 0 | <a href="../RID" title="Layer 1 interneuron" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#ff3300;">RID</span></span></a>|
    |**<span style="color:#ff3300;">RIFL</span>** |1 | 0 | <a href="../RIFL" title="Layer 3 interneuron" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#ff3300;">RIFL</span></span></a>|
    |**<span style="color:#ff3300;">RIFR</span>** |1 | 0 | <a href="../RIFR" title="Layer 3 interneuron" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#ff3300;">RIFR</span></span></a>|
    |**<span style="color:#ff3300;">RIGL</span>** |1 | 0 | <a href="../RIGL" title="Layer 2 interneuron" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#ff3300;">RIGL</span></span></a>|
    |**<span style="color:#ff3300;">RIGR</span>** |1 | 0 | <a href="../RIGR" title="Layer 2 interneuron" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#ff3300;">RIGR</span></span></a>|
    |**<span style="color:#ff3300;">RIH</span>** |1 | 0 | <a href="../RIH" title="Category 4 interneuron" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#ff3300;">RIH</span></span></a>|
    |**<span style="color:#ff3300;">RIML</span>** |1 | 0 | <a href="../RIML" title="Layer 1 interneuron; motorneuron in White et al., 1986" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#ff3300;">RIML</span></span></a>|
    |**<span style="color:#ff3300;">RIMR</span>** |1 | 0 | <a href="../RIMR" title="Layer 1 interneuron; motorneuron in White et al., 1986" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#ff3300;">RIMR</span></span></a>|
    |**<span style="color:#ff3300;">RIPL</span>** |1 | 0 | <a href="../RIPL" title="Linker to pharynx" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#ff3300;">RIPL</span></span></a>|
    |**<span style="color:#ff3300;">RIPR</span>** |1 | 0 | <a href="../RIPR" title="Linker to pharynx" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#ff3300;">RIPR</span></span></a>|
    |**<span style="color:#ff3300;">RIR</span>** |1 | 0 | <a href="../RIR" title="Category 4 interneuron" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#ff3300;">RIR</span></span></a>|
    |**<span style="color:#ff3300;">RIS</span>** |1 | 0 | <a href="../RIS" title="Layer 3 interneuron" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#ff3300;">RIS</span></span></a>|
    |**<span style="color:#ff3300;">RMFL</span>** |1 | 0 | <a href="../RMFL" title="Layer 2 interneuron" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#ff3300;">RMFL</span></span></a>|
    |**<span style="color:#ff3300;">RMFR</span>** |1 | 0 | <a href="../RMFR" title="Layer 2 interneuron" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#ff3300;">RMFR</span></span></a>|
    |**<span style="color:#ff3300;">RMGL</span>** |1 | 0 | <a href="../RMGL" title="Layer 2 interneuron" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#ff3300;">RMGL</span></span></a>|
    |**<span style="color:#ff3300;">RMGR</span>** |1 | 1 | <a href="../RMGR" title="Layer 2 interneuron" style="text-decoration:none;"><strong><span style="color:#ff3300;">RMGR</span></strong></a>|
    |**<span style="color:#ff3300;">SAADL</span>** |1 | 0 | <a href="../SAADL" title="Layer 2 interneuron" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#ff3300;">SAADL</span></span></a>|
    |**<span style="color:#ff3300;">SAADR</span>** |1 | 0 | <a href="../SAADR" title="Layer 2 interneuron" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#ff3300;">SAADR</span></span></a>|
    |**<span style="color:#ff3300;">SAAVL</span>** |1 | 0 | <a href="../SAAVL" title="Layer 2 interneuron" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#ff3300;">SAAVL</span></span></a>|
    |**<span style="color:#ff3300;">SAAVR</span>** |1 | 0 | <a href="../SAAVR" title="Layer 2 interneuron" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#ff3300;">SAAVR</span></span></a>|
    |**<span style="color:#ff3300;">URBL</span>** |1 | 0 | <a href="../URBL" title="Category 4 interneuron" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#ff3300;">URBL</span></span></a>|
    |**<span style="color:#ff3300;">URBR</span>** |1 | 0 | <a href="../URBR" title="Category 4 interneuron" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#ff3300;">URBR</span></span></a>|
    |**<span style="color:#9966cc;">AS1</span>** |1 | 0 | <a href="../AS1" title="Ventral cord motor neuron" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#9966cc;">AS1</span></span></a>|
    |**<span style="color:#9966cc;">AS10</span>** |1 | 0 | <a href="../AS10" title="Ventral cord motor neuron" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#9966cc;">AS10</span></span></a>|
    |**<span style="color:#9966cc;">AS11</span>** |1 | 0 | <a href="../AS11" title="Ventral cord motor neuron" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#9966cc;">AS11</span></span></a>|
    |**<span style="color:#9966cc;">AS2</span>** |1 | 0 | <a href="../AS2" title="Ventral cord motor neuron" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#9966cc;">AS2</span></span></a>|
    |**<span style="color:#9966cc;">AS3</span>** |1 | 0 | <a href="../AS3" title="Ventral cord motor neuron" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#9966cc;">AS3</span></span></a>|
    |**<span style="color:#9966cc;">AS4</span>** |1 | 0 | <a href="../AS4" title="Ventral cord motor neuron" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#9966cc;">AS4</span></span></a>|
    |**<span style="color:#9966cc;">AS5</span>** |1 | 0 | <a href="../AS5" title="Ventral cord motor neuron" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#9966cc;">AS5</span></span></a>|
    |**<span style="color:#9966cc;">AS6</span>** |1 | 0 | <a href="../AS6" title="Ventral cord motor neuron" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#9966cc;">AS6</span></span></a>|
    |**<span style="color:#9966cc;">AS7</span>** |1 | 0 | <a href="../AS7" title="Ventral cord motor neuron" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#9966cc;">AS7</span></span></a>|
    |**<span style="color:#9966cc;">AS8</span>** |1 | 0 | <a href="../AS8" title="Ventral cord motor neuron" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#9966cc;">AS8</span></span></a>|
    |**<span style="color:#9966cc;">AS9</span>** |1 | 0 | <a href="../AS9" title="Ventral cord motor neuron" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#9966cc;">AS9</span></span></a>|
    |**<span style="color:#9966cc;">DA1</span>** |1 | 0 | <a href="../DA1" title="Ventral cord motor neuron" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#9966cc;">DA1</span></span></a>|
    |**<span style="color:#9966cc;">DA2</span>** |1 | 0 | <a href="../DA2" title="Ventral cord motor neuron" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#9966cc;">DA2</span></span></a>|
    |**<span style="color:#9966cc;">DA3</span>** |1 | 0 | <a href="../DA3" title="Ventral cord motor neuron" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#9966cc;">DA3</span></span></a>|
    |**<span style="color:#9966cc;">DA4</span>** |1 | 0 | <a href="../DA4" title="Ventral cord motor neuron" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#9966cc;">DA4</span></span></a>|
    |**<span style="color:#9966cc;">DA5</span>** |1 | 0 | <a href="../DA5" title="Ventral cord motor neuron" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#9966cc;">DA5</span></span></a>|
    |**<span style="color:#9966cc;">DA6</span>** |1 | 0 | <a href="../DA6" title="Ventral cord motor neuron" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#9966cc;">DA6</span></span></a>|
    |**<span style="color:#9966cc;">DA7</span>** |1 | 0 | <a href="../DA7" title="Ventral cord motor neuron" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#9966cc;">DA7</span></span></a>|
    |**<span style="color:#9966cc;">DA8</span>** |1 | 0 | <a href="../DA8" title="Ventral cord motor neuron" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#9966cc;">DA8</span></span></a>|
    |**<span style="color:#9966cc;">DA9</span>** |1 | 0 | <a href="../DA9" title="Ventral cord motor neuron" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#9966cc;">DA9</span></span></a>|
    |**<span style="color:#9966cc;">DB1</span>** |1 | 0 | <a href="../DB1" title="Ventral cord motor neuron" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#9966cc;">DB1</span></span></a>|
    |**<span style="color:#9966cc;">DB2</span>** |1 | 0 | <a href="../DB2" title="Ventral cord motor neuron" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#9966cc;">DB2</span></span></a>|
    |**<span style="color:#9966cc;">DB3</span>** |1 | 0 | <a href="../DB3" title="Ventral cord motor neuron" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#9966cc;">DB3</span></span></a>|
    |**<span style="color:#9966cc;">DB4</span>** |1 | 1 | <a href="../DB4" title="Ventral cord motor neuron" style="text-decoration:none;"><strong><span style="color:#9966cc;">DB4</span></strong></a>|
    |**<span style="color:#9966cc;">DB5</span>** |1 | 0 | <a href="../DB5" title="Ventral cord motor neuron" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#9966cc;">DB5</span></span></a>|
    |**<span style="color:#9966cc;">DB6</span>** |1 | 0 | <a href="../DB6" title="Ventral cord motor neuron" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#9966cc;">DB6</span></span></a>|
    |**<span style="color:#9966cc;">DB7</span>** |1 | 0 | <a href="../DB7" title="Ventral cord motor neuron" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#9966cc;">DB7</span></span></a>|
    |**<span style="color:#9966cc;">DD1</span>** |1 | 0 | <a href="../DD1" title="Ventral cord motor neuron" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#9966cc;">DD1</span></span></a>|
    |**<span style="color:#9966cc;">DD2</span>** |1 | 0 | <a href="../DD2" title="Ventral cord motor neuron" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#9966cc;">DD2</span></span></a>|
    |**<span style="color:#9966cc;">DD3</span>** |1 | 0 | <a href="../DD3" title="Ventral cord motor neuron" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#9966cc;">DD3</span></span></a>|
    |**<span style="color:#9966cc;">DD4</span>** |1 | 1 | <a href="../DD4" title="Ventral cord motor neuron" style="text-decoration:none;"><strong><span style="color:#9966cc;">DD4</span></strong></a>|
    |**<span style="color:#9966cc;">DD5</span>** |1 | 1 | <a href="../DD5" title="Ventral cord motor neuron" style="text-decoration:none;"><strong><span style="color:#9966cc;">DD5</span></strong></a>|
    |**<span style="color:#9966cc;">DD6</span>** |1 | 0 | <a href="../DD6" title="Ventral cord motor neuron" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#9966cc;">DD6</span></span></a>|
    |**<span style="color:#9966cc;">HSNL</span>** |1 | 0 | <a href="../HSNL" title="Hermaphrodite specific motor neuron" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#9966cc;">HSNL</span></span></a>|
    |**<span style="color:#9966cc;">HSNR</span>** |1 | 0 | <a href="../HSNR" title="Hermaphrodite specific motor neuron" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#9966cc;">HSNR</span></span></a>|
    |**<span style="color:#9966cc;">PDA</span>** |1 | 0 | <a href="../PDA" title="Ventral cord motor neuron" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#9966cc;">PDA</span></span></a>|
    |**<span style="color:#9966cc;">PDB</span>** |1 | 0 | <a href="../PDB" title="Ventral cord motor neuron" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#9966cc;">PDB</span></span></a>|
    |**<span style="color:#9966cc;">RIVL</span>** |1 | 0 | <a href="../RIVL" title="Head motor neuron" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#9966cc;">RIVL</span></span></a>|
    |**<span style="color:#9966cc;">RIVR</span>** |1 | 0 | <a href="../RIVR" title="Head motor neuron" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#9966cc;">RIVR</span></span></a>|
    |**<span style="color:#9966cc;">RMDDL</span>** |1 | 0 | <a href="../RMDDL" title="Head motor neuron" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#9966cc;">RMDDL</span></span></a>|
    |**<span style="color:#9966cc;">RMDDR</span>** |1 | 0 | <a href="../RMDDR" title="Head motor neuron" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#9966cc;">RMDDR</span></span></a>|
    |**<span style="color:#9966cc;">RMDL</span>** |1 | 0 | <a href="../RMDL" title="Head motor neuron" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#9966cc;">RMDL</span></span></a>|
    |**<span style="color:#9966cc;">RMDR</span>** |1 | 0 | <a href="../RMDR" title="Head motor neuron" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#9966cc;">RMDR</span></span></a>|
    |**<span style="color:#9966cc;">RMDVL</span>** |1 | 0 | <a href="../RMDVL" title="Head motor neuron" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#9966cc;">RMDVL</span></span></a>|
    |**<span style="color:#9966cc;">RMDVR</span>** |1 | 0 | <a href="../RMDVR" title="Head motor neuron" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#9966cc;">RMDVR</span></span></a>|
    |**<span style="color:#9966cc;">RMED</span>** |1 | 0 | <a href="../RMED" title="Head motor neuron" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#9966cc;">RMED</span></span></a>|
    |**<span style="color:#9966cc;">RMEL</span>** |1 | 0 | <a href="../RMEL" title="Head motor neuron" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#9966cc;">RMEL</span></span></a>|
    |**<span style="color:#9966cc;">RMER</span>** |1 | 0 | <a href="../RMER" title="Head motor neuron" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#9966cc;">RMER</span></span></a>|
    |**<span style="color:#9966cc;">RMEV</span>** |1 | 0 | <a href="../RMEV" title="Head motor neuron" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#9966cc;">RMEV</span></span></a>|
    |**<span style="color:#9966cc;">RMHL</span>** |1 | 0 | <a href="../RMHL" title="Head motor neuron" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#9966cc;">RMHL</span></span></a>|
    |**<span style="color:#9966cc;">RMHR</span>** |1 | 0 | <a href="../RMHR" title="Head motor neuron" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#9966cc;">RMHR</span></span></a>|
    |**<span style="color:#9966cc;">SABD</span>** |1 | 0 | <a href="../SABD" title="Sublateral motor neuron; interneuron in White et al., 1986" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#9966cc;">SABD</span></span></a>|
    |**<span style="color:#9966cc;">SABVL</span>** |1 | 0 | <a href="../SABVL" title="Sublateral motor neuron; interneuron in White et al., 1986" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#9966cc;">SABVL</span></span></a>|
    |**<span style="color:#9966cc;">SABVR</span>** |1 | 0 | <a href="../SABVR" title="Sublateral motor neuron; interneuron in White et al., 1986" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#9966cc;">SABVR</span></span></a>|
    |**<span style="color:#9966cc;">SIADL</span>** |1 | 0 | <a href="../SIADL" title="Sublateral motor neuron; interneuron in White et al., 1986" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#9966cc;">SIADL</span></span></a>|
    |**<span style="color:#9966cc;">SIADR</span>** |1 | 0 | <a href="../SIADR" title="Sublateral motor neuron; interneuron in White et al., 1986" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#9966cc;">SIADR</span></span></a>|
    |**<span style="color:#9966cc;">SIAVL</span>** |1 | 0 | <a href="../SIAVL" title="Sublateral motor neuron; interneuron in White et al., 1986" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#9966cc;">SIAVL</span></span></a>|
    |**<span style="color:#9966cc;">SIAVR</span>** |1 | 0 | <a href="../SIAVR" title="Sublateral motor neuron; interneuron in White et al., 1986" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#9966cc;">SIAVR</span></span></a>|
    |**<span style="color:#9966cc;">SIBDL</span>** |1 | 0 | <a href="../SIBDL" title="Sublateral motor neuron; interneuron in White et al., 1986" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#9966cc;">SIBDL</span></span></a>|
    |**<span style="color:#9966cc;">SIBDR</span>** |1 | 0 | <a href="../SIBDR" title="Sublateral motor neuron; interneuron in White et al., 1986" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#9966cc;">SIBDR</span></span></a>|
    |**<span style="color:#9966cc;">SIBVL</span>** |1 | 0 | <a href="../SIBVL" title="Sublateral motor neuron; interneuron in White et al., 1986" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#9966cc;">SIBVL</span></span></a>|
    |**<span style="color:#9966cc;">SIBVR</span>** |1 | 0 | <a href="../SIBVR" title="Sublateral motor neuron; interneuron in White et al., 1986" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#9966cc;">SIBVR</span></span></a>|
    |**<span style="color:#9966cc;">SMBDL</span>** |1 | 0 | <a href="../SMBDL" title="Sublateral motor neuron" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#9966cc;">SMBDL</span></span></a>|
    |**<span style="color:#9966cc;">SMBDR</span>** |1 | 0 | <a href="../SMBDR" title="Sublateral motor neuron" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#9966cc;">SMBDR</span></span></a>|
    |**<span style="color:#9966cc;">SMBVL</span>** |1 | 0 | <a href="../SMBVL" title="Sublateral motor neuron" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#9966cc;">SMBVL</span></span></a>|
    |**<span style="color:#9966cc;">SMBVR</span>** |1 | 0 | <a href="../SMBVR" title="Sublateral motor neuron" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#9966cc;">SMBVR</span></span></a>|
    |**<span style="color:#9966cc;">SMDDL</span>** |1 | 0 | <a href="../SMDDL" title="Sublateral motor neuron" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#9966cc;">SMDDL</span></span></a>|
    |**<span style="color:#9966cc;">SMDDR</span>** |1 | 0 | <a href="../SMDDR" title="Sublateral motor neuron" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#9966cc;">SMDDR</span></span></a>|
    |**<span style="color:#9966cc;">SMDVL</span>** |1 | 0 | <a href="../SMDVL" title="Sublateral motor neuron" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#9966cc;">SMDVL</span></span></a>|
    |**<span style="color:#9966cc;">SMDVR</span>** |1 | 0 | <a href="../SMDVR" title="Sublateral motor neuron" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#9966cc;">SMDVR</span></span></a>|
    |**<span style="color:#9966cc;">URADL</span>** |1 | 0 | <a href="../URADL" title="Head motor neuron" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#9966cc;">URADL</span></span></a>|
    |**<span style="color:#9966cc;">URADR</span>** |1 | 0 | <a href="../URADR" title="Head motor neuron" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#9966cc;">URADR</span></span></a>|
    |**<span style="color:#9966cc;">URAVL</span>** |1 | 0 | <a href="../URAVL" title="Head motor neuron" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#9966cc;">URAVL</span></span></a>|
    |**<span style="color:#9966cc;">URAVR</span>** |1 | 0 | <a href="../URAVR" title="Head motor neuron" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#9966cc;">URAVR</span></span></a>|
    |**<span style="color:#9966cc;">VA1</span>** |1 | 0 | <a href="../VA1" title="Ventral cord motor neuron" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#9966cc;">VA1</span></span></a>|
    |**<span style="color:#9966cc;">VA10</span>** |1 | 0 | <a href="../VA10" title="Ventral cord motor neuron" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#9966cc;">VA10</span></span></a>|
    |**<span style="color:#9966cc;">VA11</span>** |1 | 0 | <a href="../VA11" title="Ventral cord motor neuron" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#9966cc;">VA11</span></span></a>|
    |**<span style="color:#9966cc;">VA12</span>** |1 | 0 | <a href="../VA12" title="Ventral cord motor neuron" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#9966cc;">VA12</span></span></a>|
    |**<span style="color:#9966cc;">VA2</span>** |1 | 0 | <a href="../VA2" title="Ventral cord motor neuron" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#9966cc;">VA2</span></span></a>|
    |**<span style="color:#9966cc;">VA3</span>** |1 | 1 | <a href="../VA3" title="Ventral cord motor neuron" style="text-decoration:none;"><strong><span style="color:#9966cc;">VA3</span></strong></a>|
    |**<span style="color:#9966cc;">VA4</span>** |1 | 0 | <a href="../VA4" title="Ventral cord motor neuron" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#9966cc;">VA4</span></span></a>|
    |**<span style="color:#9966cc;">VA5</span>** |1 | 0 | <a href="../VA5" title="Ventral cord motor neuron" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#9966cc;">VA5</span></span></a>|
    |**<span style="color:#9966cc;">VA6</span>** |1 | 1 | <a href="../VA6" title="Ventral cord motor neuron" style="text-decoration:none;"><strong><span style="color:#9966cc;">VA6</span></strong></a>|
    |**<span style="color:#9966cc;">VA7</span>** |1 | 0 | <a href="../VA7" title="Ventral cord motor neuron" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#9966cc;">VA7</span></span></a>|
    |**<span style="color:#9966cc;">VA8</span>** |1 | 0 | <a href="../VA8" title="Ventral cord motor neuron" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#9966cc;">VA8</span></span></a>|
    |**<span style="color:#9966cc;">VA9</span>** |1 | 0 | <a href="../VA9" title="Ventral cord motor neuron" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#9966cc;">VA9</span></span></a>|
    |**<span style="color:#9966cc;">VB1</span>** |1 | 0 | <a href="../VB1" title="Ventral cord motor neuron" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#9966cc;">VB1</span></span></a>|
    |**<span style="color:#9966cc;">VB10</span>** |1 | 0 | <a href="../VB10" title="Ventral cord motor neuron" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#9966cc;">VB10</span></span></a>|
    |**<span style="color:#9966cc;">VB11</span>** |1 | 0 | <a href="../VB11" title="Ventral cord motor neuron" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#9966cc;">VB11</span></span></a>|
    |**<span style="color:#9966cc;">VB2</span>** |1 | 1 | <a href="../VB2" title="Ventral cord motor neuron" style="text-decoration:none;"><strong><span style="color:#9966cc;">VB2</span></strong></a>|
    |**<span style="color:#9966cc;">VB3</span>** |1 | 0 | <a href="../VB3" title="Ventral cord motor neuron" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#9966cc;">VB3</span></span></a>|
    |**<span style="color:#9966cc;">VB4</span>** |1 | 0 | <a href="../VB4" title="Ventral cord motor neuron" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#9966cc;">VB4</span></span></a>|
    |**<span style="color:#9966cc;">VB5</span>** |1 | 0 | <a href="../VB5" title="Ventral cord motor neuron" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#9966cc;">VB5</span></span></a>|
    |**<span style="color:#9966cc;">VB6</span>** |1 | 1 | <a href="../VB6" title="Ventral cord motor neuron" style="text-decoration:none;"><strong><span style="color:#9966cc;">VB6</span></strong></a>|
    |**<span style="color:#9966cc;">VB7</span>** |1 | 0 | <a href="../VB7" title="Ventral cord motor neuron" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#9966cc;">VB7</span></span></a>|
    |**<span style="color:#9966cc;">VB8</span>** |1 | 0 | <a href="../VB8" title="Ventral cord motor neuron" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#9966cc;">VB8</span></span></a>|
    |**<span style="color:#9966cc;">VB9</span>** |1 | 0 | <a href="../VB9" title="Ventral cord motor neuron" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#9966cc;">VB9</span></span></a>|
    |**<span style="color:#9966cc;">VC1</span>** |1 | 0 | <a href="../VC1" title="Hermaphrodite specific motor neuron" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#9966cc;">VC1</span></span></a>|
    |**<span style="color:#9966cc;">VC2</span>** |1 | 0 | <a href="../VC2" title="Hermaphrodite specific motor neuron" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#9966cc;">VC2</span></span></a>|
    |**<span style="color:#9966cc;">VC3</span>** |1 | 0 | <a href="../VC3" title="Hermaphrodite specific motor neuron" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#9966cc;">VC3</span></span></a>|
    |**<span style="color:#9966cc;">VC4</span>** |1 | 0 | <a href="../VC4" title="Hermaphrodite specific motor neuron" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#9966cc;">VC4</span></span></a>|
    |**<span style="color:#9966cc;">VC5</span>** |1 | 0 | <a href="../VC5" title="Hermaphrodite specific motor neuron" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#9966cc;">VC5</span></span></a>|
    |**<span style="color:#9966cc;">VC6</span>** |1 | 0 | <a href="../VC6" title="Hermaphrodite specific motor neuron" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#9966cc;">VC6</span></span></a>|
    |**<span style="color:#9966cc;">VD1</span>** |1 | 0 | <a href="../VD1" title="Ventral cord motor neuron" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#9966cc;">VD1</span></span></a>|
    |**<span style="color:#9966cc;">VD10</span>** |1 | 0 | <a href="../VD10" title="Ventral cord motor neuron" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#9966cc;">VD10</span></span></a>|
    |**<span style="color:#9966cc;">VD11</span>** |1 | 0 | <a href="../VD11" title="Ventral cord motor neuron" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#9966cc;">VD11</span></span></a>|
    |**<span style="color:#9966cc;">VD12</span>** |1 | 0 | <a href="../VD12" title="Ventral cord motor neuron" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#9966cc;">VD12</span></span></a>|
    |**<span style="color:#9966cc;">VD13</span>** |1 | 0 | <a href="../VD13" title="Ventral cord motor neuron" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#9966cc;">VD13</span></span></a>|
    |**<span style="color:#9966cc;">VD2</span>** |1 | 0 | <a href="../VD2" title="Ventral cord motor neuron" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#9966cc;">VD2</span></span></a>|
    |**<span style="color:#9966cc;">VD3</span>** |1 | 1 | <a href="../VD3" title="Ventral cord motor neuron" style="text-decoration:none;"><strong><span style="color:#9966cc;">VD3</span></strong></a>|
    |**<span style="color:#9966cc;">VD4</span>** |1 | 0 | <a href="../VD4" title="Ventral cord motor neuron" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#9966cc;">VD4</span></span></a>|
    |**<span style="color:#9966cc;">VD5</span>** |1 | 0 | <a href="../VD5" title="Ventral cord motor neuron" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#9966cc;">VD5</span></span></a>|
    |**<span style="color:#9966cc;">VD6</span>** |1 | 1 | <a href="../VD6" title="Ventral cord motor neuron" style="text-decoration:none;"><strong><span style="color:#9966cc;">VD6</span></strong></a>|
    |**<span style="color:#9966cc;">VD7</span>** |1 | 0 | <a href="../VD7" title="Ventral cord motor neuron" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#9966cc;">VD7</span></span></a>|
    |**<span style="color:#9966cc;">VD8</span>** |1 | 0 | <a href="../VD8" title="Ventral cord motor neuron" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#9966cc;">VD8</span></span></a>|
    |**<span style="color:#9966cc;">VD9</span>** |1 | 0 | <a href="../VD9" title="Ventral cord motor neuron" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#9966cc;">VD9</span></span></a>|
    |**<span style="color:#990033;">CANL</span>** |1 | 0 | <a href="../CANL" title="Canal neuron" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#990033;">CANL</span></span></a>|
    |**<span style="color:#990033;">CANR</span>** |1 | 0 | <a href="../CANR" title="Canal neuron" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#990033;">CANR</span></span></a>|
    |**<span style="color:#9966cc;">DA10</span>** |1 | 0 | <a href="../DA10" title="NOT AN ACTUAL C. ELEGANS NEURON! A cell by this name is sometimes used in computational models of worm locomotion" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#9966cc;">DA10</span></span></a>|
    |**<span style="color:#9966cc;">DB10</span>** |1 | 0 | <a href="../DB10" title="NOT AN ACTUAL C. ELEGANS NEURON! A cell by this name is sometimes used in computational models of worm locomotion" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#9966cc;">DB10</span></span></a>|
    |**<span style="color:#9966cc;">DB8</span>** |1 | 0 | <a href="../DB8" title="NOT AN ACTUAL C. ELEGANS NEURON! A cell by this name is sometimes used in computational models of worm locomotion" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#9966cc;">DB8</span></span></a>|
    |**<span style="color:#9966cc;">DB9</span>** |1 | 0 | <a href="../DB9" title="NOT AN ACTUAL C. ELEGANS NEURON! A cell by this name is sometimes used in computational models of worm locomotion" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#9966cc;">DB9</span></span></a>|
    |**<span style="color:#9966cc;">DD10</span>** |1 | 0 | <a href="../DD10" title="NOT AN ACTUAL C. ELEGANS NEURON! A cell by this name is sometimes used in computational models of worm locomotion" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#9966cc;">DD10</span></span></a>|
    |**<span style="color:#9966cc;">DD7</span>** |1 | 0 | <a href="../DD7" title="NOT AN ACTUAL C. ELEGANS NEURON! A cell by this name is sometimes used in computational models of worm locomotion" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#9966cc;">DD7</span></span></a>|
    |**<span style="color:#9966cc;">DD8</span>** |1 | 0 | <a href="../DD8" title="NOT AN ACTUAL C. ELEGANS NEURON! A cell by this name is sometimes used in computational models of worm locomotion" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#9966cc;">DD8</span></span></a>|
    |**<span style="color:#9966cc;">DD9</span>** |1 | 0 | <a href="../DD9" title="NOT AN ACTUAL C. ELEGANS NEURON! A cell by this name is sometimes used in computational models of worm locomotion" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#9966cc;">DD9</span></span></a>|
    |**<span style="color:#336600;">BWM</span>** |1 | 0 | <a href="../BWM" title="Unspecified body wall muscle" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#336600;">BWM</span></span></a>|
    |**<span style="color:#669900;">MANAL</span>** |1 | 0 | <a href="../MANAL" title="Anal/sphincter muscle" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#669900;">MANAL</span></span></a>|
    |**<span style="color:#336600;">MDL01</span>** |1 | 0 | <a href="../MDL01" title="Head muscle" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#336600;">MDL01</span></span></a>|
    |**<span style="color:#336600;">MDL02</span>** |1 | 0 | <a href="../MDL02" title="Head muscle" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#336600;">MDL02</span></span></a>|
    |**<span style="color:#336600;">MDL03</span>** |1 | 0 | <a href="../MDL03" title="Head muscle" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#336600;">MDL03</span></span></a>|
    |**<span style="color:#336600;">MDL04</span>** |1 | 0 | <a href="../MDL04" title="Head muscle" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#336600;">MDL04</span></span></a>|
    |**<span style="color:#336600;">MDL05</span>** |1 | 0 | <a href="../MDL05" title="Head muscle" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#336600;">MDL05</span></span></a>|
    |**<span style="color:#336600;">MDL06</span>** |1 | 0 | <a href="../MDL06" title="Head muscle" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#336600;">MDL06</span></span></a>|
    |**<span style="color:#336600;">MDL07</span>** |1 | 0 | <a href="../MDL07" title="Head muscle" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#336600;">MDL07</span></span></a>|
    |**<span style="color:#336600;">MDL08</span>** |1 | 0 | <a href="../MDL08" title="Main body muscle" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#336600;">MDL08</span></span></a>|
    |**<span style="color:#336600;">MDL09</span>** |1 | 0 | <a href="../MDL09" title="Main body muscle" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#336600;">MDL09</span></span></a>|
    |**<span style="color:#336600;">MDL10</span>** |1 | 0 | <a href="../MDL10" title="Main body muscle" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#336600;">MDL10</span></span></a>|
    |**<span style="color:#336600;">MDL11</span>** |1 | 0 | <a href="../MDL11" title="Main body muscle" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#336600;">MDL11</span></span></a>|
    |**<span style="color:#336600;">MDL12</span>** |1 | 0 | <a href="../MDL12" title="Main body muscle" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#336600;">MDL12</span></span></a>|
    |**<span style="color:#336600;">MDL13</span>** |1 | 0 | <a href="../MDL13" title="Main body muscle" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#336600;">MDL13</span></span></a>|
    |**<span style="color:#336600;">MDL14</span>** |1 | 0 | <a href="../MDL14" title="Main body muscle" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#336600;">MDL14</span></span></a>|
    |**<span style="color:#336600;">MDL15</span>** |1 | 0 | <a href="../MDL15" title="Main body muscle" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#336600;">MDL15</span></span></a>|
    |**<span style="color:#336600;">MDL16</span>** |1 | 0 | <a href="../MDL16" title="Main body muscle" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#336600;">MDL16</span></span></a>|
    |**<span style="color:#336600;">MDL17</span>** |1 | 0 | <a href="../MDL17" title="Main body muscle" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#336600;">MDL17</span></span></a>|
    |**<span style="color:#336600;">MDL18</span>** |1 | 0 | <a href="../MDL18" title="Main body muscle" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#336600;">MDL18</span></span></a>|
    |**<span style="color:#336600;">MDL19</span>** |1 | 0 | <a href="../MDL19" title="Main body muscle" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#336600;">MDL19</span></span></a>|
    |**<span style="color:#336600;">MDL20</span>** |1 | 0 | <a href="../MDL20" title="Main body muscle" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#336600;">MDL20</span></span></a>|
    |**<span style="color:#336600;">MDL21</span>** |1 | 0 | <a href="../MDL21" title="Main body muscle" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#336600;">MDL21</span></span></a>|
    |**<span style="color:#336600;">MDL22</span>** |1 | 0 | <a href="../MDL22" title="Main body muscle" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#336600;">MDL22</span></span></a>|
    |**<span style="color:#336600;">MDL23</span>** |1 | 0 | <a href="../MDL23" title="Main body muscle" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#336600;">MDL23</span></span></a>|
    |**<span style="color:#336600;">MDL24</span>** |1 | 0 | <a href="../MDL24" title="Main body muscle" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#336600;">MDL24</span></span></a>|
    |**<span style="color:#336600;">MDR01</span>** |1 | 0 | <a href="../MDR01" title="Head muscle" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#336600;">MDR01</span></span></a>|
    |**<span style="color:#336600;">MDR02</span>** |1 | 0 | <a href="../MDR02" title="Head muscle" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#336600;">MDR02</span></span></a>|
    |**<span style="color:#336600;">MDR03</span>** |1 | 0 | <a href="../MDR03" title="Head muscle" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#336600;">MDR03</span></span></a>|
    |**<span style="color:#336600;">MDR04</span>** |1 | 0 | <a href="../MDR04" title="Head muscle" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#336600;">MDR04</span></span></a>|
    |**<span style="color:#336600;">MDR05</span>** |1 | 0 | <a href="../MDR05" title="Head muscle" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#336600;">MDR05</span></span></a>|
    |**<span style="color:#336600;">MDR06</span>** |1 | 0 | <a href="../MDR06" title="Head muscle" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#336600;">MDR06</span></span></a>|
    |**<span style="color:#336600;">MDR07</span>** |1 | 0 | <a href="../MDR07" title="Head muscle" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#336600;">MDR07</span></span></a>|
    |**<span style="color:#336600;">MDR08</span>** |1 | 0 | <a href="../MDR08" title="Main body muscle" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#336600;">MDR08</span></span></a>|
    |**<span style="color:#336600;">MDR09</span>** |1 | 0 | <a href="../MDR09" title="Main body muscle" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#336600;">MDR09</span></span></a>|
    |**<span style="color:#336600;">MDR10</span>** |1 | 0 | <a href="../MDR10" title="Main body muscle" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#336600;">MDR10</span></span></a>|
    |**<span style="color:#336600;">MDR11</span>** |1 | 0 | <a href="../MDR11" title="Main body muscle" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#336600;">MDR11</span></span></a>|
    |**<span style="color:#336600;">MDR12</span>** |1 | 0 | <a href="../MDR12" title="Main body muscle" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#336600;">MDR12</span></span></a>|
    |**<span style="color:#336600;">MDR13</span>** |1 | 0 | <a href="../MDR13" title="Main body muscle" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#336600;">MDR13</span></span></a>|
    |**<span style="color:#336600;">MDR14</span>** |1 | 0 | <a href="../MDR14" title="Main body muscle" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#336600;">MDR14</span></span></a>|
    |**<span style="color:#336600;">MDR15</span>** |1 | 0 | <a href="../MDR15" title="Main body muscle" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#336600;">MDR15</span></span></a>|
    |**<span style="color:#336600;">MDR16</span>** |1 | 0 | <a href="../MDR16" title="Main body muscle" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#336600;">MDR16</span></span></a>|
    |**<span style="color:#336600;">MDR17</span>** |1 | 0 | <a href="../MDR17" title="Main body muscle" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#336600;">MDR17</span></span></a>|
    |**<span style="color:#336600;">MDR18</span>** |1 | 0 | <a href="../MDR18" title="Main body muscle" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#336600;">MDR18</span></span></a>|
    |**<span style="color:#336600;">MDR19</span>** |1 | 0 | <a href="../MDR19" title="Main body muscle" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#336600;">MDR19</span></span></a>|
    |**<span style="color:#336600;">MDR20</span>** |1 | 0 | <a href="../MDR20" title="Main body muscle" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#336600;">MDR20</span></span></a>|
    |**<span style="color:#336600;">MDR21</span>** |1 | 0 | <a href="../MDR21" title="Main body muscle" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#336600;">MDR21</span></span></a>|
    |**<span style="color:#336600;">MDR22</span>** |1 | 0 | <a href="../MDR22" title="Main body muscle" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#336600;">MDR22</span></span></a>|
    |**<span style="color:#336600;">MDR23</span>** |1 | 0 | <a href="../MDR23" title="Main body muscle" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#336600;">MDR23</span></span></a>|
    |**<span style="color:#336600;">MDR24</span>** |1 | 0 | <a href="../MDR24" title="Main body muscle" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#336600;">MDR24</span></span></a>|
    |**<span style="color:#336600;">MVL01</span>** |1 | 0 | <a href="../MVL01" title="Head muscle" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#336600;">MVL01</span></span></a>|
    |**<span style="color:#336600;">MVL02</span>** |1 | 0 | <a href="../MVL02" title="Head muscle" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#336600;">MVL02</span></span></a>|
    |**<span style="color:#336600;">MVL03</span>** |1 | 0 | <a href="../MVL03" title="Head muscle" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#336600;">MVL03</span></span></a>|
    |**<span style="color:#336600;">MVL04</span>** |1 | 0 | <a href="../MVL04" title="Head muscle" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#336600;">MVL04</span></span></a>|
    |**<span style="color:#336600;">MVL05</span>** |1 | 0 | <a href="../MVL05" title="Head muscle" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#336600;">MVL05</span></span></a>|
    |**<span style="color:#336600;">MVL06</span>** |1 | 0 | <a href="../MVL06" title="Head muscle" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#336600;">MVL06</span></span></a>|
    |**<span style="color:#336600;">MVL07</span>** |1 | 0 | <a href="../MVL07" title="Head muscle" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#336600;">MVL07</span></span></a>|
    |**<span style="color:#336600;">MVL08</span>** |1 | 0 | <a href="../MVL08" title="Main body muscle" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#336600;">MVL08</span></span></a>|
    |**<span style="color:#336600;">MVL09</span>** |1 | 0 | <a href="../MVL09" title="Main body muscle" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#336600;">MVL09</span></span></a>|
    |**<span style="color:#336600;">MVL10</span>** |1 | 0 | <a href="../MVL10" title="Main body muscle" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#336600;">MVL10</span></span></a>|
    |**<span style="color:#336600;">MVL11</span>** |1 | 0 | <a href="../MVL11" title="Main body muscle" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#336600;">MVL11</span></span></a>|
    |**<span style="color:#336600;">MVL12</span>** |1 | 0 | <a href="../MVL12" title="Main body muscle" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#336600;">MVL12</span></span></a>|
    |**<span style="color:#336600;">MVL13</span>** |1 | 0 | <a href="../MVL13" title="Main body muscle" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#336600;">MVL13</span></span></a>|
    |**<span style="color:#336600;">MVL14</span>** |1 | 0 | <a href="../MVL14" title="Main body muscle" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#336600;">MVL14</span></span></a>|
    |**<span style="color:#336600;">MVL15</span>** |1 | 0 | <a href="../MVL15" title="Main body muscle" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#336600;">MVL15</span></span></a>|
    |**<span style="color:#336600;">MVL16</span>** |1 | 0 | <a href="../MVL16" title="Main body muscle" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#336600;">MVL16</span></span></a>|
    |**<span style="color:#336600;">MVL17</span>** |1 | 0 | <a href="../MVL17" title="Main body muscle" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#336600;">MVL17</span></span></a>|
    |**<span style="color:#336600;">MVL18</span>** |1 | 0 | <a href="../MVL18" title="Main body muscle" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#336600;">MVL18</span></span></a>|
    |**<span style="color:#336600;">MVL19</span>** |1 | 0 | <a href="../MVL19" title="Main body muscle" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#336600;">MVL19</span></span></a>|
    |**<span style="color:#336600;">MVL20</span>** |1 | 0 | <a href="../MVL20" title="Main body muscle" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#336600;">MVL20</span></span></a>|
    |**<span style="color:#336600;">MVL21</span>** |1 | 0 | <a href="../MVL21" title="Main body muscle" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#336600;">MVL21</span></span></a>|
    |**<span style="color:#336600;">MVL22</span>** |1 | 0 | <a href="../MVL22" title="Main body muscle" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#336600;">MVL22</span></span></a>|
    |**<span style="color:#336600;">MVL23</span>** |1 | 0 | <a href="../MVL23" title="Main body muscle" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#336600;">MVL23</span></span></a>|
    |**<span style="color:#336600;">MVR01</span>** |1 | 0 | <a href="../MVR01" title="Head muscle" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#336600;">MVR01</span></span></a>|
    |**<span style="color:#336600;">MVR02</span>** |1 | 0 | <a href="../MVR02" title="Head muscle" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#336600;">MVR02</span></span></a>|
    |**<span style="color:#336600;">MVR03</span>** |1 | 0 | <a href="../MVR03" title="Head muscle" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#336600;">MVR03</span></span></a>|
    |**<span style="color:#336600;">MVR04</span>** |1 | 0 | <a href="../MVR04" title="Head muscle" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#336600;">MVR04</span></span></a>|
    |**<span style="color:#336600;">MVR05</span>** |1 | 0 | <a href="../MVR05" title="Head muscle" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#336600;">MVR05</span></span></a>|
    |**<span style="color:#336600;">MVR06</span>** |1 | 0 | <a href="../MVR06" title="Head muscle" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#336600;">MVR06</span></span></a>|
    |**<span style="color:#336600;">MVR07</span>** |1 | 0 | <a href="../MVR07" title="Head muscle" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#336600;">MVR07</span></span></a>|
    |**<span style="color:#336600;">MVR08</span>** |1 | 0 | <a href="../MVR08" title="Main body muscle" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#336600;">MVR08</span></span></a>|
    |**<span style="color:#336600;">MVR09</span>** |1 | 0 | <a href="../MVR09" title="Main body muscle" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#336600;">MVR09</span></span></a>|
    |**<span style="color:#336600;">MVR10</span>** |1 | 0 | <a href="../MVR10" title="Main body muscle" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#336600;">MVR10</span></span></a>|
    |**<span style="color:#336600;">MVR11</span>** |1 | 0 | <a href="../MVR11" title="Main body muscle" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#336600;">MVR11</span></span></a>|
    |**<span style="color:#336600;">MVR12</span>** |1 | 0 | <a href="../MVR12" title="Main body muscle" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#336600;">MVR12</span></span></a>|
    |**<span style="color:#336600;">MVR13</span>** |1 | 0 | <a href="../MVR13" title="Main body muscle" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#336600;">MVR13</span></span></a>|
    |**<span style="color:#336600;">MVR14</span>** |1 | 0 | <a href="../MVR14" title="Main body muscle" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#336600;">MVR14</span></span></a>|
    |**<span style="color:#336600;">MVR15</span>** |1 | 0 | <a href="../MVR15" title="Main body muscle" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#336600;">MVR15</span></span></a>|
    |**<span style="color:#336600;">MVR16</span>** |1 | 0 | <a href="../MVR16" title="Main body muscle" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#336600;">MVR16</span></span></a>|
    |**<span style="color:#336600;">MVR17</span>** |1 | 0 | <a href="../MVR17" title="Main body muscle" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#336600;">MVR17</span></span></a>|
    |**<span style="color:#336600;">MVR18</span>** |1 | 0 | <a href="../MVR18" title="Main body muscle" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#336600;">MVR18</span></span></a>|
    |**<span style="color:#336600;">MVR19</span>** |1 | 0 | <a href="../MVR19" title="Main body muscle" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#336600;">MVR19</span></span></a>|
    |**<span style="color:#336600;">MVR20</span>** |1 | 0 | <a href="../MVR20" title="Main body muscle" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#336600;">MVR20</span></span></a>|
    |**<span style="color:#336600;">MVR21</span>** |1 | 0 | <a href="../MVR21" title="Main body muscle" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#336600;">MVR21</span></span></a>|
    |**<span style="color:#336600;">MVR22</span>** |1 | 0 | <a href="../MVR22" title="Main body muscle" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#336600;">MVR22</span></span></a>|
    |**<span style="color:#336600;">MVR23</span>** |1 | 0 | <a href="../MVR23" title="Main body muscle" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#336600;">MVR23</span></span></a>|
    |**<span style="color:#336600;">MVR24</span>** |1 | 0 | <a href="../MVR24" title="Main body muscle" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#336600;">MVR24</span></span></a>|
    |**<span style="color:#99cc66;">MVULVA</span>** |1 | 0 | <a href="../MVULVA" title="Vulval muscle" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#99cc66;">MVULVA</span></span></a>|
    |**<span style="color:#99cc33;">ailL</span>** |1 | 0 | <a href="../ailL" title="Anterior inner longitudinal muscle (male specific)" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#99cc33;">ailL</span></span></a>|
    |**<span style="color:#99cc33;">ailR</span>** |1 | 0 | <a href="../ailR" title="Anterior inner longitudinal muscle (male specific)" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#99cc33;">ailR</span></span></a>|
    |**<span style="color:#33cc99;">aobL</span>** |1 | 0 | <a href="../aobL" title="Anterior oblique (male specific)" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#33cc99;">aobL</span></span></a>|
    |**<span style="color:#33cc99;">aobR</span>** |1 | 0 | <a href="../aobR" title="Anterior oblique (male specific)" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#33cc99;">aobR</span></span></a>|
    |**<span style="color:#99cc99;">cdlL</span>** |1 | 0 | <a href="../cdlL" title="Caudal longitudinal muscle (male specific)" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#99cc99;">cdlL</span></span></a>|
    |**<span style="color:#99cc99;">cdlR</span>** |1 | 0 | <a href="../cdlR" title="Caudal longitudinal muscle (male specific)" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#99cc99;">cdlR</span></span></a>|
    |**<span style="color:#66cc66;">dglL1</span>** |1 | 0 | <a href="../dglL1" title="Diagonal muscle (male specific)" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#66cc66;">dglL1</span></span></a>|
    |**<span style="color:#66cc66;">dglL2</span>** |1 | 0 | <a href="../dglL2" title="Diagonal muscle (male specific)" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#66cc66;">dglL2</span></span></a>|
    |**<span style="color:#66cc66;">dglL3</span>** |1 | 0 | <a href="../dglL3" title="Diagonal muscle (male specific)" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#66cc66;">dglL3</span></span></a>|
    |**<span style="color:#66cc66;">dglL4</span>** |1 | 0 | <a href="../dglL4" title="Diagonal muscle (male specific)" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#66cc66;">dglL4</span></span></a>|
    |**<span style="color:#66cc66;">dglL5</span>** |1 | 0 | <a href="../dglL5" title="Diagonal muscle (male specific)" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#66cc66;">dglL5</span></span></a>|
    |**<span style="color:#66cc66;">dglL6</span>** |1 | 0 | <a href="../dglL6" title="Diagonal muscle (male specific)" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#66cc66;">dglL6</span></span></a>|
    |**<span style="color:#66cc66;">dglL7</span>** |1 | 0 | <a href="../dglL7" title="Diagonal muscle (male specific)" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#66cc66;">dglL7</span></span></a>|
    |**<span style="color:#66cc66;">dglR1</span>** |1 | 0 | <a href="../dglR1" title="Diagonal muscle (male specific)" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#66cc66;">dglR1</span></span></a>|
    |**<span style="color:#66cc66;">dglR2</span>** |1 | 0 | <a href="../dglR2" title="Diagonal muscle (male specific)" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#66cc66;">dglR2</span></span></a>|
    |**<span style="color:#66cc66;">dglR3</span>** |1 | 0 | <a href="../dglR3" title="Diagonal muscle (male specific)" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#66cc66;">dglR3</span></span></a>|
    |**<span style="color:#66cc66;">dglR4</span>** |1 | 0 | <a href="../dglR4" title="Diagonal muscle (male specific)" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#66cc66;">dglR4</span></span></a>|
    |**<span style="color:#66cc66;">dglR5</span>** |1 | 0 | <a href="../dglR5" title="Diagonal muscle (male specific)" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#66cc66;">dglR5</span></span></a>|
    |**<span style="color:#66cc66;">dglR6</span>** |1 | 0 | <a href="../dglR6" title="Diagonal muscle (male specific)" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#66cc66;">dglR6</span></span></a>|
    |**<span style="color:#66cc66;">dglR7</span>** |1 | 0 | <a href="../dglR7" title="Diagonal muscle (male specific)" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#66cc66;">dglR7</span></span></a>|
    |**<span style="color:#66cc66;">dglR8</span>** |1 | 0 | <a href="../dglR8" title="Diagonal muscle (male specific)" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#66cc66;">dglR8</span></span></a>|
    |**<span style="color:#99ff99;">dspL</span>** |1 | 0 | <a href="../dspL" title="Dorsal spicule protractor (male specific)" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#99ff99;">dspL</span></span></a>|
    |**<span style="color:#99ff99;">dspR</span>** |1 | 0 | <a href="../dspR" title="Dorsal spicule protractor (male specific)" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#99ff99;">dspR</span></span></a>|
    |**<span style="color:#669966;">dsrL</span>** |1 | 0 | <a href="../dsrL" title="Dorsal spicule retractor (male specific)" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#669966;">dsrL</span></span></a>|
    |**<span style="color:#669966;">dsrR</span>** |1 | 0 | <a href="../dsrR" title="Dorsal spicule retractor (male specific)" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#669966;">dsrR</span></span></a>|
    |**<span style="color:#66ff33;">gecL</span>** |1 | 0 | <a href="../gecL" title="Gubernacular erector (male specific)" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#66ff33;">gecL</span></span></a>|
    |**<span style="color:#66ff33;">gecR</span>** |1 | 0 | <a href="../gecR" title="Gubernacular erector (male specific)" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#66ff33;">gecR</span></span></a>|
    |**<span style="color:#99ffcc;">grtL</span>** |1 | 0 | <a href="../grtL" title="Gubernacular retractor (male specific)" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#99ffcc;">grtL</span></span></a>|
    |**<span style="color:#99ffcc;">grtR</span>** |1 | 0 | <a href="../grtR" title="Gubernacular retractor (male specific)" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#99ffcc;">grtR</span></span></a>|
    |**<span style="color:#669900;">mu_anal</span>** |1 | 0 | <a href="../mu_anal" title="Anal/sphincter muscle" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#669900;">mu_anal</span></span></a>|
    |**<span style="color:#006600;">mu_intL</span>** |1 | 0 | <a href="../mu_intL" title="Intestinal muscles" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#006600;">mu_intL</span></span></a>|
    |**<span style="color:#006600;">mu_intR</span>** |1 | 0 | <a href="../mu_intR" title="Intestinal muscles" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#006600;">mu_intR</span></span></a>|
    |**<span style="color:#669900;">mu_sph</span>** |1 | 0 | <a href="../mu_sph" title="Anal/sphincter muscle" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#669900;">mu_sph</span></span></a>|
    |**<span style="color:#ccff33;">pilL</span>** |1 | 0 | <a href="../pilL" title="Posterior inner longitudinal muscle (male specific)" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#ccff33;">pilL</span></span></a>|
    |**<span style="color:#ccff33;">pilR</span>** |1 | 0 | <a href="../pilR" title="Posterior inner longitudinal muscle (male specific)" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#ccff33;">pilR</span></span></a>|
    |**<span style="color:#33cC00;">pm1</span>** |1 | 0 | <a href="../pm1" title="Pharyngeal muscle" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#33cC00;">pm1</span></span></a>|
    |**<span style="color:#ccf199;">pm2D</span>** |1 | 0 | <a href="../pm2D" title="Pharyngeal muscle" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#ccf199;">pm2D</span></span></a>|
    |**<span style="color:#ccf199;">pm2VL</span>** |1 | 0 | <a href="../pm2VL" title="Pharyngeal muscle" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#ccf199;">pm2VL</span></span></a>|
    |**<span style="color:#ccf199;">pm2VR</span>** |1 | 0 | <a href="../pm2VR" title="Pharyngeal muscle" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#ccf199;">pm2VR</span></span></a>|
    |**<span style="color:#33cC00;">pm3D</span>** |1 | 0 | <a href="../pm3D" title="Pharyngeal muscle" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#33cC00;">pm3D</span></span></a>|
    |**<span style="color:#33cC00;">pm3VL</span>** |1 | 0 | <a href="../pm3VL" title="Pharyngeal muscle" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#33cC00;">pm3VL</span></span></a>|
    |**<span style="color:#33cC00;">pm3VR</span>** |1 | 0 | <a href="../pm3VR" title="Pharyngeal muscle" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#33cC00;">pm3VR</span></span></a>|
    |**<span style="color:#ccf199;">pm4D</span>** |1 | 0 | <a href="../pm4D" title="Pharyngeal muscle" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#ccf199;">pm4D</span></span></a>|
    |**<span style="color:#ccf199;">pm4VL</span>** |1 | 0 | <a href="../pm4VL" title="Pharyngeal muscle" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#ccf199;">pm4VL</span></span></a>|
    |**<span style="color:#ccf199;">pm4VR</span>** |1 | 0 | <a href="../pm4VR" title="Pharyngeal muscle" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#ccf199;">pm4VR</span></span></a>|
    |**<span style="color:#ccf199;">pm4_UNSPECIFIED</span>** |1 | 0 | <a href="../pm4_UNSPECIFIED" title="Pharyngeal muscle" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#ccf199;">pm4_UNSPECIFIED</span></span></a>|
    |**<span style="color:#33cC00;">pm5D</span>** |1 | 0 | <a href="../pm5D" title="Pharyngeal muscle" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#33cC00;">pm5D</span></span></a>|
    |**<span style="color:#33cC00;">pm5VL</span>** |1 | 0 | <a href="../pm5VL" title="Pharyngeal muscle" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#33cC00;">pm5VL</span></span></a>|
    |**<span style="color:#33cC00;">pm5VR</span>** |1 | 0 | <a href="../pm5VR" title="Pharyngeal muscle" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#33cC00;">pm5VR</span></span></a>|
    |**<span style="color:#ccf199;">pm6D</span>** |1 | 0 | <a href="../pm6D" title="Pharyngeal muscle" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#ccf199;">pm6D</span></span></a>|
    |**<span style="color:#ccf199;">pm6VL</span>** |1 | 0 | <a href="../pm6VL" title="Pharyngeal muscle" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#ccf199;">pm6VL</span></span></a>|
    |**<span style="color:#ccf199;">pm6VR</span>** |1 | 0 | <a href="../pm6VR" title="Pharyngeal muscle" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#ccf199;">pm6VR</span></span></a>|
    |**<span style="color:#33cC00;">pm7D</span>** |1 | 0 | <a href="../pm7D" title="Pharyngeal muscle" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#33cC00;">pm7D</span></span></a>|
    |**<span style="color:#33cC00;">pm7VL</span>** |1 | 0 | <a href="../pm7VL" title="Pharyngeal muscle" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#33cC00;">pm7VL</span></span></a>|
    |**<span style="color:#33cC00;">pm7VR</span>** |1 | 0 | <a href="../pm7VR" title="Pharyngeal muscle" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#33cC00;">pm7VR</span></span></a>|
    |**<span style="color:#ccf199;">pm8</span>** |1 | 0 | <a href="../pm8" title="Pharyngeal muscle" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#ccf199;">pm8</span></span></a>|
    |**<span style="color:#66cc99;">pobL</span>** |1 | 0 | <a href="../pobL" title="Posterior oblique (male specific)" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#66cc99;">pobL</span></span></a>|
    |**<span style="color:#66cc99;">pobR</span>** |1 | 0 | <a href="../pobR" title="Posterior oblique (male specific)" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#66cc99;">pobR</span></span></a>|
    |**<span style="color:#999933;">polL</span>** |1 | 0 | <a href="../polL" title="Posterior outer longitudinal muscle (male specific)" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#999933;">polL</span></span></a>|
    |**<span style="color:#999933;">polR</span>** |1 | 0 | <a href="../polR" title="Posterior outer longitudinal muscle (male specific)" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#999933;">polR</span></span></a>|
    |**<span style="color:#99cc00;">um1AL</span>** |1 | 0 | <a href="../um1AL" title="Uterine muscle" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#99cc00;">um1AL</span></span></a>|
    |**<span style="color:#99cc00;">um1AR</span>** |1 | 0 | <a href="../um1AR" title="Uterine muscle" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#99cc00;">um1AR</span></span></a>|
    |**<span style="color:#99cc00;">um1PL</span>** |1 | 0 | <a href="../um1PL" title="Uterine muscle" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#99cc00;">um1PL</span></span></a>|
    |**<span style="color:#99cc00;">um1PR</span>** |1 | 0 | <a href="../um1PR" title="Uterine muscle" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#99cc00;">um1PR</span></span></a>|
    |**<span style="color:#99cc00;">um2AL</span>** |1 | 0 | <a href="../um2AL" title="Uterine muscle" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#99cc00;">um2AL</span></span></a>|
    |**<span style="color:#99cc00;">um2AR</span>** |1 | 0 | <a href="../um2AR" title="Uterine muscle" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#99cc00;">um2AR</span></span></a>|
    |**<span style="color:#99cc00;">um2PL</span>** |1 | 0 | <a href="../um2PL" title="Uterine muscle" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#99cc00;">um2PL</span></span></a>|
    |**<span style="color:#99cc00;">um2PR</span>** |1 | 0 | <a href="../um2PR" title="Uterine muscle" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#99cc00;">um2PR</span></span></a>|
    |**<span style="color:#99cc66;">vm1AL</span>** |1 | 0 | <a href="../vm1AL" title="Vulval muscle" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#99cc66;">vm1AL</span></span></a>|
    |**<span style="color:#99cc66;">vm1AR</span>** |1 | 0 | <a href="../vm1AR" title="Vulval muscle" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#99cc66;">vm1AR</span></span></a>|
    |**<span style="color:#99cc66;">vm1PL</span>** |1 | 0 | <a href="../vm1PL" title="Vulval muscle" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#99cc66;">vm1PL</span></span></a>|
    |**<span style="color:#99cc66;">vm1PR</span>** |1 | 0 | <a href="../vm1PR" title="Vulval muscle" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#99cc66;">vm1PR</span></span></a>|
    |**<span style="color:#99cc66;">vm2AL</span>** |1 | 0 | <a href="../vm2AL" title="Vulval muscle" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#99cc66;">vm2AL</span></span></a>|
    |**<span style="color:#99cc66;">vm2AR</span>** |1 | 0 | <a href="../vm2AR" title="Vulval muscle" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#99cc66;">vm2AR</span></span></a>|
    |**<span style="color:#99cc66;">vm2PL</span>** |1 | 0 | <a href="../vm2PL" title="Vulval muscle" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#99cc66;">vm2PL</span></span></a>|
    |**<span style="color:#99cc66;">vm2PR</span>** |1 | 0 | <a href="../vm2PR" title="Vulval muscle" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#99cc66;">vm2PR</span></span></a>|
    |**<span style="color:#99ff99;">vspL</span>** |1 | 0 | <a href="../vspL" title="Ventral spicule protractor (male specific)" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#99ff99;">vspL</span></span></a>|
    |**<span style="color:#99ff99;">vspR</span>** |1 | 0 | <a href="../vspR" title="Ventral spicule protractor (male specific)" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#99ff99;">vspR</span></span></a>|
    |**<span style="color:#669966;">vsrL</span>** |1 | 0 | <a href="../vsrL" title="Ventral spicule retractor (male specific)" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#669966;">vsrL</span></span></a>|
    |**<span style="color:#669966;">vsrR</span>** |1 | 0 | <a href="../vsrR" title="Ventral spicule retractor (male specific)" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#669966;">vsrR</span></span></a>|
    |**<span style="color:#339999;">CEPshDL</span>** |1 | 0 | <a href="../CEPshDL" title="Sheath cell other than amphid sheath and phasmid" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#339999;">CEPshDL</span></span></a>|
    |**<span style="color:#339999;">CEPshDR</span>** |1 | 0 | <a href="../CEPshDR" title="Sheath cell other than amphid sheath and phasmid" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#339999;">CEPshDR</span></span></a>|
    |**<span style="color:#339999;">CEPshVL</span>** |1 | 0 | <a href="../CEPshVL" title="Sheath cell other than amphid sheath and phasmid" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#339999;">CEPshVL</span></span></a>|
    |**<span style="color:#339999;">CEPshVR</span>** |1 | 0 | <a href="../CEPshVR" title="Sheath cell other than amphid sheath and phasmid" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#339999;">CEPshVR</span></span></a>|
    |**<span style="color:#cc9900;">GLRDL</span>** |1 | 0 | <a href="../GLRDL" title="GLR cell" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#cc9900;">GLRDL</span></span></a>|
    |**<span style="color:#cc9900;">GLRDR</span>** |1 | 0 | <a href="../GLRDR" title="GLR cell" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#cc9900;">GLRDR</span></span></a>|
    |**<span style="color:#cc9900;">GLRL</span>** |1 | 0 | <a href="../GLRL" title="GLR cell" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#cc9900;">GLRL</span></span></a>|
    |**<span style="color:#cc9900;">GLRR</span>** |1 | 0 | <a href="../GLRR" title="GLR cell" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#cc9900;">GLRR</span></span></a>|
    |**<span style="color:#cc9900;">GLRVL</span>** |1 | 0 | <a href="../GLRVL" title="GLR cell" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#cc9900;">GLRVL</span></span></a>|
    |**<span style="color:#cc9900;">GLRVR</span>** |1 | 0 | <a href="../GLRVR" title="GLR cell" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#cc9900;">GLRVR</span></span></a>|
    |**<span style="color:#006666;">R1shL</span>** |1 | 0 | <a href="../R1shL" title="Male ray structural cell" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#006666;">R1shL</span></span></a>|
    |**<span style="color:#006666;">R1shR</span>** |1 | 0 | <a href="../R1shR" title="Male ray structural cell" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#006666;">R1shR</span></span></a>|
    |**<span style="color:#006666;">R1stL</span>** |1 | 0 | <a href="../R1stL" title="Male ray structural cell" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#006666;">R1stL</span></span></a>|
    |**<span style="color:#006666;">R1stR</span>** |1 | 0 | <a href="../R1stR" title="Male ray structural cell" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#006666;">R1stR</span></span></a>|
    |**<span style="color:#006666;">R2shL</span>** |1 | 0 | <a href="../R2shL" title="Male ray structural cell" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#006666;">R2shL</span></span></a>|
    |**<span style="color:#006666;">R2shR</span>** |1 | 0 | <a href="../R2shR" title="Male ray structural cell" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#006666;">R2shR</span></span></a>|
    |**<span style="color:#006666;">R2stL</span>** |1 | 0 | <a href="../R2stL" title="Male ray structural cell" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#006666;">R2stL</span></span></a>|
    |**<span style="color:#006666;">R2stR</span>** |1 | 0 | <a href="../R2stR" title="Male ray structural cell" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#006666;">R2stR</span></span></a>|
    |**<span style="color:#006666;">R3shL</span>** |1 | 0 | <a href="../R3shL" title="Male ray structural cell" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#006666;">R3shL</span></span></a>|
    |**<span style="color:#006666;">R3shR</span>** |1 | 0 | <a href="../R3shR" title="Male ray structural cell" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#006666;">R3shR</span></span></a>|
    |**<span style="color:#006666;">R3stL</span>** |1 | 0 | <a href="../R3stL" title="Male ray structural cell" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#006666;">R3stL</span></span></a>|
    |**<span style="color:#006666;">R3stR</span>** |1 | 0 | <a href="../R3stR" title="Male ray structural cell" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#006666;">R3stR</span></span></a>|
    |**<span style="color:#006666;">R4shL</span>** |1 | 0 | <a href="../R4shL" title="Male ray structural cell" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#006666;">R4shL</span></span></a>|
    |**<span style="color:#006666;">R4shR</span>** |1 | 0 | <a href="../R4shR" title="Male ray structural cell" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#006666;">R4shR</span></span></a>|
    |**<span style="color:#006666;">R4stL</span>** |1 | 0 | <a href="../R4stL" title="Male ray structural cell" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#006666;">R4stL</span></span></a>|
    |**<span style="color:#006666;">R4stR</span>** |1 | 0 | <a href="../R4stR" title="Male ray structural cell" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#006666;">R4stR</span></span></a>|
    |**<span style="color:#006666;">R5shL</span>** |1 | 0 | <a href="../R5shL" title="Male ray structural cell" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#006666;">R5shL</span></span></a>|
    |**<span style="color:#006666;">R5shR</span>** |1 | 0 | <a href="../R5shR" title="Male ray structural cell" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#006666;">R5shR</span></span></a>|
    |**<span style="color:#006666;">R5stL</span>** |1 | 0 | <a href="../R5stL" title="Male ray structural cell" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#006666;">R5stL</span></span></a>|
    |**<span style="color:#006666;">R5stR</span>** |1 | 0 | <a href="../R5stR" title="Male ray structural cell" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#006666;">R5stR</span></span></a>|
    |**<span style="color:#006666;">R6shL</span>** |1 | 0 | <a href="../R6shL" title="Male ray structural cell" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#006666;">R6shL</span></span></a>|
    |**<span style="color:#006666;">R6shR</span>** |1 | 0 | <a href="../R6shR" title="Male ray structural cell" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#006666;">R6shR</span></span></a>|
    |**<span style="color:#006666;">R6stL</span>** |1 | 0 | <a href="../R6stL" title="Male ray structural cell" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#006666;">R6stL</span></span></a>|
    |**<span style="color:#006666;">R6stR</span>** |1 | 0 | <a href="../R6stR" title="Male ray structural cell" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#006666;">R6stR</span></span></a>|
    |**<span style="color:#006666;">R7shL</span>** |1 | 0 | <a href="../R7shL" title="Male ray structural cell" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#006666;">R7shL</span></span></a>|
    |**<span style="color:#006666;">R7shR</span>** |1 | 0 | <a href="../R7shR" title="Male ray structural cell" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#006666;">R7shR</span></span></a>|
    |**<span style="color:#006666;">R7stL</span>** |1 | 0 | <a href="../R7stL" title="Male ray structural cell" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#006666;">R7stL</span></span></a>|
    |**<span style="color:#006666;">R7stR</span>** |1 | 0 | <a href="../R7stR" title="Male ray structural cell" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#006666;">R7stR</span></span></a>|
    |**<span style="color:#006666;">R8shL</span>** |1 | 0 | <a href="../R8shL" title="Male ray structural cell" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#006666;">R8shL</span></span></a>|
    |**<span style="color:#006666;">R8shR</span>** |1 | 0 | <a href="../R8shR" title="Male ray structural cell" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#006666;">R8shR</span></span></a>|
    |**<span style="color:#006666;">R8stL</span>** |1 | 0 | <a href="../R8stL" title="Male ray structural cell" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#006666;">R8stL</span></span></a>|
    |**<span style="color:#006666;">R8stR</span>** |1 | 0 | <a href="../R8stR" title="Male ray structural cell" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#006666;">R8stR</span></span></a>|
    |**<span style="color:#006666;">R9shL</span>** |1 | 0 | <a href="../R9shL" title="Male ray structural cell" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#006666;">R9shL</span></span></a>|
    |**<span style="color:#006666;">R9shR</span>** |1 | 0 | <a href="../R9shR" title="Male ray structural cell" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#006666;">R9shR</span></span></a>|
    |**<span style="color:#006666;">R9stL</span>** |1 | 0 | <a href="../R9stL" title="Male ray structural cell" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#006666;">R9stL</span></span></a>|
    |**<span style="color:#006666;">R9stR</span>** |1 | 0 | <a href="../R9stR" title="Male ray structural cell" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#006666;">R9stR</span></span></a>|
    |**<span style="color:#ff9900;">bm</span>** |1 | 0 | <a href="../bm" title="Pharyngeal basement membrane" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#ff9900;">bm</span></span></a>|
    |**<span style="color:#996699;">e2D</span>** |1 | 0 | <a href="../e2D" title="Pharyngeal epithelium" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#996699;">e2D</span></span></a>|
    |**<span style="color:#996699;">e2DL</span>** |1 | 0 | <a href="../e2DL" title="Pharyngeal epithelium" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#996699;">e2DL</span></span></a>|
    |**<span style="color:#996699;">e2DR</span>** |1 | 0 | <a href="../e2DR" title="Pharyngeal epithelium" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#996699;">e2DR</span></span></a>|
    |**<span style="color:#996699;">e2V</span>** |1 | 0 | <a href="../e2V" title="Pharyngeal epithelium" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#996699;">e2V</span></span></a>|
    |**<span style="color:#996699;">e2VL</span>** |1 | 0 | <a href="../e2VL" title="Pharyngeal epithelium" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#996699;">e2VL</span></span></a>|
    |**<span style="color:#996699;">e2VR</span>** |1 | 0 | <a href="../e2VR" title="Pharyngeal epithelium" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#996699;">e2VR</span></span></a>|
    |**<span style="color:#996699;">e3D</span>** |1 | 0 | <a href="../e3D" title="Pharyngeal epithelium" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#996699;">e3D</span></span></a>|
    |**<span style="color:#996699;">e3VL</span>** |1 | 0 | <a href="../e3VL" title="Pharyngeal epithelium" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#996699;">e3VL</span></span></a>|
    |**<span style="color:#996699;">e3VR</span>** |1 | 0 | <a href="../e3VR" title="Pharyngeal epithelium" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#996699;">e3VR</span></span></a>|
    |**<span style="color:#cc3366;">exc_cell</span>** |1 | 0 | <a href="../exc_cell" title="Excretory cell" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#cc3366;">exc_cell</span></span></a>|
    |**<span style="color:#9999cc;">exc_gl</span>** |1 | 0 | <a href="../exc_gl" title="Excretory gland" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#9999cc;">exc_gl</span></span></a>|
    |**<span style="color:#996699;">g1AL</span>** |1 | 0 | <a href="../g1AL" title="Pharyngeal glial cell" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#996699;">g1AL</span></span></a>|
    |**<span style="color:#996699;">g1AR</span>** |1 | 0 | <a href="../g1AR" title="Pharyngeal glial cell" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#996699;">g1AR</span></span></a>|
    |**<span style="color:#996699;">g1P</span>** |1 | 0 | <a href="../g1P" title="Pharyngeal glial cell" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#996699;">g1P</span></span></a>|
    |**<span style="color:#996699;">g1p</span>** |1 | 0 | <a href="../g1p" title="Pharyngeal glial cell" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#996699;">g1p</span></span></a>|
    |**<span style="color:#996699;">g2L</span>** |1 | 0 | <a href="../g2L" title="Pharyngeal glial cell" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#996699;">g2L</span></span></a>|
    |**<span style="color:#996699;">g2R</span>** |1 | 0 | <a href="../g2R" title="Pharyngeal glial cell" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#996699;">g2R</span></span></a>|
    |**<span style="color:#66cccc;">gonad</span>** |1 | 0 | <a href="../gonad" title="Gonad (male specific)" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#66cccc;">gonad</span></span></a>|
    |**<span style="color:#ff6633;">hmc</span>** |1 | 0 | <a href="../hmc" title="Head mesodermal cell" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#ff6633;">hmc</span></span></a>|
    |**<span style="color:#dcc3ac;">hyp</span>** |1 | 0 | <a href="../hyp" title="Hypodermis" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#dcc3ac;">hyp</span></span></a>|
    |**<span style="color:#ffccff;">int</span>** |1 | 0 | <a href="../int" title="Intestine" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#ffccff;">int</span></span></a>|
    |**<span style="color:#cc33cc;">mc1DL</span>** |1 | 0 | <a href="../mc1DL" title="Marginal cell of the pharynx" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#cc33cc;">mc1DL</span></span></a>|
    |**<span style="color:#cc33cc;">mc1DR</span>** |1 | 0 | <a href="../mc1DR" title="Marginal cell of the pharynx" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#cc33cc;">mc1DR</span></span></a>|
    |**<span style="color:#cc33cc;">mc1V</span>** |1 | 0 | <a href="../mc1V" title="Marginal cell of the pharynx" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#cc33cc;">mc1V</span></span></a>|
    |**<span style="color:#cc33cc;">mc2DL</span>** |1 | 0 | <a href="../mc2DL" title="Marginal cell of the pharynx" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#cc33cc;">mc2DL</span></span></a>|
    |**<span style="color:#cc33cc;">mc2DR</span>** |1 | 0 | <a href="../mc2DR" title="Marginal cell of the pharynx" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#cc33cc;">mc2DR</span></span></a>|
    |**<span style="color:#cc33cc;">mc2V</span>** |1 | 0 | <a href="../mc2V" title="Marginal cell of the pharynx" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#cc33cc;">mc2V</span></span></a>|
    |**<span style="color:#cc33cc;">mc3DL</span>** |1 | 0 | <a href="../mc3DL" title="Marginal cell of the pharynx" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#cc33cc;">mc3DL</span></span></a>|
    |**<span style="color:#cc33cc;">mc3DR</span>** |1 | 0 | <a href="../mc3DR" title="Marginal cell of the pharynx" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#cc33cc;">mc3DR</span></span></a>|
    |**<span style="color:#cc33cc;">mc3V</span>** |1 | 0 | <a href="../mc3V" title="Marginal cell of the pharynx" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#cc33cc;">mc3V</span></span></a>|
    |**<span style="color:#996666;">proctodeum</span>** |1 | 0 | <a href="../proctodeum" title="Proctodeum (male specific)" style="text-decoration:none;"><span style="text-decoration: line-through;"><span style="color:#996666;">proctodeum</span></span></a>|
    


### Neurons (herm) (21)
<details open><summary>Full list of Neurons (hermaphrodite only) in this dataset</summary>
<a href="../ASHR" title="Sensory neuron (amphid, nociceptive)" style="text-decoration:none;"><span style="color:#ff66cc;">ASHR</span></a>
 | <a href="../ASKR" title="Sensory neuron (amphid)" style="text-decoration:none;"><span style="color:#ff66cc;">ASKR</span></a>
 | <a href="../AVBL" title="Layer 1 interneuron" style="text-decoration:none;"><span style="color:#ff3300;">AVBL</span></a>
 | <a href="../AVBR" title="Layer 1 interneuron" style="text-decoration:none;"><span style="color:#ff3300;">AVBR</span></a>
 | <a href="../AWBR" title="Sensory neuron (amphid)" style="text-decoration:none;"><span style="color:#ff66cc;">AWBR</span></a>
 | <a href="../DB4" title="Ventral cord motor neuron" style="text-decoration:none;"><span style="color:#9966cc;">DB4</span></a>
 | <a href="../DD4" title="Ventral cord motor neuron" style="text-decoration:none;"><span style="color:#9966cc;">DD4</span></a>
 | <a href="../DD5" title="Ventral cord motor neuron" style="text-decoration:none;"><span style="color:#9966cc;">DD5</span></a>
 | <a href="../DVA" title="Sensory neuron (mechanosensory)" style="text-decoration:none;"><span style="color:#ff66cc;">DVA</span></a>
 | <a href="../I5" title="Pharyngeal interneuron" style="text-decoration:none;"><span style="color:#ff3300;">I5</span></a>
 | <a href="../M1" title="Pharyngeal motor neuron" style="text-decoration:none;"><span style="color:#9966cc;">M1</span></a>
 | <a href="../M4" title="Pharyngeal motor neuron" style="text-decoration:none;"><span style="color:#9966cc;">M4</span></a>
 | <a href="../PVCL" title="Layer 1 interneuron" style="text-decoration:none;"><span style="color:#ff3300;">PVCL</span></a>
 | <a href="../PVCR" title="Layer 1 interneuron" style="text-decoration:none;"><span style="color:#ff3300;">PVCR</span></a>
 | <a href="../RMGR" title="Layer 2 interneuron" style="text-decoration:none;"><span style="color:#ff3300;">RMGR</span></a>
 | <a href="../VA3" title="Ventral cord motor neuron" style="text-decoration:none;"><span style="color:#9966cc;">VA3</span></a>
 | <a href="../VA6" title="Ventral cord motor neuron" style="text-decoration:none;"><span style="color:#9966cc;">VA6</span></a>
 | <a href="../VB2" title="Ventral cord motor neuron" style="text-decoration:none;"><span style="color:#9966cc;">VB2</span></a>
 | <a href="../VB6" title="Ventral cord motor neuron" style="text-decoration:none;"><span style="color:#9966cc;">VB6</span></a>
 | <a href="../VD3" title="Ventral cord motor neuron" style="text-decoration:none;"><span style="color:#9966cc;">VD3</span></a>
 | <a href="../VD6" title="Ventral cord motor neuron" style="text-decoration:none;"><span style="color:#9966cc;">VD6</span></a>

</details>

### Missing neurons (281)
<details open><summary>Full list of Missing neurons (known hermaphrodite neurons not present)</summary>
<a href="../ADAL" title="Layer 3 interneuron" style="text-decoration:none;"><span style="color:#ff3300;">ADAL</span></a>
 | <a href="../ADAR" title="Layer 3 interneuron" style="text-decoration:none;"><span style="color:#ff3300;">ADAR</span></a>
 | <a href="../ADEL" title="Sensory neuron (mechanosensory)" style="text-decoration:none;"><span style="color:#ff66cc;">ADEL</span></a>
 | <a href="../ADER" title="Sensory neuron (mechanosensory)" style="text-decoration:none;"><span style="color:#ff66cc;">ADER</span></a>
 | <a href="../ADFL" title="Sensory neuron (amphid)" style="text-decoration:none;"><span style="color:#ff66cc;">ADFL</span></a>
 | <a href="../ADFR" title="Sensory neuron (amphid)" style="text-decoration:none;"><span style="color:#ff66cc;">ADFR</span></a>
 | <a href="../ADLL" title="Sensory neuron (amphid, nociceptive)" style="text-decoration:none;"><span style="color:#ff66cc;">ADLL</span></a>
 | <a href="../ADLR" title="Sensory neuron (amphid, nociceptive)" style="text-decoration:none;"><span style="color:#ff66cc;">ADLR</span></a>
 | <a href="../AFDL" title="Sensory neuron (amphid)" style="text-decoration:none;"><span style="color:#ff66cc;">AFDL</span></a>
 | <a href="../AFDR" title="Sensory neuron (amphid)" style="text-decoration:none;"><span style="color:#ff66cc;">AFDR</span></a>
 | <a href="../AIAL" title="Layer 3 interneuron" style="text-decoration:none;"><span style="color:#ff3300;">AIAL</span></a>
 | <a href="../AIAR" title="Layer 3 interneuron" style="text-decoration:none;"><span style="color:#ff3300;">AIAR</span></a>
 | <a href="../AIBL" title="Layer 2 interneuron" style="text-decoration:none;"><span style="color:#ff3300;">AIBL</span></a>
 | <a href="../AIBR" title="Layer 2 interneuron" style="text-decoration:none;"><span style="color:#ff3300;">AIBR</span></a>
 | <a href="../AIML" title="Category 4 interneuron" style="text-decoration:none;"><span style="color:#ff3300;">AIML</span></a>
 | <a href="../AIMR" title="Category 4 interneuron" style="text-decoration:none;"><span style="color:#ff3300;">AIMR</span></a>
 | <a href="../AINL" title="Category 4 interneuron" style="text-decoration:none;"><span style="color:#ff3300;">AINL</span></a>
 | <a href="../AINR" title="Category 4 interneuron" style="text-decoration:none;"><span style="color:#ff3300;">AINR</span></a>
 | <a href="../AIYL" title="Layer 3 interneuron" style="text-decoration:none;"><span style="color:#ff3300;">AIYL</span></a>
 | <a href="../AIYR" title="Layer 3 interneuron" style="text-decoration:none;"><span style="color:#ff3300;">AIYR</span></a>
 | <a href="../AIZL" title="Layer 3 interneuron" style="text-decoration:none;"><span style="color:#ff3300;">AIZL</span></a>
 | <a href="../AIZR" title="Layer 3 interneuron" style="text-decoration:none;"><span style="color:#ff3300;">AIZR</span></a>
 | <a href="../ALA" title="Layer 3 interneuron" style="text-decoration:none;"><span style="color:#ff3300;">ALA</span></a>
 | <a href="../ALML" title="Sensory neuron (mechanosensory)" style="text-decoration:none;"><span style="color:#ff66cc;">ALML</span></a>
 | <a href="../ALMR" title="Sensory neuron (mechanosensory)" style="text-decoration:none;"><span style="color:#ff66cc;">ALMR</span></a>
 | <a href="../ALNL" title="Sensory neuron (touch)" style="text-decoration:none;"><span style="color:#ff66cc;">ALNL</span></a>
 | <a href="../ALNR" title="Sensory neuron (touch)" style="text-decoration:none;"><span style="color:#ff66cc;">ALNR</span></a>
 | <a href="../AQR" title="Sensory neuron (touch)" style="text-decoration:none;"><span style="color:#ff66cc;">AQR</span></a>
 | <a href="../AS1" title="Ventral cord motor neuron" style="text-decoration:none;"><span style="color:#9966cc;">AS1</span></a>
 | <a href="../AS10" title="Ventral cord motor neuron" style="text-decoration:none;"><span style="color:#9966cc;">AS10</span></a>
 | <a href="../AS11" title="Ventral cord motor neuron" style="text-decoration:none;"><span style="color:#9966cc;">AS11</span></a>
 | <a href="../AS2" title="Ventral cord motor neuron" style="text-decoration:none;"><span style="color:#9966cc;">AS2</span></a>
 | <a href="../AS3" title="Ventral cord motor neuron" style="text-decoration:none;"><span style="color:#9966cc;">AS3</span></a>
 | <a href="../AS4" title="Ventral cord motor neuron" style="text-decoration:none;"><span style="color:#9966cc;">AS4</span></a>
 | <a href="../AS5" title="Ventral cord motor neuron" style="text-decoration:none;"><span style="color:#9966cc;">AS5</span></a>
 | <a href="../AS6" title="Ventral cord motor neuron" style="text-decoration:none;"><span style="color:#9966cc;">AS6</span></a>
 | <a href="../AS7" title="Ventral cord motor neuron" style="text-decoration:none;"><span style="color:#9966cc;">AS7</span></a>
 | <a href="../AS8" title="Ventral cord motor neuron" style="text-decoration:none;"><span style="color:#9966cc;">AS8</span></a>
 | <a href="../AS9" title="Ventral cord motor neuron" style="text-decoration:none;"><span style="color:#9966cc;">AS9</span></a>
 | <a href="../ASEL" title="Sensory neuron (amphid)" style="text-decoration:none;"><span style="color:#ff66cc;">ASEL</span></a>
 | <a href="../ASER" title="Sensory neuron (amphid)" style="text-decoration:none;"><span style="color:#ff66cc;">ASER</span></a>
 | <a href="../ASGL" title="Sensory neuron (amphid)" style="text-decoration:none;"><span style="color:#ff66cc;">ASGL</span></a>
 | <a href="../ASGR" title="Sensory neuron (amphid)" style="text-decoration:none;"><span style="color:#ff66cc;">ASGR</span></a>
 | <a href="../ASHL" title="Sensory neuron (amphid, nociceptive)" style="text-decoration:none;"><span style="color:#ff66cc;">ASHL</span></a>
 | <a href="../ASIL" title="Sensory neuron (amphid)" style="text-decoration:none;"><span style="color:#ff66cc;">ASIL</span></a>
 | <a href="../ASIR" title="Sensory neuron (amphid)" style="text-decoration:none;"><span style="color:#ff66cc;">ASIR</span></a>
 | <a href="../ASJL" title="Sensory neuron (amphid)" style="text-decoration:none;"><span style="color:#ff66cc;">ASJL</span></a>
 | <a href="../ASJR" title="Sensory neuron (amphid)" style="text-decoration:none;"><span style="color:#ff66cc;">ASJR</span></a>
 | <a href="../ASKL" title="Sensory neuron (amphid)" style="text-decoration:none;"><span style="color:#ff66cc;">ASKL</span></a>
 | <a href="../AUAL" title="Layer 3 interneuron" style="text-decoration:none;"><span style="color:#ff3300;">AUAL</span></a>
 | <a href="../AUAR" title="Layer 3 interneuron" style="text-decoration:none;"><span style="color:#ff3300;">AUAR</span></a>
 | <a href="../AVAL" title="Layer 1 interneuron" style="text-decoration:none;"><span style="color:#ff3300;">AVAL</span></a>
 | <a href="../AVAR" title="Layer 1 interneuron" style="text-decoration:none;"><span style="color:#ff3300;">AVAR</span></a>
 | <a href="../AVDL" title="Layer 2 interneuron" style="text-decoration:none;"><span style="color:#ff3300;">AVDL</span></a>
 | <a href="../AVDR" title="Layer 2 interneuron" style="text-decoration:none;"><span style="color:#ff3300;">AVDR</span></a>
 | <a href="../AVEL" title="Layer 1 interneuron" style="text-decoration:none;"><span style="color:#ff3300;">AVEL</span></a>
 | <a href="../AVER" title="Layer 1 interneuron" style="text-decoration:none;"><span style="color:#ff3300;">AVER</span></a>
 | <a href="../AVFL" title="Layer 3 interneuron" style="text-decoration:none;"><span style="color:#ff3300;">AVFL</span></a>
 | <a href="../AVFR" title="Layer 3 interneuron" style="text-decoration:none;"><span style="color:#ff3300;">AVFR</span></a>
 | <a href="../AVG" title="Layer 3 interneuron" style="text-decoration:none;"><span style="color:#ff3300;">AVG</span></a>
 | <a href="../AVHL" title="Layer 3 interneuron" style="text-decoration:none;"><span style="color:#ff3300;">AVHL</span></a>
 | <a href="../AVHR" title="Layer 3 interneuron" style="text-decoration:none;"><span style="color:#ff3300;">AVHR</span></a>
 | <a href="../AVJL" title="Layer 2 interneuron" style="text-decoration:none;"><span style="color:#ff3300;">AVJL</span></a>
 | <a href="../AVJR" title="Layer 2 interneuron" style="text-decoration:none;"><span style="color:#ff3300;">AVJR</span></a>
 | <a href="../AVKL" title="Layer 2 interneuron" style="text-decoration:none;"><span style="color:#ff3300;">AVKL</span></a>
 | <a href="../AVKR" title="Layer 2 interneuron" style="text-decoration:none;"><span style="color:#ff3300;">AVKR</span></a>
 | <a href="../AVL" title="Layer 2 interneuron" style="text-decoration:none;"><span style="color:#ff3300;">AVL</span></a>
 | <a href="../AVM" title="Sensory neuron (mechanosensory)" style="text-decoration:none;"><span style="color:#ff66cc;">AVM</span></a>
 | <a href="../AWAL" title="Sensory neuron (amphid)" style="text-decoration:none;"><span style="color:#ff66cc;">AWAL</span></a>
 | <a href="../AWAR" title="Sensory neuron (amphid)" style="text-decoration:none;"><span style="color:#ff66cc;">AWAR</span></a>
 | <a href="../AWBL" title="Sensory neuron (amphid)" style="text-decoration:none;"><span style="color:#ff66cc;">AWBL</span></a>
 | <a href="../AWCL" title="Sensory neuron (amphid)" style="text-decoration:none;"><span style="color:#ff66cc;">AWCL</span></a>
 | <a href="../AWCR" title="Sensory neuron (amphid)" style="text-decoration:none;"><span style="color:#ff66cc;">AWCR</span></a>
 | <a href="../BAGL" title="Sensory neuron (O2, CO2, social signals, touch)" style="text-decoration:none;"><span style="color:#ff66cc;">BAGL</span></a>
 | <a href="../BAGR" title="Sensory neuron (O2, CO2, social signals, touch)" style="text-decoration:none;"><span style="color:#ff66cc;">BAGR</span></a>
 | <a href="../BDUL" title="Layer 3 interneuron" style="text-decoration:none;"><span style="color:#ff3300;">BDUL</span></a>
 | <a href="../BDUR" title="Layer 3 interneuron" style="text-decoration:none;"><span style="color:#ff3300;">BDUR</span></a>
 | <a href="../CANL" title="Canal neuron" style="text-decoration:none;"><span style="color:#990033;">CANL</span></a>
 | <a href="../CANR" title="Canal neuron" style="text-decoration:none;"><span style="color:#990033;">CANR</span></a>
 | <a href="../CEPDL" title="Sensory neuron (cephalic)" style="text-decoration:none;"><span style="color:#ff66cc;">CEPDL</span></a>
 | <a href="../CEPDR" title="Sensory neuron (cephalic)" style="text-decoration:none;"><span style="color:#ff66cc;">CEPDR</span></a>
 | <a href="../CEPVL" title="Sensory neuron (cephalic)" style="text-decoration:none;"><span style="color:#ff66cc;">CEPVL</span></a>
 | <a href="../CEPVR" title="Sensory neuron (cephalic)" style="text-decoration:none;"><span style="color:#ff66cc;">CEPVR</span></a>
 | <a href="../DA1" title="Ventral cord motor neuron" style="text-decoration:none;"><span style="color:#9966cc;">DA1</span></a>
 | <a href="../DA2" title="Ventral cord motor neuron" style="text-decoration:none;"><span style="color:#9966cc;">DA2</span></a>
 | <a href="../DA3" title="Ventral cord motor neuron" style="text-decoration:none;"><span style="color:#9966cc;">DA3</span></a>
 | <a href="../DA4" title="Ventral cord motor neuron" style="text-decoration:none;"><span style="color:#9966cc;">DA4</span></a>
 | <a href="../DA5" title="Ventral cord motor neuron" style="text-decoration:none;"><span style="color:#9966cc;">DA5</span></a>
 | <a href="../DA6" title="Ventral cord motor neuron" style="text-decoration:none;"><span style="color:#9966cc;">DA6</span></a>
 | <a href="../DA7" title="Ventral cord motor neuron" style="text-decoration:none;"><span style="color:#9966cc;">DA7</span></a>
 | <a href="../DA8" title="Ventral cord motor neuron" style="text-decoration:none;"><span style="color:#9966cc;">DA8</span></a>
 | <a href="../DA9" title="Ventral cord motor neuron" style="text-decoration:none;"><span style="color:#9966cc;">DA9</span></a>
 | <a href="../DB1" title="Ventral cord motor neuron" style="text-decoration:none;"><span style="color:#9966cc;">DB1</span></a>
 | <a href="../DB2" title="Ventral cord motor neuron" style="text-decoration:none;"><span style="color:#9966cc;">DB2</span></a>
 | <a href="../DB3" title="Ventral cord motor neuron" style="text-decoration:none;"><span style="color:#9966cc;">DB3</span></a>
 | <a href="../DB5" title="Ventral cord motor neuron" style="text-decoration:none;"><span style="color:#9966cc;">DB5</span></a>
 | <a href="../DB6" title="Ventral cord motor neuron" style="text-decoration:none;"><span style="color:#9966cc;">DB6</span></a>
 | <a href="../DB7" title="Ventral cord motor neuron" style="text-decoration:none;"><span style="color:#9966cc;">DB7</span></a>
 | <a href="../DD1" title="Ventral cord motor neuron" style="text-decoration:none;"><span style="color:#9966cc;">DD1</span></a>
 | <a href="../DD2" title="Ventral cord motor neuron" style="text-decoration:none;"><span style="color:#9966cc;">DD2</span></a>
 | <a href="../DD3" title="Ventral cord motor neuron" style="text-decoration:none;"><span style="color:#9966cc;">DD3</span></a>
 | <a href="../DD6" title="Ventral cord motor neuron" style="text-decoration:none;"><span style="color:#9966cc;">DD6</span></a>
 | <a href="../DVB" title="Layer 3 interneuron" style="text-decoration:none;"><span style="color:#ff3300;">DVB</span></a>
 | <a href="../DVC" title="Layer 2 interneuron" style="text-decoration:none;"><span style="color:#ff3300;">DVC</span></a>
 | <a href="../FLPL" title="Sensory neuron (mechanosensory)" style="text-decoration:none;"><span style="color:#ff66cc;">FLPL</span></a>
 | <a href="../FLPR" title="Sensory neuron (mechanosensory)" style="text-decoration:none;"><span style="color:#ff66cc;">FLPR</span></a>
 | <a href="../HSNL" title="Hermaphrodite specific motor neuron" style="text-decoration:none;"><span style="color:#9966cc;">HSNL</span></a>
 | <a href="../HSNR" title="Hermaphrodite specific motor neuron" style="text-decoration:none;"><span style="color:#9966cc;">HSNR</span></a>
 | <a href="../I1L" title="Pharyngeal interneuron" style="text-decoration:none;"><span style="color:#ff3300;">I1L</span></a>
 | <a href="../I1R" title="Pharyngeal interneuron" style="text-decoration:none;"><span style="color:#ff3300;">I1R</span></a>
 | <a href="../I2L" title="Pharyngeal interneuron" style="text-decoration:none;"><span style="color:#ff3300;">I2L</span></a>
 | <a href="../I2R" title="Pharyngeal interneuron" style="text-decoration:none;"><span style="color:#ff3300;">I2R</span></a>
 | <a href="../I3" title="Pharyngeal interneuron" style="text-decoration:none;"><span style="color:#ff3300;">I3</span></a>
 | <a href="../I4" title="Pharyngeal interneuron" style="text-decoration:none;"><span style="color:#ff3300;">I4</span></a>
 | <a href="../I6" title="Pharyngeal interneuron" style="text-decoration:none;"><span style="color:#ff3300;">I6</span></a>
 | <a href="../IL1DL" title="Sensory neuron (cephalic)" style="text-decoration:none;"><span style="color:#ff66cc;">IL1DL</span></a>
 | <a href="../IL1DR" title="Sensory neuron (cephalic)" style="text-decoration:none;"><span style="color:#ff66cc;">IL1DR</span></a>
 | <a href="../IL1L" title="Sensory neuron (cephalic)" style="text-decoration:none;"><span style="color:#ff66cc;">IL1L</span></a>
 | <a href="../IL1R" title="Sensory neuron (cephalic)" style="text-decoration:none;"><span style="color:#ff66cc;">IL1R</span></a>
 | <a href="../IL1VL" title="Sensory neuron (cephalic)" style="text-decoration:none;"><span style="color:#ff66cc;">IL1VL</span></a>
 | <a href="../IL1VR" title="Sensory neuron (cephalic)" style="text-decoration:none;"><span style="color:#ff66cc;">IL1VR</span></a>
 | <a href="../IL2DL" title="Sensory neuron (cephalic)" style="text-decoration:none;"><span style="color:#ff66cc;">IL2DL</span></a>
 | <a href="../IL2DR" title="Sensory neuron (cephalic)" style="text-decoration:none;"><span style="color:#ff66cc;">IL2DR</span></a>
 | <a href="../IL2L" title="Sensory neuron (cephalic)" style="text-decoration:none;"><span style="color:#ff66cc;">IL2L</span></a>
 | <a href="../IL2R" title="Sensory neuron (cephalic)" style="text-decoration:none;"><span style="color:#ff66cc;">IL2R</span></a>
 | <a href="../IL2VL" title="Sensory neuron (cephalic)" style="text-decoration:none;"><span style="color:#ff66cc;">IL2VL</span></a>
 | <a href="../IL2VR" title="Sensory neuron (cephalic)" style="text-decoration:none;"><span style="color:#ff66cc;">IL2VR</span></a>
 | <a href="../LUAL" title="Layer 3 interneuron" style="text-decoration:none;"><span style="color:#ff3300;">LUAL</span></a>
 | <a href="../LUAR" title="Layer 3 interneuron" style="text-decoration:none;"><span style="color:#ff3300;">LUAR</span></a>
 | <a href="../M2L" title="Pharyngeal motor neuron" style="text-decoration:none;"><span style="color:#9966cc;">M2L</span></a>
 | <a href="../M2R" title="Pharyngeal motor neuron" style="text-decoration:none;"><span style="color:#9966cc;">M2R</span></a>
 | <a href="../M3L" title="Pharyngeal motor neuron" style="text-decoration:none;"><span style="color:#9966cc;">M3L</span></a>
 | <a href="../M3R" title="Pharyngeal motor neuron" style="text-decoration:none;"><span style="color:#9966cc;">M3R</span></a>
 | <a href="../M5" title="Pharyngeal motor neuron" style="text-decoration:none;"><span style="color:#9966cc;">M5</span></a>
 | <a href="../MCL" title="Pharyngeal polymodal neuron" style="text-decoration:none;"><span style="color:#cc0033;">MCL</span></a>
 | <a href="../MCR" title="Pharyngeal polymodal neuron" style="text-decoration:none;"><span style="color:#cc0033;">MCR</span></a>
 | <a href="../MI" title="Pharyngeal polymodal neuron" style="text-decoration:none;"><span style="color:#cc0033;">MI</span></a>
 | <a href="../NSML" title="Pharyngeal polymodal neuron" style="text-decoration:none;"><span style="color:#cc0033;">NSML</span></a>
 | <a href="../NSMR" title="Pharyngeal polymodal neuron" style="text-decoration:none;"><span style="color:#cc0033;">NSMR</span></a>
 | <a href="../OLLL" title="Sensory neuron (cephalic)" style="text-decoration:none;"><span style="color:#ff66cc;">OLLL</span></a>
 | <a href="../OLLR" title="Sensory neuron (cephalic)" style="text-decoration:none;"><span style="color:#ff66cc;">OLLR</span></a>
 | <a href="../OLQDL" title="Sensory neuron (cephalic)" style="text-decoration:none;"><span style="color:#ff66cc;">OLQDL</span></a>
 | <a href="../OLQDR" title="Sensory neuron (cephalic)" style="text-decoration:none;"><span style="color:#ff66cc;">OLQDR</span></a>
 | <a href="../OLQVL" title="Sensory neuron (cephalic)" style="text-decoration:none;"><span style="color:#ff66cc;">OLQVL</span></a>
 | <a href="../OLQVR" title="Sensory neuron (cephalic)" style="text-decoration:none;"><span style="color:#ff66cc;">OLQVR</span></a>
 | <a href="../PDA" title="Ventral cord motor neuron" style="text-decoration:none;"><span style="color:#9966cc;">PDA</span></a>
 | <a href="../PDB" title="Ventral cord motor neuron" style="text-decoration:none;"><span style="color:#9966cc;">PDB</span></a>
 | <a href="../PDEL" title="Sensory neuron (mechanosensory)" style="text-decoration:none;"><span style="color:#ff66cc;">PDEL</span></a>
 | <a href="../PDER" title="Sensory neuron (mechanosensory)" style="text-decoration:none;"><span style="color:#ff66cc;">PDER</span></a>
 | <a href="../PHAL" title="Sensory neuron (phasmid)" style="text-decoration:none;"><span style="color:#ff66cc;">PHAL</span></a>
 | <a href="../PHAR" title="Sensory neuron (phasmid)" style="text-decoration:none;"><span style="color:#ff66cc;">PHAR</span></a>
 | <a href="../PHBL" title="Sensory neuron (phasmid)" style="text-decoration:none;"><span style="color:#ff66cc;">PHBL</span></a>
 | <a href="../PHBR" title="Sensory neuron (phasmid)" style="text-decoration:none;"><span style="color:#ff66cc;">PHBR</span></a>
 | <a href="../PHCL" title="Sensory neuron (phasmid)" style="text-decoration:none;"><span style="color:#ff66cc;">PHCL</span></a>
 | <a href="../PHCR" title="Sensory neuron (phasmid)" style="text-decoration:none;"><span style="color:#ff66cc;">PHCR</span></a>
 | <a href="../PLML" title="Sensory neuron (mechanosensory)" style="text-decoration:none;"><span style="color:#ff66cc;">PLML</span></a>
 | <a href="../PLMR" title="Sensory neuron (mechanosensory)" style="text-decoration:none;"><span style="color:#ff66cc;">PLMR</span></a>
 | <a href="../PLNL" title="Sensory neuron (touch)" style="text-decoration:none;"><span style="color:#ff66cc;">PLNL</span></a>
 | <a href="../PLNR" title="Sensory neuron (touch)" style="text-decoration:none;"><span style="color:#ff66cc;">PLNR</span></a>
 | <a href="../PQR" title="Sensory neuron (touch)" style="text-decoration:none;"><span style="color:#ff66cc;">PQR</span></a>
 | <a href="../PVDL" title="Sensory neuron (mechanosensory)" style="text-decoration:none;"><span style="color:#ff66cc;">PVDL</span></a>
 | <a href="../PVDR" title="Sensory neuron (mechanosensory)" style="text-decoration:none;"><span style="color:#ff66cc;">PVDR</span></a>
 | <a href="../PVM" title="Sensory neuron (mechanosensory)" style="text-decoration:none;"><span style="color:#ff66cc;">PVM</span></a>
 | <a href="../PVNL" title="Layer 3 interneuron" style="text-decoration:none;"><span style="color:#ff3300;">PVNL</span></a>
 | <a href="../PVNR" title="Layer 3 interneuron" style="text-decoration:none;"><span style="color:#ff3300;">PVNR</span></a>
 | <a href="../PVPL" title="Layer 3 interneuron" style="text-decoration:none;"><span style="color:#ff3300;">PVPL</span></a>
 | <a href="../PVPR" title="Layer 3 interneuron" style="text-decoration:none;"><span style="color:#ff3300;">PVPR</span></a>
 | <a href="../PVQL" title="Layer 3 interneuron" style="text-decoration:none;"><span style="color:#ff3300;">PVQL</span></a>
 | <a href="../PVQR" title="Layer 3 interneuron" style="text-decoration:none;"><span style="color:#ff3300;">PVQR</span></a>
 | <a href="../PVR" title="Layer 3 interneuron" style="text-decoration:none;"><span style="color:#ff3300;">PVR</span></a>
 | <a href="../PVT" title="Layer 2 interneuron" style="text-decoration:none;"><span style="color:#ff3300;">PVT</span></a>
 | <a href="../PVWL" title="Layer 2 interneuron" style="text-decoration:none;"><span style="color:#ff3300;">PVWL</span></a>
 | <a href="../PVWR" title="Layer 2 interneuron" style="text-decoration:none;"><span style="color:#ff3300;">PVWR</span></a>
 | <a href="../RIAL" title="Layer 1 interneuron" style="text-decoration:none;"><span style="color:#ff3300;">RIAL</span></a>
 | <a href="../RIAR" title="Layer 1 interneuron" style="text-decoration:none;"><span style="color:#ff3300;">RIAR</span></a>
 | <a href="../RIBL" title="Layer 2 interneuron" style="text-decoration:none;"><span style="color:#ff3300;">RIBL</span></a>
 | <a href="../RIBR" title="Layer 2 interneuron" style="text-decoration:none;"><span style="color:#ff3300;">RIBR</span></a>
 | <a href="../RICL" title="Layer 2 interneuron" style="text-decoration:none;"><span style="color:#ff3300;">RICL</span></a>
 | <a href="../RICR" title="Layer 2 interneuron" style="text-decoration:none;"><span style="color:#ff3300;">RICR</span></a>
 | <a href="../RID" title="Layer 1 interneuron" style="text-decoration:none;"><span style="color:#ff3300;">RID</span></a>
 | <a href="../RIFL" title="Layer 3 interneuron" style="text-decoration:none;"><span style="color:#ff3300;">RIFL</span></a>
 | <a href="../RIFR" title="Layer 3 interneuron" style="text-decoration:none;"><span style="color:#ff3300;">RIFR</span></a>
 | <a href="../RIGL" title="Layer 2 interneuron" style="text-decoration:none;"><span style="color:#ff3300;">RIGL</span></a>
 | <a href="../RIGR" title="Layer 2 interneuron" style="text-decoration:none;"><span style="color:#ff3300;">RIGR</span></a>
 | <a href="../RIH" title="Category 4 interneuron" style="text-decoration:none;"><span style="color:#ff3300;">RIH</span></a>
 | <a href="../RIML" title="Layer 1 interneuron; motorneuron in White et al., 1986" style="text-decoration:none;"><span style="color:#ff3300;">RIML</span></a>
 | <a href="../RIMR" title="Layer 1 interneuron; motorneuron in White et al., 1986" style="text-decoration:none;"><span style="color:#ff3300;">RIMR</span></a>
 | <a href="../RIPL" title="Linker to pharynx" style="text-decoration:none;"><span style="color:#ff3300;">RIPL</span></a>
 | <a href="../RIPR" title="Linker to pharynx" style="text-decoration:none;"><span style="color:#ff3300;">RIPR</span></a>
 | <a href="../RIR" title="Category 4 interneuron" style="text-decoration:none;"><span style="color:#ff3300;">RIR</span></a>
 | <a href="../RIS" title="Layer 3 interneuron" style="text-decoration:none;"><span style="color:#ff3300;">RIS</span></a>
 | <a href="../RIVL" title="Head motor neuron" style="text-decoration:none;"><span style="color:#9966cc;">RIVL</span></a>
 | <a href="../RIVR" title="Head motor neuron" style="text-decoration:none;"><span style="color:#9966cc;">RIVR</span></a>
 | <a href="../RMDDL" title="Head motor neuron" style="text-decoration:none;"><span style="color:#9966cc;">RMDDL</span></a>
 | <a href="../RMDDR" title="Head motor neuron" style="text-decoration:none;"><span style="color:#9966cc;">RMDDR</span></a>
 | <a href="../RMDL" title="Head motor neuron" style="text-decoration:none;"><span style="color:#9966cc;">RMDL</span></a>
 | <a href="../RMDR" title="Head motor neuron" style="text-decoration:none;"><span style="color:#9966cc;">RMDR</span></a>
 | <a href="../RMDVL" title="Head motor neuron" style="text-decoration:none;"><span style="color:#9966cc;">RMDVL</span></a>
 | <a href="../RMDVR" title="Head motor neuron" style="text-decoration:none;"><span style="color:#9966cc;">RMDVR</span></a>
 | <a href="../RMED" title="Head motor neuron" style="text-decoration:none;"><span style="color:#9966cc;">RMED</span></a>
 | <a href="../RMEL" title="Head motor neuron" style="text-decoration:none;"><span style="color:#9966cc;">RMEL</span></a>
 | <a href="../RMER" title="Head motor neuron" style="text-decoration:none;"><span style="color:#9966cc;">RMER</span></a>
 | <a href="../RMEV" title="Head motor neuron" style="text-decoration:none;"><span style="color:#9966cc;">RMEV</span></a>
 | <a href="../RMFL" title="Layer 2 interneuron" style="text-decoration:none;"><span style="color:#ff3300;">RMFL</span></a>
 | <a href="../RMFR" title="Layer 2 interneuron" style="text-decoration:none;"><span style="color:#ff3300;">RMFR</span></a>
 | <a href="../RMGL" title="Layer 2 interneuron" style="text-decoration:none;"><span style="color:#ff3300;">RMGL</span></a>
 | <a href="../RMHL" title="Head motor neuron" style="text-decoration:none;"><span style="color:#9966cc;">RMHL</span></a>
 | <a href="../RMHR" title="Head motor neuron" style="text-decoration:none;"><span style="color:#9966cc;">RMHR</span></a>
 | <a href="../SAADL" title="Layer 2 interneuron" style="text-decoration:none;"><span style="color:#ff3300;">SAADL</span></a>
 | <a href="../SAADR" title="Layer 2 interneuron" style="text-decoration:none;"><span style="color:#ff3300;">SAADR</span></a>
 | <a href="../SAAVL" title="Layer 2 interneuron" style="text-decoration:none;"><span style="color:#ff3300;">SAAVL</span></a>
 | <a href="../SAAVR" title="Layer 2 interneuron" style="text-decoration:none;"><span style="color:#ff3300;">SAAVR</span></a>
 | <a href="../SABD" title="Sublateral motor neuron; interneuron in White et al., 1986" style="text-decoration:none;"><span style="color:#9966cc;">SABD</span></a>
 | <a href="../SABVL" title="Sublateral motor neuron; interneuron in White et al., 1986" style="text-decoration:none;"><span style="color:#9966cc;">SABVL</span></a>
 | <a href="../SABVR" title="Sublateral motor neuron; interneuron in White et al., 1986" style="text-decoration:none;"><span style="color:#9966cc;">SABVR</span></a>
 | <a href="../SDQL" title="Sensory neuron (touch)" style="text-decoration:none;"><span style="color:#ff66cc;">SDQL</span></a>
 | <a href="../SDQR" title="Sensory neuron (touch)" style="text-decoration:none;"><span style="color:#ff66cc;">SDQR</span></a>
 | <a href="../SIADL" title="Sublateral motor neuron; interneuron in White et al., 1986" style="text-decoration:none;"><span style="color:#9966cc;">SIADL</span></a>
 | <a href="../SIADR" title="Sublateral motor neuron; interneuron in White et al., 1986" style="text-decoration:none;"><span style="color:#9966cc;">SIADR</span></a>
 | <a href="../SIAVL" title="Sublateral motor neuron; interneuron in White et al., 1986" style="text-decoration:none;"><span style="color:#9966cc;">SIAVL</span></a>
 | <a href="../SIAVR" title="Sublateral motor neuron; interneuron in White et al., 1986" style="text-decoration:none;"><span style="color:#9966cc;">SIAVR</span></a>
 | <a href="../SIBDL" title="Sublateral motor neuron; interneuron in White et al., 1986" style="text-decoration:none;"><span style="color:#9966cc;">SIBDL</span></a>
 | <a href="../SIBDR" title="Sublateral motor neuron; interneuron in White et al., 1986" style="text-decoration:none;"><span style="color:#9966cc;">SIBDR</span></a>
 | <a href="../SIBVL" title="Sublateral motor neuron; interneuron in White et al., 1986" style="text-decoration:none;"><span style="color:#9966cc;">SIBVL</span></a>
 | <a href="../SIBVR" title="Sublateral motor neuron; interneuron in White et al., 1986" style="text-decoration:none;"><span style="color:#9966cc;">SIBVR</span></a>
 | <a href="../SMBDL" title="Sublateral motor neuron" style="text-decoration:none;"><span style="color:#9966cc;">SMBDL</span></a>
 | <a href="../SMBDR" title="Sublateral motor neuron" style="text-decoration:none;"><span style="color:#9966cc;">SMBDR</span></a>
 | <a href="../SMBVL" title="Sublateral motor neuron" style="text-decoration:none;"><span style="color:#9966cc;">SMBVL</span></a>
 | <a href="../SMBVR" title="Sublateral motor neuron" style="text-decoration:none;"><span style="color:#9966cc;">SMBVR</span></a>
 | <a href="../SMDDL" title="Sublateral motor neuron" style="text-decoration:none;"><span style="color:#9966cc;">SMDDL</span></a>
 | <a href="../SMDDR" title="Sublateral motor neuron" style="text-decoration:none;"><span style="color:#9966cc;">SMDDR</span></a>
 | <a href="../SMDVL" title="Sublateral motor neuron" style="text-decoration:none;"><span style="color:#9966cc;">SMDVL</span></a>
 | <a href="../SMDVR" title="Sublateral motor neuron" style="text-decoration:none;"><span style="color:#9966cc;">SMDVR</span></a>
 | <a href="../URADL" title="Head motor neuron" style="text-decoration:none;"><span style="color:#9966cc;">URADL</span></a>
 | <a href="../URADR" title="Head motor neuron" style="text-decoration:none;"><span style="color:#9966cc;">URADR</span></a>
 | <a href="../URAVL" title="Head motor neuron" style="text-decoration:none;"><span style="color:#9966cc;">URAVL</span></a>
 | <a href="../URAVR" title="Head motor neuron" style="text-decoration:none;"><span style="color:#9966cc;">URAVR</span></a>
 | <a href="../URBL" title="Category 4 interneuron" style="text-decoration:none;"><span style="color:#ff3300;">URBL</span></a>
 | <a href="../URBR" title="Category 4 interneuron" style="text-decoration:none;"><span style="color:#ff3300;">URBR</span></a>
 | <a href="../URXL" title="Sensory neuron (O2, CO2, social signals, touch)" style="text-decoration:none;"><span style="color:#ff66cc;">URXL</span></a>
 | <a href="../URXR" title="Sensory neuron (O2, CO2, social signals, touch)" style="text-decoration:none;"><span style="color:#ff66cc;">URXR</span></a>
 | <a href="../URYDL" title="Sensory neuron (cephalic)" style="text-decoration:none;"><span style="color:#ff66cc;">URYDL</span></a>
 | <a href="../URYDR" title="Sensory neuron (cephalic)" style="text-decoration:none;"><span style="color:#ff66cc;">URYDR</span></a>
 | <a href="../URYVL" title="Sensory neuron (cephalic)" style="text-decoration:none;"><span style="color:#ff66cc;">URYVL</span></a>
 | <a href="../URYVR" title="Sensory neuron (cephalic)" style="text-decoration:none;"><span style="color:#ff66cc;">URYVR</span></a>
 | <a href="../VA1" title="Ventral cord motor neuron" style="text-decoration:none;"><span style="color:#9966cc;">VA1</span></a>
 | <a href="../VA10" title="Ventral cord motor neuron" style="text-decoration:none;"><span style="color:#9966cc;">VA10</span></a>
 | <a href="../VA11" title="Ventral cord motor neuron" style="text-decoration:none;"><span style="color:#9966cc;">VA11</span></a>
 | <a href="../VA12" title="Ventral cord motor neuron" style="text-decoration:none;"><span style="color:#9966cc;">VA12</span></a>
 | <a href="../VA2" title="Ventral cord motor neuron" style="text-decoration:none;"><span style="color:#9966cc;">VA2</span></a>
 | <a href="../VA4" title="Ventral cord motor neuron" style="text-decoration:none;"><span style="color:#9966cc;">VA4</span></a>
 | <a href="../VA5" title="Ventral cord motor neuron" style="text-decoration:none;"><span style="color:#9966cc;">VA5</span></a>
 | <a href="../VA7" title="Ventral cord motor neuron" style="text-decoration:none;"><span style="color:#9966cc;">VA7</span></a>
 | <a href="../VA8" title="Ventral cord motor neuron" style="text-decoration:none;"><span style="color:#9966cc;">VA8</span></a>
 | <a href="../VA9" title="Ventral cord motor neuron" style="text-decoration:none;"><span style="color:#9966cc;">VA9</span></a>
 | <a href="../VB1" title="Ventral cord motor neuron" style="text-decoration:none;"><span style="color:#9966cc;">VB1</span></a>
 | <a href="../VB10" title="Ventral cord motor neuron" style="text-decoration:none;"><span style="color:#9966cc;">VB10</span></a>
 | <a href="../VB11" title="Ventral cord motor neuron" style="text-decoration:none;"><span style="color:#9966cc;">VB11</span></a>
 | <a href="../VB3" title="Ventral cord motor neuron" style="text-decoration:none;"><span style="color:#9966cc;">VB3</span></a>
 | <a href="../VB4" title="Ventral cord motor neuron" style="text-decoration:none;"><span style="color:#9966cc;">VB4</span></a>
 | <a href="../VB5" title="Ventral cord motor neuron" style="text-decoration:none;"><span style="color:#9966cc;">VB5</span></a>
 | <a href="../VB7" title="Ventral cord motor neuron" style="text-decoration:none;"><span style="color:#9966cc;">VB7</span></a>
 | <a href="../VB8" title="Ventral cord motor neuron" style="text-decoration:none;"><span style="color:#9966cc;">VB8</span></a>
 | <a href="../VB9" title="Ventral cord motor neuron" style="text-decoration:none;"><span style="color:#9966cc;">VB9</span></a>
 | <a href="../VC1" title="Hermaphrodite specific motor neuron" style="text-decoration:none;"><span style="color:#9966cc;">VC1</span></a>
 | <a href="../VC2" title="Hermaphrodite specific motor neuron" style="text-decoration:none;"><span style="color:#9966cc;">VC2</span></a>
 | <a href="../VC3" title="Hermaphrodite specific motor neuron" style="text-decoration:none;"><span style="color:#9966cc;">VC3</span></a>
 | <a href="../VC4" title="Hermaphrodite specific motor neuron" style="text-decoration:none;"><span style="color:#9966cc;">VC4</span></a>
 | <a href="../VC5" title="Hermaphrodite specific motor neuron" style="text-decoration:none;"><span style="color:#9966cc;">VC5</span></a>
 | <a href="../VC6" title="Hermaphrodite specific motor neuron" style="text-decoration:none;"><span style="color:#9966cc;">VC6</span></a>
 | <a href="../VD1" title="Ventral cord motor neuron" style="text-decoration:none;"><span style="color:#9966cc;">VD1</span></a>
 | <a href="../VD10" title="Ventral cord motor neuron" style="text-decoration:none;"><span style="color:#9966cc;">VD10</span></a>
 | <a href="../VD11" title="Ventral cord motor neuron" style="text-decoration:none;"><span style="color:#9966cc;">VD11</span></a>
 | <a href="../VD12" title="Ventral cord motor neuron" style="text-decoration:none;"><span style="color:#9966cc;">VD12</span></a>
 | <a href="../VD13" title="Ventral cord motor neuron" style="text-decoration:none;"><span style="color:#9966cc;">VD13</span></a>
 | <a href="../VD2" title="Ventral cord motor neuron" style="text-decoration:none;"><span style="color:#9966cc;">VD2</span></a>
 | <a href="../VD4" title="Ventral cord motor neuron" style="text-decoration:none;"><span style="color:#9966cc;">VD4</span></a>
 | <a href="../VD5" title="Ventral cord motor neuron" style="text-decoration:none;"><span style="color:#9966cc;">VD5</span></a>
 | <a href="../VD7" title="Ventral cord motor neuron" style="text-decoration:none;"><span style="color:#9966cc;">VD7</span></a>
 | <a href="../VD8" title="Ventral cord motor neuron" style="text-decoration:none;"><span style="color:#9966cc;">VD8</span></a>
 | <a href="../VD9" title="Ventral cord motor neuron" style="text-decoration:none;"><span style="color:#9966cc;">VD9</span></a>

</details>

### Muscles (0)

### Other cells (0)
