---
title: "Dataset: Test"
search:
  exclude: true
---


!!! example "Choose Dataset"

    <a href="../Loco3_White_A_data_graph">White_A</a> <a href="../Loco3_White_L4_data_graph">White_L4</a> <a href="../Loco3_White_whole_data_graph">White_whole</a> <a href="../Loco3_Varshney_data_graph">Varshney</a> <a href="../Loco3_Bentley2016_MA_data_graph">Bentley2016_MA</a> <a href="../Loco3_Bentley2016_PEP_data_graph">Bentley2016_PEP</a> <a href="../Loco3_Cook2019Herm_data_graph">Cook2019Herm</a> <a href="../Loco3_Cook2019Male_data_graph">Cook2019Male</a> <a href="../Loco3_Cook2020_data_graph">Cook2020</a> <a href="../Loco3_Brittin2021_data_graph">Brittin2021</a> <a href="../Loco3_Witvliet1_data_graph">Witvliet1</a> <a href="../Loco3_Witvliet2_data_graph">Witvliet2</a> <a href="../Loco3_Witvliet3_data_graph">Witvliet3</a> <a href="../Loco3_Witvliet4_data_graph">Witvliet4</a> <a href="../Loco3_Witvliet5_data_graph">Witvliet5</a> <a href="../Loco3_Witvliet6_data_graph">Witvliet6</a> <a href="../Loco3_Witvliet7_data_graph">Witvliet7</a> <a href="../Loco3_Witvliet8_data_graph">Witvliet8</a> <a href="../Loco3_WormNeuroAtlas_data_graph">WormNeuroAtlas</a> <a href="../Loco3_Randi2023_data_graph">Randi2023</a> <a href="../Loco3_RipollSanchezShortRange_data_graph">RipollSanchezShortRange</a> <a href="../Loco3_RipollSanchezMidRange_data_graph">RipollSanchezMidRange</a> <a href="../Loco3_RipollSanchezLongRange_data_graph">RipollSanchezLongRange</a> <a href="../Loco3_Yim2024_data_graph">Yim2024</a> <a href="../Loco3_Yim2024NonNorm_data_graph">Yim2024NonNorm</a> <a href="../Loco3_Wang2024Herm_data_graph">Wang2024Herm</a> <a href="../Loco3_Wang2024Male_data_graph">Wang2024Male</a> <a href="../Loco3_OpenWormUnified_data_graph">OpenWormUnified</a> <b><a href="../Loco3_Test_data_graph">Test</a></b> <a href="../Loco3_SSData_data_graph">SSData</a> <a href="../Loco3_UpdSSData_data_graph">UpdSSData</a> <a href="../Loco3_UpdSSData2_data_graph">UpdSSData2</a> <a href="../Loco3_GleesonModel_data_graph">GleesonModel</a> <a href="../Loco3_OlivaresModel_data_graph">OlivaresModel</a> 

    <i>Dummy dataset used for testing webpage/graph generation. <b>Do not assume any of these connections are correct!</b>.&nbsp;&nbsp;&nbsp;Python Reader: <a href="../api/cect/TestDataReader">TestDataReader</a></i>


    

!!! abstract inline "Choose Graph type"

    <b><a href="../Loco3_Test_data_graph"> Graph</a></b> - <a href="../Loco3_Test_data"> Matrix</a> - <a href="../Loco3_Test_data_hiveplot"> Hive plot</a> -<a href="../Loco3_Test_data_symmetry"> Symmetry</a> 


!!! tip  "Choose View"

    <a href="../Test_data_graph"> Raw Data</a> - <a href="../Neurons_Test_data_graph"> Neurons</a> - <a href="../Pharynx_Test_data_graph"> Pharynx</a> - <a href="../Social_Test_data_graph"> Social Network</a> - <a href="../Escape_Test_data_graph"> Escape Response Circuit</a> - <a href="../Full1_Test_data_graph"> Cook 2019 Fig 3</a> - <a href="../Loco1_Test_data_graph"> Locomotion 1</a> - <a href="../Loco2_Test_data_graph"> Locomotion 2</a> - <b><a href="../Loco3_Test_data_graph"> Locomotion 3</a></b> - <a href="../PeptidergicHubs_Test_data_graph"> Peptidergic Hubs</a> - <a href="../NonpharyngealH_Test_data_graph"> Nonpharyngeal Neurons (herm)</a> - <a href="../SensorySomaticH_Test_data_graph"> Sensory Neurons (somatic)</a> - <a href="../MotorSomaticH_Test_data_graph"> Motor Neurons (somatic)</a> - <a href="../InterneuronsSomaticH_Test_data_graph"> Interneurons (somatic)</a> - 

    <i>Subset of cells involved in locomotion</i>
=== "Chemical"

    ```{.plotly .no-auto-theme}
    { "file_path": "./assets/Test_Loco3_Chemical_graph.json" }
    ```

=== "Electrical"

    ```{.plotly .no-auto-theme}
    { "file_path": "./assets/Test_Loco3_Electrical_graph.json" }
    ```

=== "Acetylcholine"

    ```{.plotly .no-auto-theme}
    { "file_path": "./assets/Test_Loco3_Acetylcholine_graph.json" }
    ```

=== "GABA"

    ```{.plotly .no-auto-theme}
    { "file_path": "./assets/Test_Loco3_GABA_graph.json" }
    ```

