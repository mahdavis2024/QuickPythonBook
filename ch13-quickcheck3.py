'''Quick Check: Pickles
Think about why a pickle would or would not be a good solution in the following use
cases:
1- Saving some state variables from one run to the next
2- Keeping a higg-score list for a game
3- Storing usernames and passwords
4- Storing a large dictionary of English terms
'''

# 1- it is doable but time-consuming and memory-guzzling.
# 2- it is a good use but still can be accessed by malicious actors and changed.
# 3- it is not secure to store credentials this way.
# 4- it does not make sense to dump and load the dictionary each time we want to look up a term.