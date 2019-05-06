---
title: "Reproducible research: A case study of Cantonese intonation"
author: 葛淳宇
theme: Berkeley
colortheme: beaver
mainfont: "STSong"
---

# Introduction

## Reproducible research

*Definition*:

> "Reproducible research is the capacity of repeating an experiment in any place with any person."
> 
> "Same data + same script = same results" ([Daniel, 2016](https://www.r-bloggers.com/what-is-reproducible-research/))

. . .

**Keywords**:

- Scientific ethics;
- Reproducibility.

## Basic stages and common tasks in phonetic researches

:::::: {.columns}
::: {.column width="45%"}
Basic stages:

![](./workflow.png)
:::

::: {.column width="55%"}
### Common tasks:

- Reference management;
- Note-taking;
- File management;
- Data backup;
- Annotation and measurement;
- Statistical analyses;
- Visualisation;
- Typesetting;
- Reference generation with various styles.
:::
::::::

## Tools and what they can do

- [Zotero](www.zotero.org) (generates [*Bibtex*](www.bibtex.org) files): reference management;
- Markdown: note-taking and writing in plain text;
- [Pandoc](www.pandoc.org): transforming *markdown* files to *pdf*, *docx*, *beamer*, etc;
- Praat and praat scripting: annotation and measurements;
- Shell: common file management and text tasks;
- Python: complex tasks and data analyses;
- R: statistical analyses and visualization.

### An alternative
`Rmarkdown`:

- Statistical analyses, visualization, writing and typesetting in one place.

## The essential of reproducible research

**Plain text**:

- Cross-platform compatibility:
    + Viewing and editing in any text editor, even the *Notepad* in *Windows*;
- Keeping track of the modifications:
    + Version control.

# A case study of Cantonese intonation

## Tone and intonation in Cantonese
- Six lexical tone categories:
    + three checked tones included in the corresponding unchecked level tones;
- High boundary tone in yes-no questions.

------------    -------  ---------
 tones           values   symbols
------------    -------  ---------
 Yinping           55 \      T1 \
 Yangping          21 \      T2 \
 Yinshang          35 \      T3 \
 Yangshang         13 \      T4 \
 Yinqu             33 \      T5 \
 Yangqu            22        T6
-----------     -------  ---------

## Cantonese intonation

### Research question
Can Cantonese lexical tone categories still be distinct under the influence of the H boundary tone?

. . .

### Previous studies
- T1 and T5 can be identified with high accuracy, a large portion of T2, T4, and T6 are misperceived as T3 (Ma et al. 2007);
- the pairs T3 and T4, T3 and T6, T4 and T6 are hard to discriminate (Mai, 2000).

. . .

### Our approach
Functional Data Analysis (FDA)

## Data management
- Maintain appropriate and **human-readable** folder structures;
- Keep detailed documentation.

## Functional Data Analysis (FDA)

:::::: {.columns}
::: {.column width=55%}
FDA:

- uses B-spline functions to model curves; 
- the smoothed curves submitted to functional principal component analysis (FPCA).
:::

::: {.column width=45%}
The workflow of FDA:
![](./fda.png)
:::
::::::

## Data preparation
The pitch curves of the last syllables in the yes-no questions are used.

### Praat
- TextGrid files;
- PitchTier files.

### Python
- `metadata.py`: extracts the metadata of the pitch files;
- `toPitch.py`: converts PitchTier files to Pitch objects;
- `extractPitch.py`: extracts the pitch curves of the last syllables.

## Results
The pitch curves of the last syllables:

:::::: {.columns}
::: {.column width="70%"}
![](./final_q.png)
:::
::: {.column width="30%"}
:::
::::::

## FDA results
The distributions of PC1 and PC2:

:::::: {.columns}
::: {.column width="50%"}
![](./PC1.png)
:::
::: {.column width="50%"}
![](./PC2.png)
:::
::::::

## The distributions of six tones in the $PC1 \times PC2$ plane

:::::: {.columns}
::: {.column width="50%"}
![](./pc1-pc2.png)
:::
::: {.column width="50%"}

- T1 and T5 cluster together, respectively;
- T2, T3, and T4 overlap to a great degree;
- Yet the distributions are quite dispersed.
:::
::::::

# Introspection

## Two big challenges in phonetic researches

- Experimental designs and experimental practices makes results less replicable:
  + especially in prosodic researches, where speakers often fail to pronounce the speech material in the intended manner;
- Lack of clear guidelines for speech annotation:
  + Prevalent coarticulation;
  + No clear boundary between segments.

## The nature of these two challenges

- Lab speech vs. spontaneous speech;
- Linearity of phonetic symbols vs. simultaneity of speech.

# Conclusions

## Many facets of reproducible research

### Advantages of reproducible research
- Makes the research reproducible both to yourself and to other researchers;
- Keeps the research (and most importantly, the mind) organized;
- Makes research/life easier.

. . .

### Disadvantages of reproducible research
- Technically complex;
- Steep learning curve;
- Distracting from research.

. . .

### Caveats

- Pay attention to experimental designs and experimental practices;
- Concentrate on research itself!