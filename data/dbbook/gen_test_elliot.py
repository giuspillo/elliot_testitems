#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  2 18:17:29 2023

@author: giuse
"""

# apri il file di input
with open("test2id.tsv", "r", encoding="utf-8") as input_file:
    # apri il file di output
    with open("test2id_elliot.tsv", "w", encoding="utf-8") as output_file:
        # per ogni riga del file di input
        for line in input_file:
            # dividi la riga in base al carattere di tabulazione
            user, item, rating = line.strip().split("\t")
            # se il rating è "1"
            if rating == "1":
                # scrivi la tripla nel file di output
                output_file.write(line)
                
