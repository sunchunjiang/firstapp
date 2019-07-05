#coding: utf-8
from time import ctime
def splitFile(fileLocation, targetFoler):
   file_handler = open(fileLocation, 'r')
   # 定义每个小文件的行数
   block_size = 100
   line = file_handler.readline()
   temp = []
   countFile = 1
   count = len(open(r"%s" % fileLocation,'rU').readlines())
   while line:
       for i in range(block_size):
    # 到最后一行的时候将temp列表中内容写入到文件中
           if i == (block_size-1):
               # write block to small files
               file_writer = open(targetFoler + "file_"+str(countFile)+".txt", 'a+')
               file_writer.writelines(temp)
               file_writer.close()
               temp = []
               print "  file " + str(countFile) + " generated at: " + str(ctime())
               countFile = countFile + 1
           else:
               temp.append(file_handler.readline())
    #切割文件数量
       if countFile == count/(block_size -1) + 2:
               break;
 
   file_handler.close()
 
if __name__ == '__main__':
   print "Start At: " + str(ctime())
   splitFile("/root/server.log", "/tmp/")
