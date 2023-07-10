import re

my_pattern = r"[A-Z][\S]{3}\s[\w]{4}\sa\s[\w]{6}\s[\w]{3}\s[\w]{5}\.|[A-Z][\w]{3}\s[\w]{7}\s[\S]{5}\s[\w]{6}\s[\w]{5}\,\s[\w]{3}\?|[A-Z][\w]{4}\s[\w]{5}\'s\s[\w]{4}\s[\w]{3}\s[\w]{2}\s[\w]{3}\."
my_regex = re.compile(my_pattern)

