from Bio import Entrez
from urllib.request import urlretrieve

# Set your email address to identify yourself to NCBI
Entrez.email = "your.email@example.com"

# Set the list of accession numbers for the genomes you want to download
accession_numbers = ["NC_000852", "NC_007346", "NC_008724"]

# Use the Entrez.efetch function to download the records in GenBank format
for accession in accession_numbers:
    handle = Entrez.efetch(db="nuccore", id=accession, rettype="gb", retmode="text")
    filename = f"{accession}.gb"
    urlretrieve(url=handle.url, filename=filename)
