# ENTROPY_PDOS

1) `mkdir` folders named with the supercells you would like to study.
e.g. in `TEST`, there is:

```
1_times_landau_supercell
2_times_landau_supercell
3_times_landau_supercell
4_times_landau_supercell
```

2) Place in each of these folders the `*.out` for the phonon dispersion calculation,


and the `*PHONDOS`:

3) `cd` to each folder and run `extract_freqs.py`. This will extract all the frecuencies at all k-points and will generate a file, `All_freq.dat`, with
all the frequencies sorted

4) Edit `Entropy_pdos.py` by indicating the path for each folder.


