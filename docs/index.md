# Overview

Information on published connectomics data related to _C. elegans_. This is being developed as part of the [OpenWorm project](https://www.openworm.org).

**Please note: this is a <u>Work in Progress</u>! Please [get in contact](About.md) if you are interested in contributing to this resource!**

### Example plots

Some of the generated views of the connectomics datasets covered here. Click on the images for more details.

<a href="Cook2019Male_data_graph/#electrical"><img src="assets/Cook2019Male_Raw_Electrical_graph.png" width="45%"></img></a>
<a href="RipollSanchezShortRange_data"><img src="assets/RipollSanchezShortRange_Raw_Extrasynaptic.png" width="45%"></img></a>
<a href="Escape_Cook2019Herm_data_graph/#chemical-exc"><img src="assets/Cook2019Herm_Escape_Chemical_Exc_graph.png" width="45%"></img></a>
<a href="Cook2020_data_hiveplot/#chemical"><img src="assets/Cook2020_Pharynx_Chemical_Exc_hiveplot.png" width="45%"></img></a>

### Historical publications on _C. elegans_ connectomics

```mermaid
block-beta
columns 4

t1["<b>Anatomical - Chemical/electrical</b>"]
t2["<b>Extrasynaptic</b>"]
t4["<b>Gene/protein expression</b>"]
t3["<b>Functional</b>"]

  style t1 fill:#ff6666
  style t2 fill:#99bbff
  style t3 fill:#ff80ff
  style t4 fill:#85e085

```
```mermaid
block-beta

columns 4

  block:70sA
    columns 1
    space    
    A1("<b><a href='Albertson_1976'>Albertson and Thomson 1976</a></b>")
    space space space
  end

  block:70sB
    columns 1
    space
  end

  block:70sC
    columns 1
    space
  end
  
  block:70sD
    columns 1
    space
  end

  block:80sA
    columns 1
    A("<b><a href='White_1986' >White et al. 1986</a></b>")
    space
    B("<b><a href='Durbin_1987/' >Durbin 1987</a></b>")
    space
    space
  end

  block:80sB
    columns 1
    space
  end

  block:80sC
    columns 1
    space
  end
  
  block:80sD
    columns 1
    space
  end

  block:90sA
    columns 1
    space
    A2("<b><a href='Hall_1991/'>Hall & Russell 1991</a></b>") space space space
  end
  
  block:90sB
    columns 1
    space
  end

  block:90sC
    columns 1
    space
  end
  
  block:90sD
    columns 1
    space
  end

  block:00sA
    columns 1
    space
  end

  block:00sB
    columns 1
    space
  end

  block:00sC
    columns 1
    C("<b><a href='Altun_2009/'>Altun et al. 2009</a></b>")
    space space space
  end
  
  block:00sD
    columns 1
    space
  end

  block:10sA
    columns 1
    D("<b><a href='Varshney_2011/'>Varshney et al.2011</a></b>") 
    G("<b><a href='Cook_2019/'>Cook et al. 2019</a></b>") 
    space
    space
  end

  block:10sB
    columns 1
    E1("<b><a href='Serrano_2013/'>Serrano-Saiz et al. 2013</a></b>") 
    E("<b><a href='Pereira_2015/'>Pereira et al. 2015</a></b>")
    E2("<b><a href='Gendrel_2016/'>Gendrel, Atlas & Hobert 2016</a></b>")
    F("<b><a href='Bentley_2016/'>Bentley et al. 2016</a></b>")
  end
  block:10sC
    columns 1
    space
  end
  block:10sD
    columns 1
    space
  end


  block:20sA
    columns 1
    I("<b><a href='Cook_2020/'>Cook et al. 2020</a></b>")
    J("<b><a href='Brittin_2021'>Brittin et al. 2021</a></b>")
    K("<b><a href='Witvliet_2021'>Witvliet et al. 2021</a></b>")
    space
  end    

  block:20sB
    columns 1
    NP("<b><a href='Ripoll_2023'>Ripoll-Sanchez et al. 2023</a></b>")
    space
    space
    space
  end    

  block:20sC
    columns 1
    L("<b><a href='Taylor_2021'>Taylor et al. 2021</a></b>")
    M("<b><a href='Yemini_2021'>Yemini et al. 2021</a></b>")
    N("<b><a href='Beets_2023'>Beets et al. 2023</a></b>")
    space
  end    
  block:20sD
    columns 1
    H("<b><a href='Fenyves_2020/'>Fenyves et al.2020</a></b>") 
    P("<b><a href='Randi_2023'>Randi et al. 2023</a></b>")
    R("<b><a href='Dag_2023'>Dag et al. 2023</a></b>")
    T("<b><a href='Atanas_2023'>Atanas et al. 2023</a></b>")
  end     

    E --> H
    E1 --> H
    E2 --> H
    E --> F
    C --> L
    L --> M
    M --> N
    A --> B
    A1 --> A
    A1 --> I
    A  --> A2
    A --> D
    B --> D
    A2 --> D
    A --> G
    A --> I
    A --> J
    A --> F
    D --> F
    A --> NP
    A1 --> NP
    F --> NP
    L --> NP
    K --> NP
    D --> NP
    A --> P
    L --> P
    N --> P
    K --> P
    NP --> P
    F --> P
    M --> R
    T --> R
    A --> R
    K --> R
    A --> T
    K --> T

  style 70sA fill:#eeeeee
  style 70sB fill:#eeeeee
  style 70sC fill:#eeeeee
  style 70sD fill:#eeeeee
  
  style 80sA fill:#dddddd
  style 80sB fill:#dddddd
  style 80sC fill:#dddddd
  style 80sD fill:#dddddd

  style 90sA fill:#cccccc
  style 90sB fill:#cccccc
  style 90sC fill:#cccccc
  style 90sD fill:#cccccc

  style 00sA fill:#bbbbbb
  style 00sB fill:#bbbbbb
  style 00sC fill:#bbbbbb
  style 00sD fill:#bbbbbb

  style 10sA fill:#aaaaaa
  style 10sB fill:#aaaaaa
  style 10sC fill:#aaaaaa
  style 10sD fill:#aaaaaa

  style 20sA fill:#999999
  style 20sB fill:#999999
  style 20sC fill:#999999
  style 20sD fill:#999999

  style A1 fill:#ff6666
  style A fill:#ff6666
  style B fill:#ff6666
  style A2 fill:#ff6666
  style D fill:#ff6666
  style J fill:#ff6666
  style K fill:#ff6666
  style G fill:#ff6666
  style I fill:#ff6666

  style E fill:#99bbff
  style E1 fill:#99bbff
  style E2 fill:#99bbff
  style F fill:#99bbff
  style NP fill:#99bbff

  style H fill:#ff80ff
  style P fill:#ff80ff
  style R fill:#ff80ff
  style T fill:#ff80ff

  style C fill:#85e085
  style L fill:#85e085
  style M fill:#85e085
  style N fill:#85e085

```

Another view on the data

```mermaid
%%{ init: { 'flowchart': { 'curve': 'stepAfter' } } }%%
flowchart TD
    classDef anat fill:#ff6666
    classDef gene fill:#85e085
    classDef es fill:#99bbff
    classDef func fill:#ff80ff


    subgraph 1970-1980
    A1["<a href='Albertson_1976/' >Albertson & Thomson 1976</a>"]:::anat
    end
    subgraph 1980-1990
    A["<a href='White_1986/' >White et al. 1986</a>"]:::anat & B["<a href='Durbin_1987/' >Durbin 1987</a>"]:::anat
    end

    subgraph 1990-2000
    A2["<a href='Hall_1991/' >Hall & Russell 1991</a>"]:::anat
    end

    subgraph 2000-2010
    C["<a href='Altun_2009/' >Altun et al. 2009</a>"]:::gene 
    end

    subgraph 2010-2020
    D["<a href='Varshney_2011/' >Varshney et al.2011</a>"]:::anat & E["<a href='Pereira_2015/' >Pereira et al. 2015</a>"]:::es & E1["<a href='Serrano_2013/' >Serrano-Saiz et al. 2013</a>"]:::es  & E2["<a href='Gendrel_2016/' >Gendrel, Atlas & Hobert 2016</a>"]:::es & F["<a href='Bentley_2016/' >Bentley et al. 2016 </a>"]:::es & G["<a href='Cook_2019/' >Cook et al. 2019</a>"]:::anat & H["<a href='Fenyves_2020/' >Fenyves et al.2020</a>"]:::func & I["<a href='Cook_2020/' >Cook et al. 2020</a>"]:::anat
    end

    subgraph 2020-2030
    J["<a href='Brittin_2021' >Brittin et al. 2021</a>"]:::anat & K["<a href='Witvliet_2021' >Witvliet et al. 2021</a>"]:::anat & L["<a href='Taylor_2021' >Taylor et al. 2021</a>"]:::gene & M["<a href='Yemini_2021' >Yemini et al. 2021</a>"]:::gene & N["<a href='Beets_2023' >Beets et al. 2023</a>"]:::gene & P["<a href='Randi_2023' >Randi et al. 2023</a>"]:::func & NP["<a href='Ripoll_2023' >Ripoll-Sanchez et al. 2023</a>"]:::es & R["<a href='Dag_2023' >Dag et al. 2023</a>"]:::func & T["<a href='Atanas_2023' >Atanas et al. 2023</a>"]:::func
    end     


    E --> H
    E1 --> H
    E2 --> H
    E --> F
    C --> L
    L --> M
    M --> N
    A --> B
    A1 --> A
    A1 --> I
    A  --> A2
    A --> D
    B --> D
    A2 --> D
    A --> G
    A --> I
    A --> J
    A --> F
    D --> F
    A --> NP
    A1 --> NP
    F --> NP
    L --> NP
    K --> NP
    D --> NP
    A --> P
    L --> P
    N --> P
    K --> P
    NP --> P
    F --> P
    M --> R
    T --> R
    A --> R
    K --> R
```

### Datasets

| Papers                                                     | Features      | Datasets |
| -------------                                              | -----         | ---- |
| [Albertson & Thomson 1976](Albertson_1976.md)     | Anatomical | N/A |
| **[White et al. 1986](White_1986.md)**     | Anatomical | **[White_A](White_A_data.md) - [White_L4](White_L4_data.md) -  [White_whole](White_whole_data.md)** |
| [Durbin 1987](Durbin_1987.md)    | Anatomical | *Work in progress: [Durbin.txt](https://github.com/dwitvliet/nature2021/blob/0646af9d25896ae660f97d462eab2d67282f5625/data/legacy_data/durbin.txt)* |
| [Hall & Russell 1991](Hall_1991.md)     | Anatomical | N/A |
| [Altun et al. 2009](Altun_2009.md)   | Gene Expression |  *Work in progress: [data](https://docs.google.com/spreadsheets/d/1Jc9pOJAce8DdcgkTgkUXafhsBQdrer2Y47zrHsxlqWg/edit?gid=283505544#gid=283505544)* |
| **[Varshney et al. 2011](Varshney_2011.md)**  | Anatomical | **[Varshney 2011](Varshney_data.md)** |
| [Pereira et al. 2015](Pereira_2015.md)  | Extrasynaptic | *Work in progress: [Cholinergic neurons](https://doi.org/10.7554/eLife.12432.003) - [NT_Map_herm](https://doi.org/10.7554/eLife.12432.009) - [WormWiring](https://doi.org/10.7554/eLife.12432.010) - [male_cholinergic](https://doi.org/10.7554/eLife.12432.016) - [transcriptional_regulators](https://doi.org/10.7554/eLife.12432.019)* |
| **[Bentley et al. 2016](Bentley_2016.md)**  | Extrasynaptic | **[Bentley et al. 2016 Monoaminergic](Bentley2016_MA_data_graph.md)** - **[Bentley et al. 2016 Peptidergic](Bentley2016_PEP_data_graph.md)** |
| **[Cook et al. 2019](Cook_2019.md)**          | Anatomical | **[Cook 2019 Hermaphrodite](Cook2019Herm_data.md)** - **[Cook 2019 Male](Cook2019Male_data.md)** |
| **[Cook et al. 2020](Cook_2020.md)**   | Anatomical | **[Cook 2020](Cook2020_data.md)**  |
| [Fenyves et al. 2020](Fenyves_2020.md)    | Functional | *Work in progress: [data](https://github.com/francescorandi/wormneuroatlas/blob/main/wormneuroatlas/data/journal.pcbi.1007974.s003.xlsx)*   |
| **[Brittin et al. 2021](Brittin_2021.md)**    | Anatomical | **[Brittin et al. 2021](Brittin2021_data.md)**  |
| [Taylor et al. 2021](Taylor_2021.md)    | Gene Expression | *Work in progress: [data](https://github.com/cengenproject/CeNGEN_integrated_analysis_biorxiv_code)* |
| [Yemini et al. 2021](Yemini_2021.md)    | Gene Expression | *Work in progress: [data](https://zenodo.org/records/3906530)* |
| **[Witvliet et al. 2021](Witvliet_2021.md)**  | Developmental | **[Witvliet1](Witvliet1_data.md)** - **[Witvliet2](Witvliet2_data.md)** - **[Witvliet3](Witvliet3_data.md)** - **[Witvliet4](Witvliet4_data.md)** - **[Witvliet5](Witvliet5_data.md)** - **[Witvliet6](Witvliet6_data.md)** - **[Witvliet7](Witvliet7_data.md)** - **[Witvliet8](Witvliet8_data.md)**|
| [Beets et al. 2023](Beets_2023.md)    | Gene Expression | *Work in progress: [data](https://github.com/cengenproject/CeNGEN_integrated_analysis_biorxiv_code)* |
| [Dag et al. 2023](Dag_2023.md)    | Functional | N/A  |
| [Atanas et al. 2023](Atanas_2023.md)    | Functional | *Work in progress: [data](https://www.wormwideweb.org/dataset.html)* |
| **[Randi et al. 2023](Randi_2023.md)**    | Functional | **[WormNeuroAtlas: anatomical](WormNeuroAtlas_data.md)** -  **[WormNeuroAtlas: functional](Randi2023_data_graph.md)**  |
| **[Ripoll-Sanchez et al. 2023](RipollSanchez_2023.md)**    | Extrasynaptic | **[Ripoll-Sánchez 2023 (short)](RipollSanchezShortRange_data.md) - [Ripoll-Sánchez 2023 (mid)](RipollSanchezMidRange_data.md) - [Ripoll-Sánchez 2023 (long)](RipollSanchezLongRange_data.md)**   |



