#存放：pickling，读取：unpickling
import pickle
mlist = [1, 'HTY']
mfile = open( './python/myPickle.txt', 'wb' )
pickle.dump( mlist, mfile )
mfile.close()

mfile = open( './python/myPickle.txt', 'rb' )
mlist2 = pickle.load(mfile)
print(mlist2)