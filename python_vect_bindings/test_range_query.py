#!/usr/bin/python

import sys
import nmslib_vector

def read_data(fn):
    with open(fn) as f:
      for line in f:
        yield [float(v) for v in line.strip().split()]


space_type = 'cosinesimil'
space_param = []
method_name = 'vptree'
index_name  = method_name + '.index'
index = nmslib_vector.init(
                         space_type,
                         space_param,
                         method_name,
                         nmslib_vector.DataType.VECTOR,
                         nmslib_vector.DistType.FLOAT)

for id, data in enumerate(read_data('sample_dataset.txt')):
    nmslib_vector.addDataPoint(index, id, data)

index_param = []
query_time_param = ["alphaLeft=1.0", "alphaRight=1.0"]

nmslib_vector.createIndex(index, index_param)
nmslib_vector.setQueryTimeParams(index,query_time_param)

k = 0.02
for idx, data in enumerate(read_data('sample_queryset.txt')):
    print idx, nmslib_vector.rangeQuery(index, k, data)
    if idx > 10:
        break


