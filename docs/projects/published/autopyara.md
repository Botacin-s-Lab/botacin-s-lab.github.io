---
title: AutoPYara
---

# AutoPYara

**Next-gen YARA rule generation for malware family clustering.**

[YARA](https://virustotal.github.io/yara/) rules are the pattern files that antivirus and security tools use to detect malware. AutoPYara writes them automatically by looking at a whole family of related samples at once instead of one sample at a time. Patterns shared across the family produce more accurate rules than tools that inspect samples individually.

## Paper

> Mabon Ninan\*, Nhat Minh Nguyen\*, Soumyajyoti Dutta, Sidharth Anil, and Marcus Botacin. **AutoPYara: Next-Gen YARA Rule Generator for Malware Family Clustering.** *Annual Computer Security Applications Conference (ACSAC), 2026. To appear.* \*Equal contribution.

```bibtex
@inproceedings{autopyara2026,
  title     = {AutoPYara: Next-Gen YARA Rule Generator for Malware Family Clustering},
  author    = {Ninan, Mabon and Nguyen, Nhat Minh and Dutta, Soumyajyoti and Anil, Sidharth and Botacin, Marcus},
  booktitle = {Proceedings of the Annual Computer Security Applications Conference (ACSAC)},
  year      = {2026},
  note      = {To appear. Ninan and Nguyen contributed equally.}
}
```

The artifact seeks the ACSAC **Available**, **Functional** and **Reproduced** badges.

## Everything in one place

<div class="feature-grid" markdown>

<div markdown>
### :material-language-python: Python package
`pip install autopyara`. The tool itself, with an API and command-line entry points.

[PyPI](https://pypi.org/project/autopyara/) · [GitHub](https://github.com/Botacin-s-Lab/AutoPYaraPyPI)
</div>

<div markdown>
### :material-book-open-variant: Documentation
Installation, quick start, API reference and architecture.

[Read the docs](https://botacin-s-lab.github.io/AutoPYaraPyPI/)
</div>

<div markdown>
### :material-language-java: Java backend
The JVM engine: byte n-gram extraction, Bloom-filter isolation, biclustering and YARA rule synthesis. Derived from [AutoYara](https://github.com/FutureComputing4AI/AutoYara) (Apache 2.0).

[GitHub](https://github.com/Botacin-s-Lab/AutoPYaraBackend)
</div>

<div markdown>
### :material-flask-outline: Reproducibility artifact
Install the tool, run it on safe synthetic data, and regenerate every number and figure in the paper.

[GitHub](https://github.com/Botacin-s-Lab/AutoPYara)
</div>

<div markdown>
### :material-database: Evaluation data
Rules and recorded results used in the paper, archived on Zenodo. The malware corpus itself cannot be redistributed for legal and ethical reasons.

[10.5281/zenodo.22665898](https://doi.org/10.5281/zenodo.22665898)
</div>

</div>

## Try it

```bash
pip install autopyara
```

To reproduce the paper's results:

```bash
git clone https://github.com/Botacin-s-Lab/AutoPYara.git
cd AutoPYara
./install.sh                                     # one-time setup, ~10-25 minutes
./claims/claim1_install/run.sh                    # the tool installs and runs
./claims/claim4_incorrect_baselines/run.sh -j 8   # reproduce a paper figure
```

Both checks print `PASS` or `FAIL`. The artifact README also describes a Docker option that needs nothing else installed.

## How the pieces fit

| Repository | Language | Role |
|---|---|---|
| [AutoPYaraPyPI](https://github.com/Botacin-s-Lab/AutoPYaraPyPI) | Python | Public package. ssdeep and DBSCAN pre-clustering happen here. Embeds the built backend jar and drives it over JPype. |
| [AutoPYaraBackend](https://github.com/Botacin-s-Lab/AutoPYaraBackend) | Java 11 | Builds `AutoYara.jar`. Not used directly by end users. |
| [AutoPYara](https://github.com/Botacin-s-Lab/AutoPYara) | Shell, Python | Artifact: install scripts, claim checks and figure regeneration. |

## Team

Mabon Ninan, Nhat Minh Nguyen, Soumyajyoti Dutta, Sidharth Anil and Marcus Botacin, Texas A&M University. The Python package and documentation are maintained by Mabon Ninan.

## License

Code is released under the MIT license. The backend keeps the Apache 2.0 license on the files it derives from AutoYara.
