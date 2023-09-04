import shutil
import sys

#def disk_usage(full_path):
def disk_usage(full_path, percentage_limit, limit_in_GB):
    space = shutil.disk_usage(full_path)
    toal_space_in_GB = space.total/(1024*1024*1024)
    used_space_in_GB = space.used/(1024*1024*1024)
    free_space_in_GB = space.free/(1024*1024*1024)

    print(toal_space_in_GB)
    print(used_space_in_GB)
    print(free_space_in_GB)
    if space.free/space.total*100 < percentage_limit or free_space_in_GB < limit_in_GB:
        print("Not enough Free Space Left")
        sys.exit(1)
    else:
        print("Enough Free Space Left")
        #return 0

disk_usage("/", 25, 20)

