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

    # Doc count based filter
    doc = DPModel.getDoc(search_query)

getData()