=== "View info"

    **Locomotion 3** (Loco3)
    
    _Subset of cells involved in locomotion_
    
    
    
    | Connection type | Total size | Values present | Nodes with pre connections | Nodes with post connections |
    | --- | --- | --- | --- | --- |
    |**Chemical** | (60, 60) matrix | 7 non-zero entries, avg. weight: 8.714285714285714, sum: 61.0| **<span style="color:#6eb0ab;">DB4</span>**, **<span style="color:#85542b;">VA6</span>**, **<span style="color:#2b665e;">VB6</span>**, **<span style="color:#a6c7e6;">VD3</span>**, **<span style="color:#a6c7e6;">VD6</span>** | **<span style="color:#3d519e;">DD4</span>**, **<span style="color:#85542b;">VA3</span>**, **<span style="color:#85542b;">VA6</span>**, **<span style="color:#2b665e;">VB2</span>**, **<span style="color:#a6c7e6;">VD6</span>** |
    |**Electrical** | (60, 60) matrix | 4 non-zero entries, avg. weight: 3.25, sum: 13.0| **<span style="color:#6eb0ab;">DB4</span>**, **<span style="color:#3d519e;">DD4</span>**, **<span style="color:#2b665e;">VB6</span>** | **<span style="color:green;">AVB</span>**, **<span style="color:#3d519e;">DD5</span>**, **<span style="color:#2b665e;">VB6</span>** |
    |**Acetylcholine** | (60, 60) matrix | 4 non-zero entries, avg. weight: 13.5, sum: 54.0| **<span style="color:#6eb0ab;">DB4</span>**, **<span style="color:#85542b;">VA6</span>**, **<span style="color:#2b665e;">VB6</span>** | **<span style="color:#3d519e;">DD4</span>**, **<span style="color:#a6c7e6;">VD6</span>** |
    |**GABA** | (60, 60) matrix | 3 non-zero entries, avg. weight: 2.3333333333333335, sum: 7.0| **<span style="color:#a6c7e6;">VD3</span>**, **<span style="color:#a6c7e6;">VD6</span>** | **<span style="color:#85542b;">VA3</span>**, **<span style="color:#85542b;">VA6</span>**, **<span style="color:#2b665e;">VB2</span>** |
    
    
    | Nodes in current view<br/>(60 total)| Num cells in node<br/>(62 total) | Num in this dataset<br/>(11 total) | Cells |
    | --- | --- | --- | --- |
    |**<span style="color:blue;">AVA</span>** |2 | 0 | <a href="../AVAL" title="Layer 1 interneuron"><span style="text-decoration: line-through;"><span style="color:#ff3300;">AVAL</span></span></a>, <a href="../AVAR" title="Layer 1 interneuron"><span style="text-decoration: line-through;"><span style="color:#ff3300;">AVAR</span></span></a>|
    |**<span style="color:green;">AVB</span>** |2 | 2 | <a href="../AVBL" title="Layer 1 interneuron"><strong><span style="color:#ff3300;">AVBL</span></strong></a>, <a href="../AVBR" title="Layer 1 interneuron"><strong><span style="color:#ff3300;">AVBR</span></strong></a>|
    |**<span style="color:#d1b36e;">DA1</span>** |1 | 0 | <a href="../DA1" title="Ventral cord motor neuron"><span style="text-decoration: line-through;"><span style="color:#9966cc;">DA1</span></span></a>|
    |**<span style="color:#d1b36e;">DA2</span>** |1 | 0 | <a href="../DA2" title="Ventral cord motor neuron"><span style="text-decoration: line-through;"><span style="color:#9966cc;">DA2</span></span></a>|
    |**<span style="color:#d1b36e;">DA3</span>** |1 | 0 | <a href="../DA3" title="Ventral cord motor neuron"><span style="text-decoration: line-through;"><span style="color:#9966cc;">DA3</span></span></a>|
    |**<span style="color:#d1b36e;">DA4</span>** |1 | 0 | <a href="../DA4" title="Ventral cord motor neuron"><span style="text-decoration: line-through;"><span style="color:#9966cc;">DA4</span></span></a>|
    |**<span style="color:#d1b36e;">DA5</span>** |1 | 0 | <a href="../DA5" title="Ventral cord motor neuron"><span style="text-decoration: line-through;"><span style="color:#9966cc;">DA5</span></span></a>|
    |**<span style="color:#d1b36e;">DA6</span>** |1 | 0 | <a href="../DA6" title="Ventral cord motor neuron"><span style="text-decoration: line-through;"><span style="color:#9966cc;">DA6</span></span></a>|
    |**<span style="color:#d1b36e;">DA7</span>** |1 | 0 | <a href="../DA7" title="Ventral cord motor neuron"><span style="text-decoration: line-through;"><span style="color:#9966cc;">DA7</span></span></a>|
    |**<span style="color:#d1b36e;">DA8</span>** |1 | 0 | <a href="../DA8" title="Ventral cord motor neuron"><span style="text-decoration: line-through;"><span style="color:#9966cc;">DA8</span></span></a>|
    |**<span style="color:#d1b36e;">DA9</span>** |1 | 0 | <a href="../DA9" title="Ventral cord motor neuron"><span style="text-decoration: line-through;"><span style="color:#9966cc;">DA9</span></span></a>|
    |**<span style="color:#6eb0ab;">DB1</span>** |1 | 0 | <a href="../DB1" title="Ventral cord motor neuron"><span style="text-decoration: line-through;"><span style="color:#9966cc;">DB1</span></span></a>|
    |**<span style="color:#6eb0ab;">DB2</span>** |1 | 0 | <a href="../DB2" title="Ventral cord motor neuron"><span style="text-decoration: line-through;"><span style="color:#9966cc;">DB2</span></span></a>|
    |**<span style="color:#6eb0ab;">DB3</span>** |1 | 0 | <a href="../DB3" title="Ventral cord motor neuron"><span style="text-decoration: line-through;"><span style="color:#9966cc;">DB3</span></span></a>|
    |**<span style="color:#6eb0ab;">DB4</span>** |1 | 1 | <a href="../DB4" title="Ventral cord motor neuron"><strong><span style="color:#9966cc;">DB4</span></strong></a>|
    |**<span style="color:#6eb0ab;">DB5</span>** |1 | 0 | <a href="../DB5" title="Ventral cord motor neuron"><span style="text-decoration: line-through;"><span style="color:#9966cc;">DB5</span></span></a>|
    |**<span style="color:#6eb0ab;">DB6</span>** |1 | 0 | <a href="../DB6" title="Ventral cord motor neuron"><span style="text-decoration: line-through;"><span style="color:#9966cc;">DB6</span></span></a>|
    |**<span style="color:#6eb0ab;">DB7</span>** |1 | 0 | <a href="../DB7" title="Ventral cord motor neuron"><span style="text-decoration: line-through;"><span style="color:#9966cc;">DB7</span></span></a>|
    |**<span style="color:#3d519e;">DD1</span>** |1 | 0 | <a href="../DD1" title="Ventral cord motor neuron"><span style="text-decoration: line-through;"><span style="color:#9966cc;">DD1</span></span></a>|
    |**<span style="color:#3d519e;">DD2</span>** |1 | 0 | <a href="../DD2" title="Ventral cord motor neuron"><span style="text-decoration: line-through;"><span style="color:#9966cc;">DD2</span></span></a>|
    |**<span style="color:#3d519e;">DD3</span>** |1 | 0 | <a href="../DD3" title="Ventral cord motor neuron"><span style="text-decoration: line-through;"><span style="color:#9966cc;">DD3</span></span></a>|
    |**<span style="color:#3d519e;">DD4</span>** |1 | 1 | <a href="../DD4" title="Ventral cord motor neuron"><strong><span style="color:#9966cc;">DD4</span></strong></a>|
    |**<span style="color:#3d519e;">DD5</span>** |1 | 1 | <a href="../DD5" title="Ventral cord motor neuron"><strong><span style="color:#9966cc;">DD5</span></strong></a>|
    |**<span style="color:#3d519e;">DD6</span>** |1 | 0 | <a href="../DD6" title="Ventral cord motor neuron"><span style="text-decoration: line-through;"><span style="color:#9966cc;">DD6</span></span></a>|
    |**<span style="color:#85542b;">VA1</span>** |1 | 0 | <a href="../VA1" title="Ventral cord motor neuron"><span style="text-decoration: line-through;"><span style="color:#9966cc;">VA1</span></span></a>|
    |**<span style="color:#85542b;">VA10</span>** |1 | 0 | <a href="../VA10" title="Ventral cord motor neuron"><span style="text-decoration: line-through;"><span style="color:#9966cc;">VA10</span></span></a>|
    |**<span style="color:#85542b;">VA11</span>** |1 | 0 | <a href="../VA11" title="Ventral cord motor neuron"><span style="text-decoration: line-through;"><span style="color:#9966cc;">VA11</span></span></a>|
    |**<span style="color:#85542b;">VA12</span>** |1 | 0 | <a href="../VA12" title="Ventral cord motor neuron"><span style="text-decoration: line-through;"><span style="color:#9966cc;">VA12</span></span></a>|
    |**<span style="color:#85542b;">VA2</span>** |1 | 0 | <a href="../VA2" title="Ventral cord motor neuron"><span style="text-decoration: line-through;"><span style="color:#9966cc;">VA2</span></span></a>|
    |**<span style="color:#85542b;">VA3</span>** |1 | 1 | <a href="../VA3" title="Ventral cord motor neuron"><strong><span style="color:#9966cc;">VA3</span></strong></a>|
    |**<span style="color:#85542b;">VA4</span>** |1 | 0 | <a href="../VA4" title="Ventral cord motor neuron"><span style="text-decoration: line-through;"><span style="color:#9966cc;">VA4</span></span></a>|
    |**<span style="color:#85542b;">VA5</span>** |1 | 0 | <a href="../VA5" title="Ventral cord motor neuron"><span style="text-decoration: line-through;"><span style="color:#9966cc;">VA5</span></span></a>|
    |**<span style="color:#85542b;">VA6</span>** |1 | 1 | <a href="../VA6" title="Ventral cord motor neuron"><strong><span style="color:#9966cc;">VA6</span></strong></a>|
    |**<span style="color:#85542b;">VA7</span>** |1 | 0 | <a href="../VA7" title="Ventral cord motor neuron"><span style="text-decoration: line-through;"><span style="color:#9966cc;">VA7</span></span></a>|
    |**<span style="color:#85542b;">VA8</span>** |1 | 0 | <a href="../VA8" title="Ventral cord motor neuron"><span style="text-decoration: line-through;"><span style="color:#9966cc;">VA8</span></span></a>|
    |**<span style="color:#85542b;">VA9</span>** |1 | 0 | <a href="../VA9" title="Ventral cord motor neuron"><span style="text-decoration: line-through;"><span style="color:#9966cc;">VA9</span></span></a>|
    |**<span style="color:#2b665e;">VB1</span>** |1 | 0 | <a href="../VB1" title="Ventral cord motor neuron"><span style="text-decoration: line-through;"><span style="color:#9966cc;">VB1</span></span></a>|
    |**<span style="color:#2b665e;">VB10</span>** |1 | 0 | <a href="../VB10" title="Ventral cord motor neuron"><span style="text-decoration: line-through;"><span style="color:#9966cc;">VB10</span></span></a>|
    |**<span style="color:#2b665e;">VB11</span>** |1 | 0 | <a href="../VB11" title="Ventral cord motor neuron"><span style="text-decoration: line-through;"><span style="color:#9966cc;">VB11</span></span></a>|
    |**<span style="color:#2b665e;">VB2</span>** |1 | 1 | <a href="../VB2" title="Ventral cord motor neuron"><strong><span style="color:#9966cc;">VB2</span></strong></a>|
    |**<span style="color:#2b665e;">VB3</span>** |1 | 0 | <a href="../VB3" title="Ventral cord motor neuron"><span style="text-decoration: line-through;"><span style="color:#9966cc;">VB3</span></span></a>|
    |**<span style="color:#2b665e;">VB4</span>** |1 | 0 | <a href="../VB4" title="Ventral cord motor neuron"><span style="text-decoration: line-through;"><span style="color:#9966cc;">VB4</span></span></a>|
    |**<span style="color:#2b665e;">VB5</span>** |1 | 0 | <a href="../VB5" title="Ventral cord motor neuron"><span style="text-decoration: line-through;"><span style="color:#9966cc;">VB5</span></span></a>|
    |**<span style="color:#2b665e;">VB6</span>** |1 | 1 | <a href="../VB6" title="Ventral cord motor neuron"><strong><span style="color:#9966cc;">VB6</span></strong></a>|
    |**<span style="color:#2b665e;">VB7</span>** |1 | 0 | <a href="../VB7" title="Ventral cord motor neuron"><span style="text-decoration: line-through;"><span style="color:#9966cc;">VB7</span></span></a>|
    |**<span style="color:#2b665e;">VB8</span>** |1 | 0 | <a href="../VB8" title="Ventral cord motor neuron"><span style="text-decoration: line-through;"><span style="color:#9966cc;">VB8</span></span></a>|
    |**<span style="color:#2b665e;">VB9</span>** |1 | 0 | <a href="../VB9" title="Ventral cord motor neuron"><span style="text-decoration: line-through;"><span style="color:#9966cc;">VB9</span></span></a>|
    |**<span style="color:#a6c7e6;">VD1</span>** |1 | 0 | <a href="../VD1" title="Ventral cord motor neuron"><span style="text-decoration: line-through;"><span style="color:#9966cc;">VD1</span></span></a>|
    |**<span style="color:#a6c7e6;">VD10</span>** |1 | 0 | <a href="../VD10" title="Ventral cord motor neuron"><span style="text-decoration: line-through;"><span style="color:#9966cc;">VD10</span></span></a>|
    |**<span style="color:#a6c7e6;">VD11</span>** |1 | 0 | <a href="../VD11" title="Ventral cord motor neuron"><span style="text-decoration: line-through;"><span style="color:#9966cc;">VD11</span></span></a>|
    |**<span style="color:#a6c7e6;">VD12</span>** |1 | 0 | <a href="../VD12" title="Ventral cord motor neuron"><span style="text-decoration: line-through;"><span style="color:#9966cc;">VD12</span></span></a>|
    |**<span style="color:#a6c7e6;">VD13</span>** |1 | 0 | <a href="../VD13" title="Ventral cord motor neuron"><span style="text-decoration: line-through;"><span style="color:#9966cc;">VD13</span></span></a>|
    |**<span style="color:#a6c7e6;">VD2</span>** |1 | 0 | <a href="../VD2" title="Ventral cord motor neuron"><span style="text-decoration: line-through;"><span style="color:#9966cc;">VD2</span></span></a>|
    |**<span style="color:#a6c7e6;">VD3</span>** |1 | 1 | <a href="../VD3" title="Ventral cord motor neuron"><strong><span style="color:#9966cc;">VD3</span></strong></a>|
    |**<span style="color:#a6c7e6;">VD4</span>** |1 | 0 | <a href="../VD4" title="Ventral cord motor neuron"><span style="text-decoration: line-through;"><span style="color:#9966cc;">VD4</span></span></a>|
    |**<span style="color:#a6c7e6;">VD5</span>** |1 | 0 | <a href="../VD5" title="Ventral cord motor neuron"><span style="text-decoration: line-through;"><span style="color:#9966cc;">VD5</span></span></a>|
    |**<span style="color:#a6c7e6;">VD6</span>** |1 | 1 | <a href="../VD6" title="Ventral cord motor neuron"><strong><span style="color:#9966cc;">VD6</span></strong></a>|
    |**<span style="color:#a6c7e6;">VD7</span>** |1 | 0 | <a href="../VD7" title="Ventral cord motor neuron"><span style="text-decoration: line-through;"><span style="color:#9966cc;">VD7</span></span></a>|
    |**<span style="color:#a6c7e6;">VD8</span>** |1 | 0 | <a href="../VD8" title="Ventral cord motor neuron"><span style="text-decoration: line-through;"><span style="color:#9966cc;">VD8</span></span></a>|
    |**<span style="color:#a6c7e6;">VD9</span>** |1 | 0 | <a href="../VD9" title="Ventral cord motor neuron"><span style="text-decoration: line-through;"><span style="color:#9966cc;">VD9</span></span></a>|
    


