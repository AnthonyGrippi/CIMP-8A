import locale as lc

# Set the locale
result = lc.setlocale(lc.LC_ALL, "")    # Windows
if result[0] == "C":
    lc.setlocale(lc.LC_ALL, "en_US")    # Mac OS X

# Display currency
print(lc.currency(12345.67, grouping=True))

# Display integer
print(lc.format_string("%d", 12345, grouping=True))

# Display float
print(lc.format_string("%.2f", 12345.67, grouping=True))