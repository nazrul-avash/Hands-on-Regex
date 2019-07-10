Regex_Pattern = r'^([a-zA-Z]|[02468]){40}([\s]|[13579]){5}$'	# Do not delete 'r'.

import re

print(str(bool(re.search(Regex_Pattern, input()))).lower())