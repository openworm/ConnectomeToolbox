# Overview

Information on published connectomics data related to _C. elegans_. This is being developed as part of the [OpenWorm project](https://www.openworm.org).

**Please note: this is a <u>Work in Progress</u>! Please contact padraig -at- openworm.org if you are interested in contributing to this work.**

- Anatomical connectome (Albertson & Thomson 1976; White et al. 1986; Durbin 1987; Varshney et al. 2011; Cook et al. 2019; Cook et al. 2020; Witvliet et al. 2021)
- Gene Expression Map (Altun et al. 2009; CenGEN)
- Extrasynaptic connectome (Pereira et al. 2015; Bentley et al. 2016; Beets et al. 2023; Ripoll-Sanchez et al. 2023)
- Functional connectome (Randi et al. 2023)
- Developmental connectome (Witvliet et al. 2021)

## Datasets

| Papers                                                     | Features      | Datasets      | Readers |
| -------------                                              | -----         | -----         | ---- |
| [White et al. 1986](White_1984.md)     | |[N2U.txt](https://github.com/dwitvliet/nature2021/blob/0646af9d25896ae660f97d462eab2d67282f5625/data/legacy_data/wormwiring_N2U.txt)|  N/A |
| [Durbin 1987](Durbin_1987.md)    | |[Durbin.txt](https://github.com/dwitvliet/nature2021/blob/0646af9d25896ae660f97d462eab2d67282f5625/data/legacy_data/durbin.txt)| N/A |
| [Altun et al. 2009](Altun_2009.md)   | |[Db.dump](datasets/neurons/Modified_celegans_db_dump.csv)| [OpenWormReader](https://github.com/yasinthanvickneswaran/c302/blob/7c7fc016c73c500567c94414ee0b7f7a4829084f/c302/OpenWormReader.py) |
| [Varshney et al. 2011](Varshney_2011.md)  |    | [NeuronsConnect](datasets/neurons/NeuronConnectFormatted(1).xlsx)   | [SpreadsheetDataReader](https://github.com/yasinthanvickneswaran/c302/blob/7c7fc016c73c500567c94414ee0b7f7a4829084f/c302/SpreadsheetDataReader.py) |
| [Pereira et al. 2015](Pereira_2015.md)  | |[Cholinergic neurons](https://doi.org/10.7554/eLife.12432.003) [NT_Map_herm](https://doi.org/10.7554/eLife.12432.009) [WormWiring](https://doi.org/10.7554/eLife.12432.010) [male_cholinergic](https://doi.org/10.7554/eLife.12432.016) [transcriptional_regulators](https://doi.org/10.7554/eLife.12432.019)| N/A |
| [Bentley et al. 2016](Bentley_2016.md)  |  | [csv](datasets/neurons/Bentley_et_al_2016_expression.csv) | N/A |
| [Cook et al. 2019](Cook_2019.md)          |      |[herm_full_edgelist.csv](datasets/neurons/herm_full_edgelist.csv) | [UpdatedSpreadsheetDataReader](https://github.com/yasinthanvickneswaran/c302/blob/7c7fc016c73c500567c94414ee0b7f7a4829084f/c302/UpdatedSpreadsheetDataReader.py) [UpdatedSpreadsheetDataReader2](https://github.com/yasinthanvickneswaran/c302/blob/7c7fc016c73c500567c94414ee0b7f7a4829084f/c302/UpdatedSpreadsheetDataReader2.py) |
| [Fenyves et al. 2020](Fenyves_2020.md)    |   | [data](https://github.com/francescorandi/wormneuroatlas/blob/main/wormneuroatlas/data/journal.pcbi.1007974.s003.xlsx) | N/A  |
| [Brittin et al. 2021](Brittin_2021.md)    |   | [data](https://github.com/cabrittin/elegansbrainmap/tree/049a26a094e085bacc70f5b05ea04a007d00eb2c/data) [parsed](https://github.com/cabrittin/parsetrakem2)| N/A  |
| [Witvliet et al. 2021](Witvliet_2021.md)  |  | [physical.csv](https://github.com/dwitvliet/nature2021/tree/0646af9d25896ae660f97d462eab2d67282f5625/data/physical_contact) [synapses.json](https://github.com/dwitvliet/nature2021/tree/0646af9d25896ae660f97d462eab2d67282f5625/data/synapses) [skeletons.json](https://github.com/dwitvliet/nature2021/tree/0646af9d25896ae660f97d462eab2d67282f5625/data/skeletons) | N/A |
| [Taylor et al. 2021](Taylor_2021.md)    |   | [data](https://github.com/cengenproject/CeNGEN_integrated_analysis_biorxiv_code) | N/A  |
| [Beets et al. 2023](Beets_2023.md)    |   | [data](https://github.com/cengenproject/CeNGEN_integrated_analysis_biorxiv_code) | N/A  |

