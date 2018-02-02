from __future__ import print_function
from glob2 import glob
import pandas as pd
import os
from pdb import set_trace

head = """

[home](http://tiny.cc/sbse) |
[tools](TOOLS.md) |
[data](DATA.md) |
[discuss](https://github.com/ai-se/ResourcesDataDrivenSBSE/issues) |
[citation](https://github.com/ai-se/ResourcesDataDrivenSBSE/blob/master/CITATION.md) |
[copyright](https://github.com/ai-se/ResourcesDataDrivenSBSE/blob/master/LICENSE.md) &copy;2018
<br>
[<img width=900 src="https://github.com/ai-se/ResourcesDataDrivenSBSE/raw/master/img/banner.png">](http://tiny.cc/sbse)<br>


 [![DOI](https://zenodo.org/badge/116411075.svg)](https://zenodo.org/badge/latestdoi/116411075)


"""

print(head)
file = os.path.abspath("../var/tools.csv")
csv = pd.read_csv(file)

columns = csv.columns
row_sep = pd.DataFrame([["---" for col in columns]], columns=columns)

csv = pd.concat([row_sep, csv])

print(csv.to_csv(path_or_buf=None, sep="|", index=False))

tail = """

## License

[![CC0](http://mirrors.creativecommons.org/presskit/buttons/88x31/svg/cc-zero.svg)](https://creativecommons.org/publicdomain/zero/1.0/)

To the extent possible under law, we waive all copyright and related or neighboring rights to this work.

"""

print(tail)
