# rearrange dict by value as list
x = {123: ['Ahmed', 'Active', 12000.0],
     125: ['Ali', 'closed', 0.0],
     255: ['Anwar', 'Active', 15000.0],
     983: ['Sami', 'Active', 8000.0],
     333: ['Mushtaq', 'Active', 20000.0],
     963: ['Saif', 'Active', 10000.0]
     }

print({k: v for k, v in sorted(
    x.items(), key=lambda item: item[1][2], reverse=True)})