### Neurons (herm) (21)
<details open><summary>Full list of Neurons (hermaphrodite only) in this dataset</summary>
<a href="../ASHR" title="Sensory neuron (amphid, nociceptive)"><span style="color:#ff66cc;">ASHR</span></a>
 | <a href="../ASKR" title="Sensory neuron (amphid)"><span style="color:#ff66cc;">ASKR</span></a>
 | <a href="../AVBL" title="Layer 1 interneuron"><span style="color:#ff3300;">AVBL</span></a>
 | <a href="../AVBR" title="Layer 1 interneuron"><span style="color:#ff3300;">AVBR</span></a>
 | <a href="../AWBR" title="Sensory neuron (amphid)"><span style="color:#ff66cc;">AWBR</span></a>
 | <a href="../DB4" title="Ventral cord motor neuron"><span style="color:#9966cc;">DB4</span></a>
 | <a href="../DD4" title="Ventral cord motor neuron"><span style="color:#9966cc;">DD4</span></a>
 | <a href="../DD5" title="Ventral cord motor neuron"><span style="color:#9966cc;">DD5</span></a>
 | <a href="../DVA" title="Sensory neuron (mechanosensory)"><span style="color:#ff66cc;">DVA</span></a>
 | <a href="../I5" title="Pharyngeal interneuron"><span style="color:#ff3300;">I5</span></a>
 | <a href="../M1" title="Pharyngeal motor neuron"><span style="color:#9966cc;">M1</span></a>
 | <a href="../M4" title="Pharyngeal motor neuron"><span style="color:#9966cc;">M4</span></a>
 | <a href="../PVCL" title="Layer 1 interneuron"><span style="color:#ff3300;">PVCL</span></a>
 | <a href="../PVCR" title="Layer 1 interneuron"><span style="color:#ff3300;">PVCR</span></a>
 | <a href="../RMGR" title="Layer 2 interneuron"><span style="color:#ff3300;">RMGR</span></a>
 | <a href="../VA3" title="Ventral cord motor neuron"><span style="color:#9966cc;">VA3</span></a>
 | <a href="../VA6" title="Ventral cord motor neuron"><span style="color:#9966cc;">VA6</span></a>
 | <a href="../VB2" title="Ventral cord motor neuron"><span style="color:#9966cc;">VB2</span></a>
 | <a href="../VB6" title="Ventral cord motor neuron"><span style="color:#9966cc;">VB6</span></a>
 | <a href="../VD3" title="Ventral cord motor neuron"><span style="color:#9966cc;">VD3</span></a>
 | <a href="../VD6" title="Ventral cord motor neuron"><span style="color:#9966cc;">VD6</span></a>

