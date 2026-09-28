Data was taken from Cook et al. 2020, The connectome of the Caenorhabditis elegans pharynx, [J Comp Neurol. 2020; 528: 2767–2784](https://onlinelibrary.wiley.com/doi/10.1002/cne.24932).

The connectivity data were released in 2 CSV files in the supplementary information for that paper:

- [cne24932-sup-0004-Supinfo4.csv](https://onlinelibrary.wiley.com/action/downloadSupplement?doi=10.1002%2Fcne.24932&file=cne24932-sup-0004-Supinfo4.csv) described as "Complete edge list for pharyngeal reconstruction."

- [cne24932-sup-0005-Supinfo5.csv](https://onlinelibrary.wiley.com/action/downloadSupplement?doi=10.1002%2Fcne.24932&file=cne24932-sup-0005-Supinfo5.csv) described as "Inferred gap junction connectivity between end-organs". These connections are included and some of these are tested below. 

These files were opened in Apple Numbers, and the weights (numbers of connections between pairs of cells, electrical or chemical) were read off, to provide checks listed below. 

**Validation issue: Repeated connections**

There were multiple entries in [cne24932-sup-0004-Supinfo4.csv](https://onlinelibrary.wiley.com/action/downloadSupplement?doi=10.1002%2Fcne.24932&file=cne24932-sup-0004-Supinfo4.csv) for the same pair of cells and the same type of connection. Where there are multiple lines of this type, the weights in the new line have been added to (summed with) the existing weight. 

This is a summary of the connections which were repeated: 

> Existing connection at (14,14) (M4->M4, Chemical), was: 15.0, new conn weight: 15.0, appended weight is: 30.000000
>
> Existing connection at (17,30) (I4->NSMR, Chemical), was: 2.0, new conn weight: 13.5, appended weight is: 15.500000
>
> Existing connection at (37,15) (NSML->pm5D, Chemical), was: 29.0, new conn weight: 9.0, appended weight is: 38.000000
>
> Existing connection at (30,31) (NSMR->bm, Chemical), was: 50.0, new conn weight: 11.0, appended weight is: 61.000000
>
> Existing connection at (30,15) (NSMR->pm5D, Chemical), was: 1.0, new conn weight: 8.5, appended weight is: 9.500000
>
> Existing connection at (30,32) (NSMR->M3R, Chemical), was: 15.0, new conn weight: 7.5, appended weight is: 22.500000
>
> Existing connection at (37,18) (NSML->pm5VL, Chemical), was: 58.0, new conn weight: 5.0, appended weight is: 63.000000
>
> Existing connection at (17,18) (I4->pm5VL, Chemical), was: 6.0, new conn weight: 4.5, appended weight is: 10.500000
>
> Existing connection at (37,31) (NSML->bm, Chemical), was: 78.0, new conn weight: 5.0, appended weight is: 83.000000
>
> Existing connection at (17,34) (I4->M2L, Chemical), was: 1.0, new conn weight: 4.0, appended weight is: 5.000000
>
> Existing connection at (32,8) (M3R->g1AR, Chemical), was: 1.0, new conn weight: 1.5, appended weight is: 2.500000
>
> Existing connection at (6,14) (I5->M4, Chemical), was: 8.0, new conn weight: 18.5, appended weight is: 26.500000
>
> Existing connection at (6,30) (I5->NSMR, Chemical), was: 3.0, new conn weight: 17.5, appended weight is: 20.500000
>
> Existing connection at (37,16) (NSML->pm5VR, Chemical), was: 3.0, new conn weight: 7.0, appended weight is: 10.000000
>
> Existing connection at (37,38) (NSML->M3L, Chemical), was: 14.0, new conn weight: 6.5, appended weight is: 20.500000
>
> Existing connection at (6,16) (I5->pm5VR, Chemical), was: 8.0, new conn weight: 3.5, appended weight is: 11.500000
>
> Existing connection at (25,41) (I1R->I2R, Chemical), was: 5.0, new conn weight: 3.0, appended weight is: 8.000000
>
> Existing connection at (9,15) (M1->pm5D, Chemical), was: 3.0, new conn weight: 1.0, appended weight is: 4.000000
>
> Existing connection at (6,8) (I5->g1AR, Chemical), was: 4.0, new conn weight: 1.0, appended weight is: 5.000000
>
> Existing connection at (6,7) (I5->g1AL, Chemical), was: 7.0, new conn weight: 1.0, appended weight is: 8.000000
>
> Existing connection at (33,27) (I1L->I2L, Chemical), was: 10.0, new conn weight: 1.0, appended weight is: 11.000000
>
> Existing connection at (14,6) (M4->I5, Chemical), was: 1.0, new conn weight: 0.5, appended weight is: 1.500000
>
> Existing connection at (36,14) (I6->M4, Chemical), was: 3.0, new conn weight: 9.5, appended weight is: 12.500000
>
> Existing connection at (36,37) (I6->NSML, Chemical), was: 13.0, new conn weight: 8.0, appended weight is: 21.000000
>
> Existing connection at (35,16) (M2R->pm5VR, Chemical), was: 9.0, new conn weight: 3.0, appended weight is: 12.000000
>
> Existing connection at (34,7) (M2L->g1AL, Chemical), was: 2.0, new conn weight: 3.0, appended weight is: 5.000000
>
> Existing connection at (42,43) (MCL->mc2V, Chemical), was: 10.0, new conn weight: 2.5, appended weight is: 12.500000
>
> Existing connection at (9,23) (M1->I3, Chemical), was: 6.0, new conn weight: 1.0, appended weight is: 7.000000
>
> Existing connection at (9,27) (M1->I2L, Chemical), was: 2.0, new conn weight: 1.0, appended weight is: 3.000000
>
> Existing connection at (25,9) (I1R->M1, Chemical), was: 2.0, new conn weight: 1.0, appended weight is: 3.000000
>
> Existing connection at (25,23) (I1R->I3, Chemical), was: 5.0, new conn weight: 1.0, appended weight is: 6.000000
>
> Existing connection at (32,14) (M3R->M4, Chemical), was: 1.0, new conn weight: 1.0, appended weight is: 2.000000
>
> Existing connection at (36,30) (I6->NSMR, Chemical), was: 3.0, new conn weight: 1.0, appended weight is: 4.000000
>
> Existing connection at (36,15) (I6->pm5D, Chemical), was: 14.0, new conn weight: 1.0, appended weight is: 15.000000
>
> Existing connection at (14,17) (M4->I4, Chemical), was: 4.0, new conn weight: 0.5, appended weight is: 4.500000
>
> Existing connection at (9,19) (M1->g1P, Chemical), was: 4.0, new conn weight: 0.5, appended weight is: 4.500000
>
> Existing connection at (0,0) (M5->M5, GapJunction), was: 1.0, new conn weight: 1.0, appended weight is: 2.000000
>
> Existing connection at (14,14) (M4->M4, GapJunction), was: 1.0, new conn weight: 1.0, appended weight is: 2.000000
>
> Existing connection at (60,49) (mc1DR->pm4VR, GapJunction), was: 3.0, new conn weight: 3.0, appended weight is: 6.000000
>
> Existing connection at (49,60) (pm4VR->mc1DR, GapJunction), was: 3.0, new conn weight: 3.0, appended weight is: 6.000000