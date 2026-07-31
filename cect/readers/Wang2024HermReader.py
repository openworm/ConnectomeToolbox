# -*- coding: utf-8 -*-

############################################################

#    A script to read the neurotransmitter atlas values from Wang et al. 2024.

############################################################


from cect.readers.Wang2024Reader import Wang2024Reader
from cect.ConnectomeDataset import LOAD_READERS_FROM_CACHE_BY_DEFAULT

NAME = "Wang2024Herm"

READER_DESCRIPTION = "???"

DATASET_DESCRIPTION = "This dataset for the hermaphrodite _C. elegans_ contains neurotransmitter expression values from: Wang et al. 2024 with basic anatomical connectivity information from Cook et al. 2019, and monoaminergic receptor expression information from Bentley et al. 2016"

WEIGHTS = "A weight of 1 indicates that the cell expresses the specific neurotransmitter, in addition to an anatomical connection between the pre- and post-synaptic cells (for Glutamate, Acetylcholine, GABA, Betaine), or (for Dopamine, Serotonin, Tyramine, Octopamine) a connection between a monoaminergic receptor-expressing cell and a monoaminergic cell according to Bentley et al. 2016."


def get_instance(from_cache=LOAD_READERS_FROM_CACHE_BY_DEFAULT):
    if from_cache:
        from cect.ConnectomeDataset import (
            load_connectome_dataset_file,
            get_cache_filename,
        )

        return load_connectome_dataset_file(get_cache_filename(__name__.split(".")[-1]))
    else:
        global READER_DESCRIPTION
        inst = Wang2024Reader(sex="Hermaphrodite")
        READER_DESCRIPTION = inst.reader_description
        return inst


def main():
    tdr_instance = get_instance(from_cache=False)

    print(tdr_instance.summary(list_pre_cells=True))
    print(tdr_instance.reader_description)
    quit()


if __name__ == "__main__":
    main()
