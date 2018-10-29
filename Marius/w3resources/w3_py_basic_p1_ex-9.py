# w3resources-9
# Write a Python program to display the examination schedule. (extract the date from exam_st_date).

exam_st_date = (11, 12, 2014)

# ma ideea
# print(type(exam_st_date))
# print(len(exam_st_date))
print("The examination will start from : {} / {} / {}".format(exam_st_date[0],exam_st_date[1],exam_st_date[2]))
# official solution
print("The examination will start from : %i / %i / %i"%exam_st_date)
