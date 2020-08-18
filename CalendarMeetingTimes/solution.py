'''
WIP
Given two calendars with daily bounds, find all time slots where
an interview of minimum length can be held for both people
'''



c1 = [['9:00','10:30'],['12:00','13:00'],['16:00','18:00']]
c1_bounds = ['9:00','20:00']

c2 = [['10:00','11:30'],['12:30','14:30'],['16:00','17:00']]
c2_bounds = ['10:00','18:30']

interview_time = 30


def intFromTime(time):
    time = list(time)
    time.remove(':')
    hours = int(''.join(time[0]+time[1]))
    minutes = int(''.join(time[2]+time[3]))
    minutes_to_decimal = minutes / 60
    time = hours + minutes_to_decimal
    return time

def getFreeBlocks(cal, bounds):
    free_blocks = []
    for i in range(len(cal)-1):
        start_free = cal[i][1]
        end_free = cal[i+1][0]
        free_blocks.append([start_free,end_free])

    if cal[-1][1] != bounds[1]:
        free_blocks.append([cal[-1][1],bounds[1]])

    return free_blocks

def getBothFreeBlocks(c1_avail, c2_avail, c1_bounds, c2_bounds):
    both_free_blocks = []
    for i in range(min(len(c1_avail),len(c2_avail))-1):
        start_free = max(c1_avail[i][1],c2_avail[i][1])
        end_free = min(c1_avail[i+1][0],c2_avail[i+1][0])
        both_free_blocks.append([start_free,end_free])

def getInterviewBlocks(both_avail, interview_time):
    interview_times = []
    for block in both_avail:
        if intFromTime(block[1]) - intFromTime(block[0]) > int(interview_time):
            interview_times.append(block)

    return interview_times

def main():
    c1_avail = getFreeBlocks(c1, c1_bounds)
    c2_avail = getFreeBlocks(c2, c2_bounds)

    both_avail = getBothFreeBlocks(c1_avail, c2_avail, c1_bounds, c2_bounds)

    interview_avail = getInterviewBlocks(both_avail, interview_time)

    return interview_avail

print(main())
