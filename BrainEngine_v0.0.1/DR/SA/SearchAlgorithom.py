# @Processor: SearchAlgorithom
# @Version  : 0.0.1
# @Author   : hak

import pprint

import DR.DataRetriverModel as DPModel

def getData():

    search_query = 'stack'

    # Title based filter
    page_title = DPModel.getTitle(search_query)
    pprint.pprint(page_title)
    print('-----------------')

    # Doc count based filter
    doc = DPModel.getDoc(search_query)
    pprint.pprint(doc)
    print('-----------------')

    # Append page_doc_count in page_title tuple
    page_title = page_title + (33,)
    pprint.pprint(page_title)
    print('-----------------')

getData()