</details>

### Missing neurons (281)
<details open><summary>Full list of Missing neurons (known hermaphrodite neurons not present)</summary>
<a href="../ADAL" title="Layer 3 interneuron"><span style="color:#ff3300;">ADAL</span></a>
 | <a href="../ADAR" title="Layer 3 interneuron"><span style="color:#ff3300;">ADAR</span></a>
 | <a href="../ADEL" title="Sensory neuron (mechanosensory)"><span style="color:#ff66cc;">ADEL</span></a>
 | <a href="../ADER" title="Sensory neuron (mechanosensory)"><span style="color:#ff66cc;">ADER</span></a>
 | <a href="../ADFL" title="Sensory neuron (amphid)"><span style="color:#ff66cc;">ADFL</span></a>
 | <a href="../ADFR" title="Sensory neuron (amphid)"><span style="color:#ff66cc;">ADFR</span></a>
 | <a href="../ADLL" title="Sensory neuron (amphid, nociceptive)"><span style="color:#ff66cc;">ADLL</span></a>
 | <a href="../ADLR" title="Sensory neuron (amphid, nociceptive)"><span style="color:#ff66cc;">ADLR</span></a>
 | <a href="../AFDL" title="Sensory neuron (amphid)"><span style="color:#ff66cc;">AFDL</span></a>
 | <a href="../AFDR" title="Sensory neuron (amphid)"><span style="color:#ff66cc;">AFDR</span></a>
 | <a href="../AIAL" title="Layer 3 interneuron"><span style="color:#ff3300;">AIAL</span></a>
 | <a href="../AIAR" title="Layer 3 interneuron"><span style="color:#ff3300;">AIAR</span></a>
 | <a href="../AIBL" title="Layer 2 interneuron"><span style="color:#ff3300;">AIBL</span></a>
 | <a href="../AIBR" title="Layer 2 interneuron"><span style="color:#ff3300;">AIBR</span></a>
 | <a href="../AIML" title="Category 4 interneuron"><span style="color:#ff3300;">AIML</span></a>
 | <a href="../AIMR" title="Category 4 interneuron"><span style="color:#ff3300;">AIMR</span></a>
 | <a href="../AINL" title="Category 4 interneuron"><span style="color:#ff3300;">AINL</span></a>
 | <a href="../AINR" title="Category 4 interneuron"><span style="color:#ff3300;">AINR</span></a>
 | <a href="../AIYL" title="Layer 3 interneuron"><span style="color:#ff3300;">AIYL</span></a>
 | <a href="../AIYR" title="Layer 3 interneuron"><span style="color:#ff3300;">AIYR</span></a>
 | <a href="../AIZL" title="Layer 3 interneuron"><span style="color:#ff3300;">AIZL</span></a>
 | <a href="../AIZR" title="Layer 3 interneuron"><span style="color:#ff3300;">AIZR</span></a>
 | <a href="../ALA" title="Layer 3 interneuron"><span style="color:#ff3300;">ALA</span></a>
 | <a href="../ALML" title="Sensory neuron (mechanosensory)"><span style="color:#ff66cc;">ALML</span></a>
 | <a href="../ALMR" title="Sensory neuron (mechanosensory)"><span style="color:#ff66cc;">ALMR</span></a>
 | <a href="../ALNL" title="Sensory neuron (touch)"><span style="color:#ff66cc;">ALNL</span></a>
 | <a href="../ALNR" title="Sensory neuron (touch)"><span style="color:#ff66cc;">ALNR</span></a>
 | <a href="../AQR" title="Sensory neuron (touch)"><span style="color:#ff66cc;">AQR</span></a>
 | <a href="../AS1" title="Ventral cord motor neuron"><span style="color:#9966cc;">AS1</span></a>
 | <a href="../AS10" title="Ventral cord motor neuron"><span style="color:#9966cc;">AS10</span></a>
 | <a href="../AS11" title="Ventral cord motor neuron"><span style="color:#9966cc;">AS11</span></a>
 | <a href="../AS2" title="Ventral cord motor neuron"><span style="color:#9966cc;">AS2</span></a>
 | <a href="../AS3" title="Ventral cord motor neuron"><span style="color:#9966cc;">AS3</span></a>
 | <a href="../AS4" title="Ventral cord motor neuron"><span style="color:#9966cc;">AS4</span></a>
 | <a href="../AS5" title="Ventral cord motor neuron"><span style="color:#9966cc;">AS5</span></a>
 | <a href="../AS6" title="Ventral cord motor neuron"><span style="color:#9966cc;">AS6</span></a>
 | <a href="../AS7" title="Ventral cord motor neuron"><span style="color:#9966cc;">AS7</span></a>
 | <a href="../AS8" title="Ventral cord motor neuron"><span style="color:#9966cc;">AS8</span></a>
 | <a href="../AS9" title="Ventral cord motor neuron"><span style="color:#9966cc;">AS9</span></a>
 | <a href="../ASEL" title="Sensory neuron (amphid)"><span style="color:#ff66cc;">ASEL</span></a>
 | <a href="../ASER" title="Sensory neuron (amphid)"><span style="color:#ff66cc;">ASER</span></a>
 | <a href="../ASGL" title="Sensory neuron (amphid)"><span style="color:#ff66cc;">ASGL</span></a>
 | <a href="../ASGR" title="Sensory neuron (amphid)"><span style="color:#ff66cc;">ASGR</span></a>
 | <a href="../ASHL" title="Sensory neuron (amphid, nociceptive)"><span style="color:#ff66cc;">ASHL</span></a>
 | <a href="../ASIL" title="Sensory neuron (amphid)"><span style="color:#ff66cc;">ASIL</span></a>
 | <a href="../ASIR" title="Sensory neuron (amphid)"><span style="color:#ff66cc;">ASIR</span></a>
 | <a href="../ASJL" title="Sensory neuron (amphid)"><span style="color:#ff66cc;">ASJL</span></a>
 | <a href="../ASJR" title="Sensory neuron (amphid)"><span style="color:#ff66cc;">ASJR</span></a>
 | <a href="../ASKL" title="Sensory neuron (amphid)"><span style="color:#ff66cc;">ASKL</span></a>
 | <a href="../AUAL" title="Layer 3 interneuron"><span style="color:#ff3300;">AUAL</span></a>
 | <a href="../AUAR" title="Layer 3 interneuron"><span style="color:#ff3300;">AUAR</span></a>
 | <a href="../AVAL" title="Layer 1 interneuron"><span style="color:#ff3300;">AVAL</span></a>
 | <a href="../AVAR" title="Layer 1 interneuron"><span style="color:#ff3300;">AVAR</span></a>
 | <a href="../AVDL" title="Layer 2 interneuron"><span style="color:#ff3300;">AVDL</span></a>
 | <a href="../AVDR" title="Layer 2 interneuron"><span style="color:#ff3300;">AVDR</span></a>
 | <a href="../AVEL" title="Layer 1 interneuron"><span style="color:#ff3300;">AVEL</span></a>
 | <a href="../AVER" title="Layer 1 interneuron"><span style="color:#ff3300;">AVER</span></a>
 | <a href="../AVFL" title="Layer 3 interneuron"><span style="color:#ff3300;">AVFL</span></a>
 | <a href="../AVFR" title="Layer 3 interneuron"><span style="color:#ff3300;">AVFR</span></a>
 | <a href="../AVG" title="Layer 3 interneuron"><span style="color:#ff3300;">AVG</span></a>
 | <a href="../AVHL" title="Layer 3 interneuron"><span style="color:#ff3300;">AVHL</span></a>
 | <a href="../AVHR" title="Layer 3 interneuron"><span style="color:#ff3300;">AVHR</span></a>
 | <a href="../AVJL" title="Layer 2 interneuron"><span style="color:#ff3300;">AVJL</span></a>
 | <a href="../AVJR" title="Layer 2 interneuron"><span style="color:#ff3300;">AVJR</span></a>
 | <a href="../AVKL" title="Layer 2 interneuron"><span style="color:#ff3300;">AVKL</span></a>
 | <a href="../AVKR" title="Layer 2 interneuron"><span style="color:#ff3300;">AVKR</span></a>
 | <a href="../AVL" title="Layer 2 interneuron"><span style="color:#ff3300;">AVL</span></a>
 | <a href="../AVM" title="Sensory neuron (mechanosensory)"><span style="color:#ff66cc;">AVM</span></a>
 | <a href="../AWAL" title="Sensory neuron (amphid)"><span style="color:#ff66cc;">AWAL</span></a>
 | <a href="../AWAR" title="Sensory neuron (amphid)"><span style="color:#ff66cc;">AWAR</span></a>
 | <a href="../AWBL" title="Sensory neuron (amphid)"><span style="color:#ff66cc;">AWBL</span></a>
 | <a href="../AWCL" title="Sensory neuron (amphid)"><span style="color:#ff66cc;">AWCL</span></a>
 | <a href="../AWCR" title="Sensory neuron (amphid)"><span style="color:#ff66cc;">AWCR</span></a>
 | <a href="../BAGL" title="Sensory neuron (O2, CO2, social signals, touch)"><span style="color:#ff66cc;">BAGL</span></a>
 | <a href="../BAGR" title="Sensory neuron (O2, CO2, social signals, touch)"><span style="color:#ff66cc;">BAGR</span></a>
 | <a href="../BDUL" title="Layer 3 interneuron"><span style="color:#ff3300;">BDUL</span></a>
 | <a href="../BDUR" title="Layer 3 interneuron"><span style="color:#ff3300;">BDUR</span></a>
 | <a href="../CANL" title="Canal neuron"><span style="color:#990033;">CANL</span></a>
 | <a href="../CANR" title="Canal neuron"><span style="color:#990033;">CANR</span></a>
 | <a href="../CEPDL" title="Sensory neuron (cephalic)"><span style="color:#ff66cc;">CEPDL</span></a>
 | <a href="../CEPDR" title="Sensory neuron (cephalic)"><span style="color:#ff66cc;">CEPDR</span></a>
 | <a href="../CEPVL" title="Sensory neuron (cephalic)"><span style="color:#ff66cc;">CEPVL</span></a>
 | <a href="../CEPVR" title="Sensory neuron (cephalic)"><span style="color:#ff66cc;">CEPVR</span></a>
 | <a href="../DA1" title="Ventral cord motor neuron"><span style="color:#9966cc;">DA1</span></a>
 | <a href="../DA2" title="Ventral cord motor neuron"><span style="color:#9966cc;">DA2</span></a>
 | <a href="../DA3" title="Ventral cord motor neuron"><span style="color:#9966cc;">DA3</span></a>
 | <a href="../DA4" title="Ventral cord motor neuron"><span style="color:#9966cc;">DA4</span></a>
 | <a href="../DA5" title="Ventral cord motor neuron"><span style="color:#9966cc;">DA5</span></a>
 | <a href="../DA6" title="Ventral cord motor neuron"><span style="color:#9966cc;">DA6</span></a>
 | <a href="../DA7" title="Ventral cord motor neuron"><span style="color:#9966cc;">DA7</span></a>
 | <a href="../DA8" title="Ventral cord motor neuron"><span style="color:#9966cc;">DA8</span></a>
 | <a href="../DA9" title="Ventral cord motor neuron"><span style="color:#9966cc;">DA9</span></a>
 | <a href="../DB1" title="Ventral cord motor neuron"><span style="color:#9966cc;">DB1</span></a>
 | <a href="../DB2" title="Ventral cord motor neuron"><span style="color:#9966cc;">DB2</span></a>
 | <a href="../DB3" title="Ventral cord motor neuron"><span style="color:#9966cc;">DB3</span></a>
 | <a href="../DB5" title="Ventral cord motor neuron"><span style="color:#9966cc;">DB5</span></a>
 | <a href="../DB6" title="Ventral cord motor neuron"><span style="color:#9966cc;">DB6</span></a>
 | <a href="../DB7" title="Ventral cord motor neuron"><span style="color:#9966cc;">DB7</span></a>
 | <a href="../DD1" title="Ventral cord motor neuron"><span style="color:#9966cc;">DD1</span></a>
 | <a href="../DD2" title="Ventral cord motor neuron"><span style="color:#9966cc;">DD2</span></a>
 | <a href="../DD3" title="Ventral cord motor neuron"><span style="color:#9966cc;">DD3</span></a>
 | <a href="../DD6" title="Ventral cord motor neuron"><span style="color:#9966cc;">DD6</span></a>
 | <a href="../DVB" title="Layer 3 interneuron"><span style="color:#ff3300;">DVB</span></a>
 | <a href="../DVC" title="Layer 2 interneuron"><span style="color:#ff3300;">DVC</span></a>
 | <a href="../FLPL" title="Sensory neuron (mechanosensory)"><span style="color:#ff66cc;">FLPL</span></a>
 | <a href="../FLPR" title="Sensory neuron (mechanosensory)"><span style="color:#ff66cc;">FLPR</span></a>
 | <a href="../HSNL" title="Hermaphrodite specific motor neuron"><span style="color:#9966cc;">HSNL</span></a>
 | <a href="../HSNR" title="Hermaphrodite specific motor neuron"><span style="color:#9966cc;">HSNR</span></a>
 | <a href="../I1L" title="Pharyngeal interneuron"><span style="color:#ff3300;">I1L</span></a>
 | <a href="../I1R" title="Pharyngeal interneuron"><span style="color:#ff3300;">I1R</span></a>
 | <a href="../I2L" title="Pharyngeal interneuron"><span style="color:#ff3300;">I2L</span></a>
 | <a href="../I2R" title="Pharyngeal interneuron"><span style="color:#ff3300;">I2R</span></a>
 | <a href="../I3" title="Pharyngeal interneuron"><span style="color:#ff3300;">I3</span></a>
 | <a href="../I4" title="Pharyngeal interneuron"><span style="color:#ff3300;">I4</span></a>
 | <a href="../I6" title="Pharyngeal interneuron"><span style="color:#ff3300;">I6</span></a>
 | <a href="../IL1DL" title="Sensory neuron (cephalic)"><span style="color:#ff66cc;">IL1DL</span></a>
 | <a href="../IL1DR" title="Sensory neuron (cephalic)"><span style="color:#ff66cc;">IL1DR</span></a>
 | <a href="../IL1L" title="Sensory neuron (cephalic)"><span style="color:#ff66cc;">IL1L</span></a>
 | <a href="../IL1R" title="Sensory neuron (cephalic)"><span style="color:#ff66cc;">IL1R</span></a>
 | <a href="../IL1VL" title="Sensory neuron (cephalic)"><span style="color:#ff66cc;">IL1VL</span></a>
 | <a href="../IL1VR" title="Sensory neuron (cephalic)"><span style="color:#ff66cc;">IL1VR</span></a>
 | <a href="../IL2DL" title="Sensory neuron (cephalic)"><span style="color:#ff66cc;">IL2DL</span></a>
 | <a href="../IL2DR" title="Sensory neuron (cephalic)"><span style="color:#ff66cc;">IL2DR</span></a>
 | <a href="../IL2L" title="Sensory neuron (cephalic)"><span style="color:#ff66cc;">IL2L</span></a>
 | <a href="../IL2R" title="Sensory neuron (cephalic)"><span style="color:#ff66cc;">IL2R</span></a>
 | <a href="../IL2VL" title="Sensory neuron (cephalic)"><span style="color:#ff66cc;">IL2VL</span></a>
 | <a href="../IL2VR" title="Sensory neuron (cephalic)"><span style="color:#ff66cc;">IL2VR</span></a>
 | <a href="../LUAL" title="Layer 3 interneuron"><span style="color:#ff3300;">LUAL</span></a>
 | <a href="../LUAR" title="Layer 3 interneuron"><span style="color:#ff3300;">LUAR</span></a>
 | <a href="../M2L" title="Pharyngeal motor neuron"><span style="color:#9966cc;">M2L</span></a>
 | <a href="../M2R" title="Pharyngeal motor neuron"><span style="color:#9966cc;">M2R</span></a>
 | <a href="../M3L" title="Pharyngeal motor neuron"><span style="color:#9966cc;">M3L</span></a>
 | <a href="../M3R" title="Pharyngeal motor neuron"><span style="color:#9966cc;">M3R</span></a>
 | <a href="../M5" title="Pharyngeal motor neuron"><span style="color:#9966cc;">M5</span></a>
 | <a href="../MCL" title="Pharyngeal polymodal neuron"><span style="color:#cc0033;">MCL</span></a>
 | <a href="../MCR" title="Pharyngeal polymodal neuron"><span style="color:#cc0033;">MCR</span></a>
 | <a href="../MI" title="Pharyngeal polymodal neuron"><span style="color:#cc0033;">MI</span></a>
 | <a href="../NSML" title="Pharyngeal polymodal neuron"><span style="color:#cc0033;">NSML</span></a>
 | <a href="../NSMR" title="Pharyngeal polymodal neuron"><span style="color:#cc0033;">NSMR</span></a>
 | <a href="../OLLL" title="Sensory neuron (cephalic)"><span style="color:#ff66cc;">OLLL</span></a>
 | <a href="../OLLR" title="Sensory neuron (cephalic)"><span style="color:#ff66cc;">OLLR</span></a>
 | <a href="../OLQDL" title="Sensory neuron (cephalic)"><span style="color:#ff66cc;">OLQDL</span></a>
 | <a href="../OLQDR" title="Sensory neuron (cephalic)"><span style="color:#ff66cc;">OLQDR</span></a>
 | <a href="../OLQVL" title="Sensory neuron (cephalic)"><span style="color:#ff66cc;">OLQVL</span></a>
 | <a href="../OLQVR" title="Sensory neuron (cephalic)"><span style="color:#ff66cc;">OLQVR</span></a>
 | <a href="../PDA" title="Ventral cord motor neuron"><span style="color:#9966cc;">PDA</span></a>
 | <a href="../PDB" title="Ventral cord motor neuron"><span style="color:#9966cc;">PDB</span></a>
 | <a href="../PDEL" title="Sensory neuron (mechanosensory)"><span style="color:#ff66cc;">PDEL</span></a>
 | <a href="../PDER" title="Sensory neuron (mechanosensory)"><span style="color:#ff66cc;">PDER</span></a>
 | <a href="../PHAL" title="Sensory neuron (phasmid)"><span style="color:#ff66cc;">PHAL</span></a>
 | <a href="../PHAR" title="Sensory neuron (phasmid)"><span style="color:#ff66cc;">PHAR</span></a>
 | <a href="../PHBL" title="Sensory neuron (phasmid)"><span style="color:#ff66cc;">PHBL</span></a>
 | <a href="../PHBR" title="Sensory neuron (phasmid)"><span style="color:#ff66cc;">PHBR</span></a>
 | <a href="../PHCL" title="Sensory neuron (phasmid)"><span style="color:#ff66cc;">PHCL</span></a>
 | <a href="../PHCR" title="Sensory neuron (phasmid)"><span style="color:#ff66cc;">PHCR</span></a>
 | <a href="../PLML" title="Sensory neuron (mechanosensory)"><span style="color:#ff66cc;">PLML</span></a>
 | <a href="../PLMR" title="Sensory neuron (mechanosensory)"><span style="color:#ff66cc;">PLMR</span></a>
 | <a href="../PLNL" title="Sensory neuron (touch)"><span style="color:#ff66cc;">PLNL</span></a>
 | <a href="../PLNR" title="Sensory neuron (touch)"><span style="color:#ff66cc;">PLNR</span></a>
 | <a href="../PQR" title="Sensory neuron (touch)"><span style="color:#ff66cc;">PQR</span></a>
 | <a href="../PVDL" title="Sensory neuron (mechanosensory)"><span style="color:#ff66cc;">PVDL</span></a>
 | <a href="../PVDR" title="Sensory neuron (mechanosensory)"><span style="color:#ff66cc;">PVDR</span></a>
 | <a href="../PVM" title="Sensory neuron (mechanosensory)"><span style="color:#ff66cc;">PVM</span></a>
 | <a href="../PVNL" title="Layer 3 interneuron"><span style="color:#ff3300;">PVNL</span></a>
 | <a href="../PVNR" title="Layer 3 interneuron"><span style="color:#ff3300;">PVNR</span></a>
 | <a href="../PVPL" title="Layer 3 interneuron"><span style="color:#ff3300;">PVPL</span></a>
 | <a href="../PVPR" title="Layer 3 interneuron"><span style="color:#ff3300;">PVPR</span></a>
 | <a href="../PVQL" title="Layer 3 interneuron"><span style="color:#ff3300;">PVQL</span></a>
 | <a href="../PVQR" title="Layer 3 interneuron"><span style="color:#ff3300;">PVQR</span></a>
 | <a href="../PVR" title="Layer 3 interneuron"><span style="color:#ff3300;">PVR</span></a>
 | <a href="../PVT" title="Layer 2 interneuron"><span style="color:#ff3300;">PVT</span></a>
 | <a href="../PVWL" title="Layer 2 interneuron"><span style="color:#ff3300;">PVWL</span></a>
 | <a href="../PVWR" title="Layer 2 interneuron"><span style="color:#ff3300;">PVWR</span></a>
 | <a href="../RIAL" title="Layer 1 interneuron"><span style="color:#ff3300;">RIAL</span></a>
 | <a href="../RIAR" title="Layer 1 interneuron"><span style="color:#ff3300;">RIAR</span></a>
 | <a href="../RIBL" title="Layer 2 interneuron"><span style="color:#ff3300;">RIBL</span></a>
 | <a href="../RIBR" title="Layer 2 interneuron"><span style="color:#ff3300;">RIBR</span></a>
 | <a href="../RICL" title="Layer 2 interneuron"><span style="color:#ff3300;">RICL</span></a>
 | <a href="../RICR" title="Layer 2 interneuron"><span style="color:#ff3300;">RICR</span></a>
 | <a href="../RID" title="Layer 1 interneuron"><span style="color:#ff3300;">RID</span></a>
 | <a href="../RIFL" title="Layer 3 interneuron"><span style="color:#ff3300;">RIFL</span></a>
 | <a href="../RIFR" title="Layer 3 interneuron"><span style="color:#ff3300;">RIFR</span></a>
 | <a href="../RIGL" title="Layer 2 interneuron"><span style="color:#ff3300;">RIGL</span></a>
 | <a href="../RIGR" title="Layer 2 interneuron"><span style="color:#ff3300;">RIGR</span></a>
 | <a href="../RIH" title="Category 4 interneuron"><span style="color:#ff3300;">RIH</span></a>
 | <a href="../RIML" title="Layer 1 interneuron; motorneuron in White et al., 1986"><span style="color:#ff3300;">RIML</span></a>
 | <a href="../RIMR" title="Layer 1 interneuron; motorneuron in White et al., 1986"><span style="color:#ff3300;">RIMR</span></a>
 | <a href="../RIPL" title="Linker to pharynx"><span style="color:#ff3300;">RIPL</span></a>
 | <a href="../RIPR" title="Linker to pharynx"><span style="color:#ff3300;">RIPR</span></a>
 | <a href="../RIR" title="Category 4 interneuron"><span style="color:#ff3300;">RIR</span></a>
 | <a href="../RIS" title="Layer 3 interneuron"><span style="color:#ff3300;">RIS</span></a>
 | <a href="../RIVL" title="Head motor neuron"><span style="color:#9966cc;">RIVL</span></a>
 | <a href="../RIVR" title="Head motor neuron"><span style="color:#9966cc;">RIVR</span></a>
 | <a href="../RMDDL" title="Head motor neuron"><span style="color:#9966cc;">RMDDL</span></a>
 | <a href="../RMDDR" title="Head motor neuron"><span style="color:#9966cc;">RMDDR</span></a>
 | <a href="../RMDL" title="Head motor neuron"><span style="color:#9966cc;">RMDL</span></a>
 | <a href="../RMDR" title="Head motor neuron"><span style="color:#9966cc;">RMDR</span></a>
 | <a href="../RMDVL" title="Head motor neuron"><span style="color:#9966cc;">RMDVL</span></a>
 | <a href="../RMDVR" title="Head motor neuron"><span style="color:#9966cc;">RMDVR</span></a>
 | <a href="../RMED" title="Head motor neuron"><span style="color:#9966cc;">RMED</span></a>
 | <a href="../RMEL" title="Head motor neuron"><span style="color:#9966cc;">RMEL</span></a>
 | <a href="../RMER" title="Head motor neuron"><span style="color:#9966cc;">RMER</span></a>
 | <a href="../RMEV" title="Head motor neuron"><span style="color:#9966cc;">RMEV</span></a>
 | <a href="../RMFL" title="Layer 2 interneuron"><span style="color:#ff3300;">RMFL</span></a>
 | <a href="../RMFR" title="Layer 2 interneuron"><span style="color:#ff3300;">RMFR</span></a>
 | <a href="../RMGL" title="Layer 2 interneuron"><span style="color:#ff3300;">RMGL</span></a>
 | <a href="../RMHL" title="Head motor neuron"><span style="color:#9966cc;">RMHL</span></a>
 | <a href="../RMHR" title="Head motor neuron"><span style="color:#9966cc;">RMHR</span></a>
 | <a href="../SAADL" title="Layer 2 interneuron"><span style="color:#ff3300;">SAADL</span></a>
 | <a href="../SAADR" title="Layer 2 interneuron"><span style="color:#ff3300;">SAADR</span></a>
 | <a href="../SAAVL" title="Layer 2 interneuron"><span style="color:#ff3300;">SAAVL</span></a>
 | <a href="../SAAVR" title="Layer 2 interneuron"><span style="color:#ff3300;">SAAVR</span></a>
 | <a href="../SABD" title="Sublateral motor neuron; interneuron in White et al., 1986"><span style="color:#9966cc;">SABD</span></a>
 | <a href="../SABVL" title="Sublateral motor neuron; interneuron in White et al., 1986"><span style="color:#9966cc;">SABVL</span></a>
 | <a href="../SABVR" title="Sublateral motor neuron; interneuron in White et al., 1986"><span style="color:#9966cc;">SABVR</span></a>
 | <a href="../SDQL" title="Sensory neuron (touch)"><span style="color:#ff66cc;">SDQL</span></a>
 | <a href="../SDQR" title="Sensory neuron (touch)"><span style="color:#ff66cc;">SDQR</span></a>
 | <a href="../SIADL" title="Sublateral motor neuron; interneuron in White et al., 1986"><span style="color:#9966cc;">SIADL</span></a>
 | <a href="../SIADR" title="Sublateral motor neuron; interneuron in White et al., 1986"><span style="color:#9966cc;">SIADR</span></a>
 | <a href="../SIAVL" title="Sublateral motor neuron; interneuron in White et al., 1986"><span style="color:#9966cc;">SIAVL</span></a>
 | <a href="../SIAVR" title="Sublateral motor neuron; interneuron in White et al., 1986"><span style="color:#9966cc;">SIAVR</span></a>
 | <a href="../SIBDL" title="Sublateral motor neuron; interneuron in White et al., 1986"><span style="color:#9966cc;">SIBDL</span></a>
 | <a href="../SIBDR" title="Sublateral motor neuron; interneuron in White et al., 1986"><span style="color:#9966cc;">SIBDR</span></a>
 | <a href="../SIBVL" title="Sublateral motor neuron; interneuron in White et al., 1986"><span style="color:#9966cc;">SIBVL</span></a>
 | <a href="../SIBVR" title="Sublateral motor neuron; interneuron in White et al., 1986"><span style="color:#9966cc;">SIBVR</span></a>
 | <a href="../SMBDL" title="Sublateral motor neuron"><span style="color:#9966cc;">SMBDL</span></a>
 | <a href="../SMBDR" title="Sublateral motor neuron"><span style="color:#9966cc;">SMBDR</span></a>
 | <a href="../SMBVL" title="Sublateral motor neuron"><span style="color:#9966cc;">SMBVL</span></a>
 | <a href="../SMBVR" title="Sublateral motor neuron"><span style="color:#9966cc;">SMBVR</span></a>
 | <a href="../SMDDL" title="Sublateral motor neuron"><span style="color:#9966cc;">SMDDL</span></a>
 | <a href="../SMDDR" title="Sublateral motor neuron"><span style="color:#9966cc;">SMDDR</span></a>
 | <a href="../SMDVL" title="Sublateral motor neuron"><span style="color:#9966cc;">SMDVL</span></a>
 | <a href="../SMDVR" title="Sublateral motor neuron"><span style="color:#9966cc;">SMDVR</span></a>
 | <a href="../URADL" title="Head motor neuron"><span style="color:#9966cc;">URADL</span></a>
 | <a href="../URADR" title="Head motor neuron"><span style="color:#9966cc;">URADR</span></a>
 | <a href="../URAVL" title="Head motor neuron"><span style="color:#9966cc;">URAVL</span></a>
 | <a href="../URAVR" title="Head motor neuron"><span style="color:#9966cc;">URAVR</span></a>
 | <a href="../URBL" title="Category 4 interneuron"><span style="color:#ff3300;">URBL</span></a>
 | <a href="../URBR" title="Category 4 interneuron"><span style="color:#ff3300;">URBR</span></a>
 | <a href="../URXL" title="Sensory neuron (O2, CO2, social signals, touch)"><span style="color:#ff66cc;">URXL</span></a>
 | <a href="../URXR" title="Sensory neuron (O2, CO2, social signals, touch)"><span style="color:#ff66cc;">URXR</span></a>
 | <a href="../URYDL" title="Sensory neuron (cephalic)"><span style="color:#ff66cc;">URYDL</span></a>
 | <a href="../URYDR" title="Sensory neuron (cephalic)"><span style="color:#ff66cc;">URYDR</span></a>
 | <a href="../URYVL" title="Sensory neuron (cephalic)"><span style="color:#ff66cc;">URYVL</span></a>
 | <a href="../URYVR" title="Sensory neuron (cephalic)"><span style="color:#ff66cc;">URYVR</span></a>
 | <a href="../VA1" title="Ventral cord motor neuron"><span style="color:#9966cc;">VA1</span></a>
 | <a href="../VA10" title="Ventral cord motor neuron"><span style="color:#9966cc;">VA10</span></a>
 | <a href="../VA11" title="Ventral cord motor neuron"><span style="color:#9966cc;">VA11</span></a>
 | <a href="../VA12" title="Ventral cord motor neuron"><span style="color:#9966cc;">VA12</span></a>
 | <a href="../VA2" title="Ventral cord motor neuron"><span style="color:#9966cc;">VA2</span></a>
 | <a href="../VA4" title="Ventral cord motor neuron"><span style="color:#9966cc;">VA4</span></a>
 | <a href="../VA5" title="Ventral cord motor neuron"><span style="color:#9966cc;">VA5</span></a>
 | <a href="../VA7" title="Ventral cord motor neuron"><span style="color:#9966cc;">VA7</span></a>
 | <a href="../VA8" title="Ventral cord motor neuron"><span style="color:#9966cc;">VA8</span></a>
 | <a href="../VA9" title="Ventral cord motor neuron"><span style="color:#9966cc;">VA9</span></a>
 | <a href="../VB1" title="Ventral cord motor neuron"><span style="color:#9966cc;">VB1</span></a>
 | <a href="../VB10" title="Ventral cord motor neuron"><span style="color:#9966cc;">VB10</span></a>
 | <a href="../VB11" title="Ventral cord motor neuron"><span style="color:#9966cc;">VB11</span></a>
 | <a href="../VB3" title="Ventral cord motor neuron"><span style="color:#9966cc;">VB3</span></a>
 | <a href="../VB4" title="Ventral cord motor neuron"><span style="color:#9966cc;">VB4</span></a>
 | <a href="../VB5" title="Ventral cord motor neuron"><span style="color:#9966cc;">VB5</span></a>
 | <a href="../VB7" title="Ventral cord motor neuron"><span style="color:#9966cc;">VB7</span></a>
 | <a href="../VB8" title="Ventral cord motor neuron"><span style="color:#9966cc;">VB8</span></a>
 | <a href="../VB9" title="Ventral cord motor neuron"><span style="color:#9966cc;">VB9</span></a>
 | <a href="../VC1" title="Hermaphrodite specific motor neuron"><span style="color:#9966cc;">VC1</span></a>
 | <a href="../VC2" title="Hermaphrodite specific motor neuron"><span style="color:#9966cc;">VC2</span></a>
 | <a href="../VC3" title="Hermaphrodite specific motor neuron"><span style="color:#9966cc;">VC3</span></a>
 | <a href="../VC4" title="Hermaphrodite specific motor neuron"><span style="color:#9966cc;">VC4</span></a>
 | <a href="../VC5" title="Hermaphrodite specific motor neuron"><span style="color:#9966cc;">VC5</span></a>
 | <a href="../VC6" title="Hermaphrodite specific motor neuron"><span style="color:#9966cc;">VC6</span></a>
 | <a href="../VD1" title="Ventral cord motor neuron"><span style="color:#9966cc;">VD1</span></a>
 | <a href="../VD10" title="Ventral cord motor neuron"><span style="color:#9966cc;">VD10</span></a>
 | <a href="../VD11" title="Ventral cord motor neuron"><span style="color:#9966cc;">VD11</span></a>
 | <a href="../VD12" title="Ventral cord motor neuron"><span style="color:#9966cc;">VD12</span></a>
 | <a href="../VD13" title="Ventral cord motor neuron"><span style="color:#9966cc;">VD13</span></a>
 | <a href="../VD2" title="Ventral cord motor neuron"><span style="color:#9966cc;">VD2</span></a>
 | <a href="../VD4" title="Ventral cord motor neuron"><span style="color:#9966cc;">VD4</span></a>
 | <a href="../VD5" title="Ventral cord motor neuron"><span style="color:#9966cc;">VD5</span></a>
 | <a href="../VD7" title="Ventral cord motor neuron"><span style="color:#9966cc;">VD7</span></a>
 | <a href="../VD8" title="Ventral cord motor neuron"><span style="color:#9966cc;">VD8</span></a>
 | <a href="../VD9" title="Ventral cord motor neuron"><span style="color:#9966cc;">VD9</span></a>

</details>

### Muscles (0)

### Other cells (0)
