# Reproducible research: A demonstration

This is a repository which stores a presentation on reproducible research with a case study of Cantonese intonation. The materials were presented in Lab of Phonetics and Speech Science, Institute of Linguistics, CASS, on 7th May, 2019.

The file `rr.md` is the presentation file. The presentation was written in *markdown*, and the presentation was generated using `pandoc`. The folder `figs` contains two files, `workflow.mmd` and `fda.mmd`, which generates flow charts of the workflows of phonetic research and FDA, respectively. The two flow charts were written in `mermaid`. The scrips folder contains three data preparation scripts written in `Python`.

The presentation file `rr.md` can be compiled using [Pandoc](http://pandoc.org/). Type the following commands in the terminal (or `cmd`/`PowerShell` in `Windows`):

```bash
git clone https://github.com/ge-chunyu/RR-Cantonese
cd RR-Cantonese
pandoc -t beamer --pdf-engine=xelatex rr.md -o rr.pdf 
```

You will  receive the following warning:

```bash
[WARNING] Could not fetch resource './workflow.png': replacing image with description
[WARNING] Could not fetch resource './fda.png': replacing image with description
[WARNING] Could not fetch resource './final_q.png': replacing image with description
[WARNING] Could not fetch resource './PC1.png': replacing image with description
[WARNING] Could not fetch resource './PC2.png': replacing image with description
[WARNING] Could not fetch resource './pc1-pc2.png': replacing image with description
```

The two files included in the `figs` folder can be used to generate the first two figures. You may try to generate these figures by yourself using [R](https://www.r-project.org/) with the [DiagrammeR](https://cran.r-project.org/web/packages/DiagrammeR/index.html) package or [Mermaid](https://mermaidjs.github.io/). You can download all the figures on [my Dropbox](https://www.dropbox.com/sh/gc3s2wke2i6ts83/AACPOz2GrZdE30Qvd9utybO1a?dl=0). Put the figures in the `RR-Cantonese` folder and rerun the code will get the same presentation file as I did. Note that `LaTeX` is also required to generate `beamer` files.

The analyses of Cantonese intonation using FDA relies heavily on the work by [Michele Gubian](https://github.com/uasolo/FDA-DH/). Thus, the codes for data analyses are not uploaded to the repo.
