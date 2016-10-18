# @Processor : DataRetriver Engine
# @Author    : hak

import DR.SA.SearchAlgorithom as SA

def startDataRetriver():
    search_query = 'stack'
    SA.getData(search_query)

startDataRetriver()