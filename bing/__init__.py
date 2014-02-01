import urllib
import urllib2
import json
import sys
import pprint
from decimal import Decimal
from collections import Counter

BASE_URL = 'https://api.datamarket.azure.com/Data.ashx/Bing/SearchWeb/v1/Web'
DEFAULT_RESULT_SIZE = '10'
FORMAT = 'json'
DEFAULT_PARAMS = '&$top=%s&$format=%s' %(DEFAULT_RESULT_SIZE, FORMAT)
ACCOUNT_KEY = '5Cgycv24wwwQE8XuUZeDMrFsMH4F3HSlSHjz1b5ubK4'

SEARCH_STARTS = "\n .d8888b.                                    888                    888                     888\nd88P  Y88b                                   888                    888                     888\nY88b.                                        888                    888                     888\n \"Y888b.    .d88b.   8888b.  888d888 .d8888b 88888b.       .d8888b  888888  8888b.  888d888 888888 .d8888b\n    \"Y88b. d8P  Y8b     \"88b 888P\"  d88P\"    888 \"88b      88K      888        \"88b 888P\"   888    88K\n      \"888 88888888 .d888888 888    888      888  888      \"Y8888b. 888    .d888888 888     888    \"Y8888b.\nY88b  d88P Y8b.     888  888 888    Y88b.    888  888           X88 Y88b.  888  888 888     Y88b.       X88\n \"Y8888P\"   \"Y8888  \"Y888888 888     \"Y8888P 888  888       88888P'  \"Y888 \"Y888888 888      \"Y888  88888P \n"
SEARCH_CONTINUES = "\n .d8888b.                                    888                                     888    d8b                                     \nd88P  Y88b                                   888                                     888    Y8P                                     \nY88b.                                        888                                     888                                            \n \"Y888b.    .d88b.   8888b.  888d888 .d8888b 88888b.        .d8888b .d88b.  88888b.  888888 888 88888b.  888  888  .d88b.  .d8888b  \n    \"Y88b. d8P  Y8b     \"88b 888P\"  d88P\"    888 \"88b      d88P\"   d88\"\"88b 888 \"88b 888    888 888 \"88b 888  888 d8P  Y8b 88K      \n      \"888 88888888 .d888888 888    888      888  888      888     888  888 888  888 888    888 888  888 888  888 88888888 \"Y8888b. \nY88b  d88P Y8b.     888  888 888    Y88b.    888  888      Y88b.   Y88..88P 888  888 Y88b.  888 888  888 Y88b 888 Y8b.          X88 \n \"Y8888P\"   \"Y8888  \"Y888888 888     \"Y8888P 888  888       \"Y8888P \"Y88P\"  888  888  \"Y888 888 888  888  \"Y88888  \"Y8888   88888P \n"
SEARCH_ENDS = "\n .d8888b.                                    888                                  888          \nd88P  Y88b                                   888                                  888          \nY88b.                                        888                                  888          \n \"Y888b.    .d88b.   8888b.  888d888 .d8888b 88888b.        .d88b.  88888b.   .d88888 .d8888b  \n    \"Y88b. d8P  Y8b     \"88b 888P\"  d88P\"    888 \"88b      d8P  Y8b 888 \"88b d88\" 888 88K      \n      \"888 88888888 .d888888 888    888      888  888      88888888 888  888 888  888 \"Y8888b. \nY88b  d88P Y8b.     888  888 888    Y88b.    888  888      Y8b.     888  888 Y88b 888      X88 \n \"Y8888P\"   \"Y8888  \"Y888888 888     \"Y8888P 888  888       \"Y8888  888  888  \"Y88888  88888P \n"