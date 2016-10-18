# @Processor: SearchAlgorithom
# @Version  : 0.0.1
# @Author   : hak

import pprint
import ast

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
    pprint.pprint(doc[0][2])

    page_doc_count_string = doc[0][2]

    # String to dictionary convert
    page_doc_count_dic = ast.literal_eval(page_doc_count_string)
    pprint.pprint(page_doc_count_dic['1'])

    print('-----------------')

    # Append page_doc_count in page_title tuple
    page_title = page_title + (33,)
    pprint.pprint(page_title)
    print('-----------------')

getData()