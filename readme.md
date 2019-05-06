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
pandoc: /Users/chunyu/Desktop/workflow.png: openBinaryFile: does not exist (No such file or directory)
```

The two files included in the `figs` folder can be used to generate the first two figures. You may try to generate these figures by yourself using [R](https://www.r-project.org/) with the [DiagrammeR](https://cran.r-project.org/web/packages/DiagrammeR/index.html) package or [Mermaid](https://mermaidjs.github.io/). You can contact the author for the other figures. The analyses of Cantonese intonation using FDA relies heavily on the work by [Michele Gubian](https://github.com/uasolo/FDA-DH/). Thus, the codes for data analyses are not uploaded to the repo.
