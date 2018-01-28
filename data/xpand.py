# vim: set filetype=python ts=2 sw=2 sts=2 expandtab: 
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
        if len(cells) == len(head):
          if last:
            cells = [cells[j] if cells[j] else last[j] for j in range(len(head))]
          yield o( {head[j]:cells[j] for  j in range(len(head))} )
          last = cells
        else:
          print("bad line:",line)

def file2dict(file):
  ds={}
  for d in lines(file):
    ds[d.id] = d
  return ds

def main():
  def writer(f,fun):
    dir='../var'
    if not os.path.exists(dir):
      os.makedirs(dir)
    with open(dir + '/' + f + '.md','w') as g:
      fun(lambda x:g.write(x), p,a,w)
  p,a,w = pubs(), about(), what()
  writer('pubs',writePubs)

# -----------------------------------------------------

def pubs() : return file2dict("pubs")
def about() : return file2dict("about")
def what() : return file2dict("what")

def h1(x)     : return "\n\n# %s"  % x
def h2(x)     : return "\n\n## %s" % x
def h3(x)     : return "\n\n#W# "  % x
def pp(x)     : return "\n\n%s"    % x
def url(a,b)  : return "[%s](%s)" % (str(a),str(b))
def urlof(x,a): return url( a[x].details, a[x].url )

def writePubs(write,p,a,w):
  write( h1("Pubs") )
  for x in sorted([y for y in p.keys()]):
    d = p[x]
    write( h2(d.when + ": " + d.id) )
    write( pp( urlof(d.where, a ) ) )

main()

