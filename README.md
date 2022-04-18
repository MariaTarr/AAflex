#ESTENO v.1.0

Esteno is a non-machine learning approach to assess the flexibility all the residues residues in a protein.


##0. Install Esteno:

The source code can be downloaded from #github link#.
Installation is executed with thw following command:

```{.sh}
pip3 install Esteno-1.0.tar.gz
```

##1. Command line version

This can be run in the command line using:

```{.sh}
Esteno <fasta>
```

##2. Graphical interface version

The graphical interface is displayed using the command:

```{.sh}
RunEsteno
```
To run the analysis, copy-paste the protein sequence in the box and press the button "Send".

In this version a graphical visualization of the obtained score is displayed in the interface (it is also saved in .png format, see section 3).

Last results can be revisited  by clicking on "Proggramme" > "Results"

##3. Output files

The programme gives two main outputs:

* Scores table: .csv file containing the numerical score (in a range 0-2) for each residue in the given protein.
* Scores sequence: .txt file containing the sequence and the numerical score as a string.
* Scores visualisation: Image in .png format.

Other files are also produced during the process:
* The PAE matrix is saved with the swissprot protein ID name in xml format.


All files mentioned above are automatically saved in the working directory.
