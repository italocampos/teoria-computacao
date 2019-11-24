from pdautomata import PDAutomata
from tools import *

G = read_from_file('grammar.in')
auto = PDAutomata(G)
