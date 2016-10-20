# @Processor: SearchAlgorithom
# @Version  : 0.0.1
# @Author   : hak

import pprint
import ast
from operator import itemgetter

import DR.DataRetriverModel as DPModel

def getData():

    search_query = 'stack'                           # For testing

    # Get page info from pages Table
    page_title = DPModel.getTitle(search_query)      # Title based filter
    pprint.pprint(page_title)
    print('-----------------')

    # Get doc from page_docs Table
    doc = DPModel.getDoc(search_query)               # Doc count based filter

    # Assign page doc count in variable
    page_doc_count_string = doc[0][2]

    # String to dictionary conversion
    page_doc_count_dic = ast.literal_eval(page_doc_count_string)
    pprint.pprint(page_doc_count_dic)
    print('-----------------')

    page_info_with_doc_count = []                 # Initialize a tuple
    for page_info in page_title:                  # Loop page info
        page_id = page_info[0]

        # Append doc_count in page_info tuple
        page_info = page_info + (page_doc_count_dic[str(page_id)],)

        # Append page_info in page_info_with_doc_count
        page_info_with_doc_count.append(page_info)

    pprint.pprint(page_info_with_doc_count)
    print('-----------------')

    # page_info_with_doc_count sort by doc_count
    page_info_with_doc_count.sort(key=itemgetter(3), reverse=True)
    pprint.pprint(page_info_with_doc_count)

getData()