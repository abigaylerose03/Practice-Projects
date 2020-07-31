
from heapq import heappush, heappop
import sys

class Interval(object):
	def __init__(self, start, end):
		self.start = start
		self.end = end

class MeetingRooms:
	def minMeetingRooms(self, intervals):
		if not intervals:
			return 0
		sorted_intervals = sorted(intervals, key=lambda it: (it.start, it.end))

		cnt = 0
		heap = []

		print([(i.start, i.end) for i in sorted_intervals])

		for it in sorted_intervals:
			start, end = it.start, it.end
			while heap and heap[0] <= start:
				heappop(heap)

			heappush(heap, end)

			cnt = max(len(heap), cnt)
		return cnt

myClasses = {
    "interval01": (0, 20),
    "interval02": (10, 40),
    "interval03": (50, 100)
    }
instances = []
for i in myClasses.values():
    instances.append(Interval(i[0],i[1]))
meetingRoom = MeetingRooms()
print(meetingRoom.minMeetingRooms(instances)) 

# myInstances = []
# myClasses = {
#     "interval01": (0, 20),
#     "interval02": (10, 40),
#     "interval03": (50, 100)
#     }

# for thisClass in myClasses.keys():
#     exec("%s = Interval('%s', '%s')" % (thisClass, myClasses[thisClass][0], myClasses[thisClass][1]))
#     myInstances.append(getattr(sys.modules[__name__], thisClass))

# meetingRoom = MeetingRooms()
# print(meetingRoom.minMeetingRooms(myInstances))