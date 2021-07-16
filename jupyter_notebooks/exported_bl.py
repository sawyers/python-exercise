# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %% [markdown]
# Business rules to follow:
#
# 1. A hardcoded list is supplied with a - c business units. The central database is expected to be in a maintenance window when the script is run
# 1. For each unit, assign a value of 5 multipled by the letter place in the alphabet. This is for accounting reasons, see Bob (bob@example.com) for more details
# 1. Print out the unit and the value

# %%
import string

units = list(map(chr, range(97, 100)))

for i in units:
    print(f"Unit: {i}, Value: {string.ascii_lowercase.index(i) + 1}")
