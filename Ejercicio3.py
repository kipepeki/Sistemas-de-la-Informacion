import sqlite3
import pandas as pd
from matplotlib import pyplot as plt

con = sqlite3.connect('database.db')
cur = con.cursor()

