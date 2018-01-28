# vim: set filetype=python ts=2 sw=2 sts=2 expandtab: 
"""
Reads N csv into a set of dictionaries (one per file).

Each csv file has a set of named fields in line one.
Files get converted into dictionary, one per line,
with index 'id' (so line one of the file needs to name one
column 'id').

Each line gets converted into a dictionary of field:value
where 'field' is a label from line one and 'value' comes
from the current line.

If a line has a missing field, it takes it from the line above
(useful for lots of lines with same values).

"""
##########################################################
head="""

[home](http://tiny.cc/sbse) |
[models](xx) |
[data](xx) |
[discuss](https://github.com/ai-se/ResourcesDataDrivenSBSE/issues) |
[citation](https://github.com/ai-se/ResourcesDataDrivenSBSE/blob/master/CITATION.md) |
[copyright](https://github.com/ai-se/ResourcesDataDrivenSBSE/blob/master/LICENSE.md) &copy;2018
<br>
[<img width=900 src="https://github.com/ai-se/ResourcesDataDrivenSBSE/raw/master/img/banner.png">](http://tiny.cc/sbse)<br>



<em>(This is an auto-generated file. Do not edit.  To modify, please
use pull requests on [these 
files](https://github.com/ai-se/ResourcesDataDrivenSBSE/tree/master/data)).</em>


 [![DOI](https://zenodo.org/badge/116411075.svg)](https://zenodo.org/badge/latestdoi/116411075)


"""
##########################################################
tail="""

## License

[![CC0](http://mirrors.creativecommons.org/presskit/buttons/88x31/svg/cc-zero.svg)](https://creativecommons.org/publicdomain/zero/1.0/)

To the extent possible under law, we waive all copyright and related or neighboring rights to this work.

"""
##########################################################

import os,re,sys
sys.dont_write_bytecode = True

def go(f): f();return f

def nfields(n):
    one='([^,]*)'
    return ','.join([one for _ in range(n)])

def groups(n,str):
  r = nfields(n)
  print(r)
  p = re.compile(nfields(n))
  m = p.match(str)
  if m:
    return [s.strip() for s in m.groups()]

def f1():
  print(groups(3,"asdas,,"))

class o:
   def __init__(i, entries) : i.__dict__.update(entries)
   def __repr__(i)          : return 'o{' + str(i.__dict__) + '}'
   def __getitem__(i, x)    : return i.__dict__[x]

def sorted(lst):
  lst.sort()
  return lst

def lines(file):
  """return a dictionary, one per line. keys are defined as per line1.
     if line1 is missing a field, we grab it from the line above"""
  head,last=None,None
  with open(file + ".csv") as f:
    for line in f.readlines():
      cells = [x.strip() for x in line.split(",")]
      if not head:
        head = cells
      else:
        assert len(cells) == len(head),'bad line: %s' % line
        if last:
          cells = [cells[j] or last[j] for j in range(len(head))]
        yield o( {head[j]:cells[j] for  j in range(len(head))} )
        last = cells

def reader(file):
  ds={}
  for d in lines(file):
    assert d.id not in ds,'repeated key %s' % d.id
    ds[d.id] = d
  return ds

def writer(f,fun,*lst):
  dir='../var'
  if not os.path.exists(dir):
    os.makedirs(dir)
  with open(dir + '/' + f + '.md','w') as g:
    g.write(head)
    fun(lambda x:g.write(x), *lst)
    g.write(tail)

def ids(d):
  for x in sorted([y for y in d.keys()]):
    yield x,d[x]

##########################################################

def h1(x)     : return "\n\n# %s"  % x
def h2(x)     : return "\n\n## %s" % x
def h3(x)     : return "\n\n#W# "  % x
def pp(x)     : return "\n\n%s"    % x
def url(a,b)  : return "[%s](%s)" % (str(a),str(b))
def urlof(x,a): return url( a[x].details, a[x].url )

def writePubs(write,p,a,w):
  write( h1("Pubs") )
  for _,d in ids(p):
    write( "%s%s" % ( 
      h2(d.when + ": " + d.id),
      pp( urlof(d.where, a))
    ))

#---------------------
p = reader("pubs")
a = reader("about")
w = reader("what")

writer('pubs',writePubs,p,a,w)

