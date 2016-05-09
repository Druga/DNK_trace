# This Python file uses the following  encoding: utf-8
#1 poišči pravo barvo las
Substance = open("dna.txt", "r").read()

Suspect_Ziga = "TGCAGGAACTTCAAAACCTCATTAGCTATCGCGCCAGTGCCGACCACAA"
Suspect_Matej = "TGCAGGAACTTCAAAACCTCACCAGCAATCGCTTGTGGTGGCAGGCCTCA"
Suspect_Miha = "TGCAGGAACTTCAAAACCTCAGCCAGTGCCGGGGAGGTGGCGCCACGG"

if Suspect_Ziga.find("TGCAGGAACTTCAAAACCTCATTAGCTATCGCGCCAGTGCCGACCACAA"):
    print "Žiga je kriv"

if Suspect_Matej.find("TGCAGGAACTTCAAAACCTCACCAGCAATCGCTTGTGGTGGCAGGCCTCA"):
    print "Matej je kriv"

if Suspect_Miha.find("TGCAGGAACTTCAAAACCTCAGCCAGTGCCGGGGAGGTGGCGCCACGG"):
    print "Miha je kriv"