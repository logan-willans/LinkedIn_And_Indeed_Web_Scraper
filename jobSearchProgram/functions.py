# Sanitizes the keyword the user enters. Makes is usable in the search string.
def sanitizeString(string):
    numSpaces = 0
    string = string.strip()
    string = string.lower()
    for letter in string:
        if letter == ' ':
            numSpaces += 1
    return string.replace(" ", "%20", numSpaces)

# Sort job by leading integer values. Only works if job wasn't posted "just now". Haven't yet figured out how to handle that.
# Also, sorting by "posted x hours ago" and "posted x minutes ago" is difficult.
def sortJobPostingsByLeadingInt(job_posting):
    return int(job_posting.time_posted[0:2])

def printResults(site_name, arr1, arr2):
    print("\n")
    print("--------------------------------")
    print("HERE ARE THE " + site_name.upper() + " RESULTS...")
    print("--------------------------------")
    print("\n")
    for job in arr1:
        print(job)
    for job in arr2:
        print(job)

def generateIndeedJobPostingLinkPageWithJKValue(jk_value):
    return('https://www.indeed.com/viewjob?jk=' + jk_value + '&q=python&tk=1fp5bs022u3ei801&from=web&advn=2600498686408392&adid=381915096&ad=-6NYlbfkN0BUqc42VoWA1IUzFhs_b-r9PP2duAgXnd_bSymumAJSOb9rNH0up1uGiy0HfIQKs8PcgPsFiflxpznzL8-zsjDUiE20bhRcGokm5Olu7HJ0KAYZmdQ75QRQr9fzN4makSgOm3CHYt74H5oO1LcyZQwvh2jBedI6La2zBx9i4EB1YVE0VbUQdtA-7VZTeI_NsXMpDz_C-_nlpgwvqhYeARzkizosAY4x1vh7W0GmhgH7irRUAGD4XLrS941h7dOn7zjmV6t6wlsYmKJjsoppyW157tpe0kaQG_95RnQ1LbW2j8vmTPO2-LjJ-o3pJQpf1HjaHW6Bjl0DePRNQcT2DoA3vqDKsxxSntf1pTTFT9R6SqWx1WsczvtK&pub=4a1b367933fd867b19b072952f68dceb&vjs=3')
