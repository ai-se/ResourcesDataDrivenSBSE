# vim: set filetype=python ts=2 sw=2 sts=2 expandtab: 
import re,sys
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

# @go
def f1():
  print(groups(3,"asdas,,"))

class o:
   def __init__(i, entries): i.__dict__.update(entries)
   def __repr__(i) : return 'o{' + str(i.__dict__) + '}'

def lines(file):
  head,last=None,None
  with open(file) as f:
    for line in f.readlines():
      cells = [x.strip() for x in line.split(",")]
      if not head:
        head = cells
      else:
        if len(cells) == len(head):
          if last:
            cells = [cells[j] if cells[j] else last[j] for j in range(len(head))]
          yield o( {head[j]:cells[j] for  j in range(len(head))} )
          last = cells
        else:
          print("bad line:",line)

@go
def lines1():
  for n,line in enumerate( lines("pubs.csv") ):
    print(n,line.about)


