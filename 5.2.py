lst = ['q', 'w', 'e', 'r', 't', 'y']
for i, char in enumerate(lst):
    print(f"Element: {char}, Positive Index: {i}, Negative Index: {-(len(lst) - i)}")
